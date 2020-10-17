# Mask Detection

Mask Detection is a simple web application that uses AI to determine
whether individuals that show up in a picture are wearing a face mask.

## Features
- Login panel. With authentication to access to the application. 
- Password recovery. User can reset his/her password with his/her email address.
- User management. The administrator is able to create additional user accounts.
- Permission control. User accounts have access to all features except create/delete user accounts.
- Mask detections.
- Upload history.


## Dependencies
At the bare minimum you'll need the following for your development environment:
    
- [Python](http://www.python.org/)
- [Virtualenv](https://python-guide.readthedocs.org/en/latest/dev/virtualenvs/#virtualenv)

MaskDetection is based on Python and depends on the following major components:
* [Flask](http://flask.pocoo.org/): Web application microframework for Python
* [SQLite](https://www.sqlite.org/): RDBMS 
* [Flask-SQLAlchemy](http://flask-sqlalchemy.palletsprojects.com): ORM framework for SQLite
* [Flask-WTF](https://flask-wtf.readthedocs.io/): A flexible forms validation and rendering library
* [Flask-Login](https://flask-login.readthedocs.io/): Provides user session management for Flask
* [Flask-Mail](https://pythonhosted.org/Flask-Mail/): Sends emails to users for password reset.

The process of installing all these components and setting up a server is described below.
## Local Setup

The following assumes you have all of the two essential tools listed above installed.
#### 1. Clone the project:

    $ git clone https://github.com/zhenyit/mask_detection.git
    $ cd mask_detection
    
#### 2. Create and initialize virtualenv for the project:

    $ virtualenv venv
    $ pip install -r requirements.txt

#### 3. Run the development server:

    $ python run.py
Visit: http://localhost:5000

## Project Structure
```
├── app
│   ├── handlers
│   │   ├──blueprint.py
│   │   └──forms
│   ├── models
│   │   └──model.py
│   ├── static
│   │   ├──css
│   │   └──img
│   ├── templates
│   ├── utils
│   ├── .env
│   ├── __init__.py
│   └── settings.py
├── README.md
├── requirements.txt
└── run.py
```
```
app/controllers     Controller handles the user request.
app/models          Model class represents the shape of the data. 
app/templates       Templates display model data and provide a user interface. 
app/static          Static resource files like css, img.
app/utils           Third-party libraries like flask-login, flask-mail used as util.
app/__init__.py     Create_app().
app/settings.py     Configuration file 
```

## Contact
- Bugs and feature request can be submitted here on [GitHub](https://github.com/zhenyit/mask_detection/issues).
- Patches should be submitted using the [Pull Request](https://github.com/zhenyit/mask_detection/pulls) system of GitHub.
- [Zhenyi Tang]  zhenyi.tang@mail.utoronto.ca
- [Ran He]       abby.he@mail.utoronto.ca
- [Macious Peng] macious.peng@mail.utoronto.ca

## License
MIT License
Copyright (c) 2020 Zhenyi Tang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

##API

| Method        | URL           | Cool  |
| ------------- |:-------------:| -----:|
| GET     | right-aligned | $1600 |
| GET      | centered      |   $12 |
| GET | are neat      |    $1 |