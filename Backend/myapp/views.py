from . import db, app
from .models import User, Photo
from .forms import RegisterForm, LoginForm, UploadFromLocal, UploadFromURL
from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
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

from .FaceMaskDetection.run_detection import start



@app.route("/")
def index():
    return render_template("index.html")


@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()

        if user and user.verify_password_hash(password):
            login_user(user)
            flash('You are logged in!', category='info')
            return redirect(url_for('index'))
        else:
            flash('Incorrect username or password.', category='error')
    return render_template('login.html', title='Login', form=form)


@app.route('/auth/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # print('aaaaaaaaaaaa')
        username = form.username.data
        email = form.email.data
        password = form.password.data
        confirm = form.confirm.data
        user = User(username=username, email=email)
        user.set_password_hash(password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!')
        return redirect(url_for('login'))
    # print('bbbbbbbbbbbbb')
    return render_template('register.html', title='Register', form=form)


@app.route('/auth/logout')
@login_required
def logout():
    logout_user()
    flash('Goodbye!')
    return redirect(url_for('index'))



@app.route('/detection', methods=['POST', 'GET'])
@login_required
def detection():
    form = UploadFromLocal()
    if form.validate_on_submit():
        photo = form.photo.data

        if photo and photo.filename:

            response = photo.read()
            frame = cv2.imdecode(np.fromstring(response, np.uint8), cv2.IMREAD_COLOR)
            
            # detection
            nfaces, nmasks, photo_type, photo_ori, photo_out = start(frame)
            
            # save detection img
            suffix = os.path.splitext(photo.filename)[-1]
            dt = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
            save_folder = os.path.join(app.config['UPLOAD_FOLDER'], str(current_user.id))
            if not os.path.exists(save_folder):
                os.makedirs(save_folder)
            photo_name = dt + suffix
            output_name = dt + '_output' + suffix
            photo_save_path = os.path.join(save_folder, photo_name)
            output_save_path = os.path.join(save_folder, output_name)

            # for windows
            photo_save_path = photo_save_path.replace('\\', '/')
            output_save_path = output_save_path.replace('\\', '/')

            # photo_gallery_path = photo_gallery_path.replace('\\', '/')
            # output_gallery_path = output_gallery_path.replace('\\', '/')

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
        return redirect(url_for('detection'))
    return render_template('detection.html', title='Detection', form=form)


@app.route('/detection2', methods=['POST', 'GET'])
@login_required
def detection2():
    form = UploadFromURL()
    if form.validate_on_submit():
        url = form.photo.data
        
        response = req.get(url) 
        frame = Image.open(BytesIO(response.content)) 
        frame = np.array(frame)
        b,g,r = cv2.split(frame)
        frame = cv2.merge([r,g,b])

        # detection
        nfaces, nmasks, photo_type, photo_ori, photo_out = start(frame)

        # save detection img
        suffix = os.path.splitext(urlparse(url).path)[-1]
        dt = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
        save_folder = os.path.join(app.config['UPLOAD_FOLDER'], str(current_user.id))
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
        photo_name = dt + suffix
        output_name = dt + '_output' + suffix
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
        photo_object = Photo(photo_name= photo_name, output_name=output_name,  
                             nfaces=nfaces, nmasks=nmasks, photo_type=photo_type, user_id=current_user.id)
        db.session.add(photo_object)
        db.session.commit()
        return redirect(url_for('detection2'))
    return render_template('detection2.html', title='Detection2', form=form)


@app.route('/gallery/')
@login_required
def gallery():
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    all_photos = Photo.query.filter(Photo.user_id == current_user.id).all()

    return render_template('gallery.html', all_photos=all_photos, user=str(current_user.id))
