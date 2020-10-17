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
│   ├── controllers
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

## API

### Oauth.login()
#### Description: 
Identifying and authenticating an user. Takes parameters username and password. Returns whether or not login was successful. If it's an admin account, render a template with higher privilege.
#### Method: `POST`
#### Path: `/oauth/login`
#### Parameter
| Field        | Type           | Description              |
| -------------|----------------|--------------------------|
| username     | String         |                          |
| password     | String         |                          |
#### Success response
| Field        | Type           | Description              |
| -------------|----------------|--------------------------|
| id           | String         | The Users-ID             |
| username     | String         |                          |
| role         | Integer        | Admin / User             |

#### Error response
| Field            | Description                                     |
| -----------------|-------------------------------------------------|
| NoAccessRight    | Only authenticated Account can access the data. |
| UserNotFound     | The username of the User was not found.         |
| PasswordWrong    | The password is not correct.                    |

---

### Oauth.logout()
#### Description: 
User will be logged out, and any cookies for their session will be cleaned up.
#### Method: `GET`
#### Path: `/oauth/logout`
#### Success response
| Field        | Type           | Description              |
| -------------|----------------|--------------------------|
| code         | Integer        | 200(success)             |
---
### Oauth.forget_password()
#### Description: 
Enter the username to reset user's password. This API will send the password reset instructions to the email address for this account.
The reset link has a parameter called token, which generate by using encryption algorithm with the user's username and an expire time.
#### Method: `POST`
#### Path: `/oauth/forget_password`
#### Parameter
| Field        | Type           | Description              |
| -------------|----------------|--------------------------|
| username     | String         |                          |
#### Success response
| Field        | Type           | Description              |
| -------------|----------------|--------------------------|
| code         | Integer        | 200(success)             |
#### Error response
| Field            | Description                                     |
| -----------------|-------------------------------------------------|
| UserNotFound     | The username of the User was not found.         |
| EmailNotSpecified| This account didn't specified an email.         |
| InvalidEmailAddr | The email address is invalid.                   |

---

### Oauth.reset_password()
#### Description: 
After request for a reset password email, user can click the link, which has a token containing user's encryption information.
The API will decode the token to get user's username from the token and check whether the token has expired. If not, update user's password.
#### Method: `POST`
#### Path: `oauth/reset-password/<token>`
#### Parameter
| Field        | Type           | Description                                                             |
| -------------|----------------|-------------------------------------------------------------------------|
| token        | String         | Generate by using encryption algorithm with username and an expire time.|
#### Success response
| Field        | Type           | Description              |
| -------------|----------------|--------------------------|
| code         | Integer        | 200(success)             |
#### Error response
| Field            | Description                  |
| -----------------|------------------------------|
| TokenExpired     | The token has expired        |

---
### Oauth.change_password()
#### Description: 
Users can change their password after login in the system.
#### Method: `POST`
#### Path: `/oauth/forget_password`
#### Parameter
| Field        | Type           | Description              |
| -------------|----------------|--------------------------|
| old_password | String         |                          |
| new_password | String         |                          |
| confirm      | String         |                          |
#### Success response
| Field        | Type           | Description              |
| -------------|----------------|--------------------------|
| code         | Integer        | 200(success)             |
#### Error response
| Field            | Description                                     |
| -----------------|-------------------------------------------------|
| PasswordWrong    | The old password is not correct.                |

---
### Admin.add_user()
#### Description: 
The administrator can create additional user/admin accounts. Only admin account has the privilege to use this API.
#### Method: `POST`
#### Path: `/admin/add_user`
#### Parameter
| Field        | Type           | Description              |
| -------------|----------------|--------------------------|
| username     | String         |                          |
| password     | String         |                          |
| confirm      | String         | Confirm password         |
| email        | String         | For password reset       |
| role         | Integer        | Admin(1) / User(0)       |
#### Success response
| Field        | Type           | Description              |
| -------------|----------------|--------------------------|
| code         | Integer        | 200(success)             |
#### Error response
| Field            | Description                                      |
| -----------------|--------------------------------------------------|
| UsernameExists   | The username is taken.                           |
| PermissionDenied | Account don't have permission to access this API.|


---
### Admin.delete_user()
#### Description: 
User account can be delete by Admin(Admin account can not be deleted).
#### Method: `POST`
#### Path: `/admin/delete_user`
#### Parameter
| Field        | Type           | Description              |
| -------------|----------------|--------------------------|
| username     | String         |                          |

#### Success response
| Field        | Type           | Description              |
| -------------|----------------|--------------------------|
| code         | Integer        | 200(success)             |


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

