import os
import cv2
import numpy as np
import requests as req
from PIL import Image
from io import BytesIO
from datetime import datetime
from urllib.parse import urlparse

from flask import Blueprint, render_template
from flask import request, flash, redirect, url_for
from flask_login import login_required, logout_user, login_user, current_user

from app import db
from ..models.user import User, Photo
from .forms.detection import UploadFromLocal, UploadFromURL

from ..settings import UPLOAD_FOLDER, ALLOWED_EXTENSIONS
from ..utils.FaceMaskDetection.run_detection import start

bp = Blueprint('detection', __name__, template_folder='../templates')


@bp.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    url_form = UploadFromURL()
    file_form = UploadFromLocal()

    if request.method == 'GET':
        photo = Photo()
        return render_template('home.html', form1=url_form, form2=file_form, photo=photo)


@bp.route('/detection_url', methods=['GET', 'POST'])
@login_required
def detection_url():
    url_form = UploadFromURL()
    file_form = UploadFromLocal()
    time = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
    
    if url_form.validate_on_submit():
        try:
            url = url_form.photo.data
            suffix = os.path.splitext(urlparse(url).path)[-1]

            img = req.get(url)
            frame = Image.open(BytesIO(img.content))
            frame = np.array(frame)
            b, g, r = cv2.split(frame)
            frame = cv2.merge([r, g, b])
            
            result_photo = detection(frame, time, suffix)
            return render_template('home.html', form1=url_form, form2=file_form, photo=result_photo)
        except:  
            flash(u'The URL doesn\'t refer to an image, or the image is not publicly accessible.')
    else:  
        flash(u'The URL doesn\'t refer to an image, or the image is not publicly accessible.')

    return redirect(url_for('detection.home'))


@bp.route('/detection_file', methods=['GET', 'POST'])
@login_required
def detection_file():
    url_form = UploadFromURL()
    file_form = UploadFromLocal()
    time = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")

    if file_form.validate_on_submit():
        try:
            file = file_form.photo.data
            suffix = os.path.splitext(file.filename)[-1]
            img = file.read()
            frame = cv2.imdecode(np.fromstring(img, np.uint8), cv2.IMREAD_COLOR)
            
            result_photo = detection(frame, time, suffix)
            return render_template('home.html', form1=url_form, form2=file_form, photo=result_photo)
        except:
            flash(u'The image must be in one of the following formats: .jpg, .jpeg, .png, .bmp.')        
    else:
        flash(u'The image must be in one of the following formats: .jpg, .jpeg, .png, .bmp.')
        
    return redirect(url_for('detection.home'))


def detection(frame, dt1, suffix):
    # detection
    nfaces, nmasks, photo_type, photo_ori, photo_out = start(frame)

    # save detection img
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

    # db
    photo_object = Photo(photo_name=photo_name, output_name=output_name,
                         nfaces=nfaces, nmasks=nmasks, photo_type=photo_type, user_id=current_user.id)
    db.session.add(photo_object)
    db.session.commit()
    error = u'Image successfully uploaded!'
    return photo_object


@bp.route('/upload_history/')
# @login_required
def upload_history():
    all_photos = Photo.query.filter(Photo.user_id == current_user.id).all()

    return render_template('history.html', all_photos=all_photos)
