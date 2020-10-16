from datetime import datetime
import os
from urllib.parse import urlparse
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import matplotlib.pyplot as plt
import numpy as np
import binascii
from PIL import Image
import requests as req
from io import BytesIO

from flask import Blueprint, render_template
from flask import request, flash, redirect, url_for
from flask_login import login_required, logout_user, login_user, current_user

from app import db
from ..models.user import User, Photo
from .forms.login import LoginForm
from .forms.recover import SearchAccountForm, ResetPasswordForm
from .forms.detection import UploadFromLocal, UploadFromURL

from ..settings import UPLOAD_FOLDER, ALLOWED_EXTENSIONS
from ..utils.FaceMaskDetection.run_detection import start

bp = Blueprint('detection', __name__, template_folder='../templates')


@bp.route('/home')
@login_required
def home():
    form1 = UploadFromURL()
    form2 = UploadFromLocal()
    return render_template('home.html', form1=form1, form2=form2)

    
@bp.route('/upload_history/')
@login_required
def upload_history():

    all_photos = Photo.query.filter(Photo.user_id == current_user.id).all()

    return render_template('history.html', all_photos=all_photos)


@bp.route('/detection_url', methods=['POST', 'GET'])
@login_required
def detection_url():
    form1 = UploadFromURL()
    form2 = UploadFromLocal()

    if form1.validate_on_submit():
        url = form1.photo.data
        suffix = os.path.splitext(urlparse(url).path)[-1]
        if suffix[1:] not in ALLOWED_EXTENSIONS:
            flash(u'Not a valid image url.')
        else:
            dt1 = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
            
            response = req.get(url) 
            frame = Image.open(BytesIO(response.content)) 
            frame = np.array(frame)
            b,g,r = cv2.split(frame)
            frame = cv2.merge([r,g,b])

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

            # detection results
            print('nfaces', nfaces)
            print('nmasks', nmasks)
            print('photo_type', photo_type) 
            img = Image.open(output_save_path) 
            img.show()

            # db
            photo_object = Photo(photo_name= photo_name, output_name=output_name,  
                                nfaces=nfaces, nmasks=nmasks, photo_type=photo_type, user_id=current_user.id)
            db.session.add(photo_object)
            db.session.commit()

            flash(u'Image successfully uploaded!')
            return redirect(url_for('detection.home'))
    else:
        flash(u'Valid url required.')
    return render_template('home.html', form1=form1, form2=form2)


@bp.route('/home', methods=['POST', 'GET'])
@login_required
def detection_local():
    form1 = UploadFromURL()
    form2 = UploadFromLocal()
    if form2.validate_on_submit():
        photo = form2.photo.data

        if photo and photo.filename:
            dt1 = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")

            response = photo.read()
            frame = cv2.imdecode(np.fromstring(response, np.uint8), cv2.IMREAD_COLOR)
            
            # detection
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
            print('nfaces', nfaces)
            print('nmasks', nmasks)
            print('photo_type', photo_type) 
            img = Image.open(output_save_path) 
            img.show()

            # db
            photo_object = Photo(photo_name=photo_name, output_name=output_name, 
                                nfaces=nfaces, nmasks=nmasks, photo_type=photo_type, user_id=current_user.id)
            db.session.add(photo_object)
            db.session.commit()

            flash(u'Image successfully uploaded!')
            return redirect(url_for('detection.home'))
    else:
        flash(u'Please upload an image.')
    return render_template('home.html', form1=form1, form2=form2)
