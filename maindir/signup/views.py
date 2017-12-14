from flask import Blueprint, render_template, request, redirect, url_for, flash, get_flashed_messages
from maindir import models as db_handler
from pymongo import MongoClient
from maindir.security.models import security

# blueprint for this .py
signup_blueprint = Blueprint('signup', __name__, template_folder='templates')

client = MongoClient('mongodb://localhost:27017/')
db = client.pgco


# collection = db.verified_users


# signup page


@signup_blueprint.route('/', methods=['GET', 'POST'])
def signup():
    return render_template('signup/signup.html')


# checking user and pass

#
#TODO have to do somthing
@signup_blueprint.route('/processing', methods=['POST'])
def signing_processing():
    # user_array = db_handler.retrieveUsers()
    collection = db.users
    find = collection.find_one({'email': request.form['email']})
    if find:
        flash('this email is already exists. please log in or use another email', 'signup')
        return redirect(url_for('signup.signup'))
    else:
        hashed_password = security.set_password(request.form['password'])
        user = {'email': request.form['email'], 'password': hashed_password}
        collection.insert_one(user).inserted_id
        return 'done'


# u = collection.find({'email': request.form['email']})
#     for i in u:
#         if request.method == 'POST':
#             mail = request.form['email']
#             if request.form['email'] == u.find_one({'email': mail}):  # if email was already exists
#                 flash('this email is already exists. please log in or use another email', 'signup')
#                 return redirect(url_for('signup.signup'))
#
#             else:
#                 print('done')
#                 return redirect(url_for('signup.signed_up'))  # if both username and password were correct
#
#
# redirect authenticated users to main page


@signup_blueprint.route('/signed_up')
def signed_up():
    return '<h1>done !</h1>'



@signup_blueprint.route('/test')
def test():
    mhasani = {
        'email': "mohammad@live.com",
        'passwrod': 'pass',
        'name': 'mohammad',
        'family': 'hasani',
        'asdasdasd': 'asdasdasdasd'
    }
    collection = db.username
    x = collection.insert_one(mhasani).inserted_id
    y = collection.find_one({'email': 'mohammaasdasdasdd@live.com'})

    print(y)
    return 'ok'
