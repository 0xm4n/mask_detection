from uuid import uuid4
from datetime import datetime
import os
import cv2
import numpy as np
from PIL import Image


from flask import Blueprint, render_template
from flask import flash, redirect, url_for, request
from flask import jsonify
from flask_login import login_required, logout_user, login_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from ..models.user import User
from ..models.photo import Photo
from sqlalchemy.sql import exists
from .forms.api_form import RegisterForm, UploadForm

from ..settings import UPLOAD_FOLDER, ALLOWED_EXTENSIONS
from ..utils.FaceMaskDetection.run_detection import start

bp = Blueprint('api', __name__, template_folder='../templates/api')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('register.html', form=form)
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        is_exist = db.session.query(exists().where(User.username == username)).scalar()
        if is_exist:
            res = jsonify(
                success = False,
                error = {
                    "code": 400,
                    "message": "That username is taken. Try another."
                }
            )
        else:
            password = generate_password_hash(password)
            user = User(str(uuid4()), username, "", password, 1, 1)
            db.session.add(user)
            db.session.commit()
            success = True
            code = 200
            message = "Success"
            res = jsonify(
                success = True
            )
        return res


@bp.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()

    if request.method == 'GET':
        return render_template('upload.html', form=form)

    elif request.method == 'POST':
        status = 0
        msg = ''
        if form.validate_on_submit():

            username = request.form.get('username')
            password = request.form.get('password')

            user = User.query.filter_by(username=username).first()
            if user and check_password_hash(user.password, password) == True:
                login_user(user)
                # Detection
                photo = form.photo.data

                if photo and photo.filename:
                    dt1 = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")

                    response = photo.read()
                    frame = cv2.imdecode(np.fromstring(response, np.uint8), cv2.IMREAD_COLOR)
                    
                    # detect
                    nfaces, nmasks, photo_type, photo_ori, photo_out = start(frame)
                    
                    # save detection img
                    suffix = os.path.splitext(photo.filename)[-1]
                    
                    save_folder = os.path.join(UPLOAD_FOLDER, str(current_user.id))
                    if not os.path.exists(save_folder):
                        os.makedirs(save_folder)
                    photo_name = dt1 + suffix
                    dt2 = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
                    output_name = dt2 + suffix
                    photo_save_path = os.path.join(save_folder, photo_name)
                    output_save_path = os.path.join(save_folder, output_name)

                    # for windows
                    photo_save_path = photo_save_path.replace('\\', '/')
                    output_save_path = output_save_path.replace('\\', '/')

                    input_img = Image.fromarray(photo_ori)
                    output_img = Image.fromarray(photo_out)
                    cv2.imwrite(photo_save_path, np.array(input_img))
                    cv2.imwrite(output_save_path, np.array(output_img))

                    # show detection results
                    img = Image.open(output_save_path) 
                    img.show()

                    # db
                    photo_object = Photo(photo_name=photo_name, output_name=output_name, 
                                        nfaces=nfaces, nmasks=nmasks, photo_type=photo_type, user_id=current_user.id)
                    db.session.add(photo_object)
                    db.session.commit()
                    
                    status = 1
            else:
                msg = "Not logged in or wrong password."
        else:
            msg = "Upload failed."    

        if status == 0:
            res = jsonify(
                success = False,
                error = {
                    "code": 400,
                    "message": msg
                }
            )
        elif status == 1:
            res = jsonify(
                success = True,
                payload={
                    "num_faces": nfaces,
                    "num_masked": nmasks,
                    "num_unmasked": nfaces - nmasks,
                }
            )
        return res

