from flask import Blueprint, render_template, request, redirect, url_for, flash, get_flashed_messages
from maindir import models as db_handler
from pymongo import MongoClient

# blueprint for this .py
login_blueprint = Blueprint('login', __name__, template_folder='templates')


# login page


@login_blueprint.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login/login.html')


# checking user and pass


@login_blueprint.route('/processing', methods=['POST'])
def logging_processing():
    user_array = db_handler.retrieveUsers()
    for i in user_array:
        if request.method == 'POST':
            if request.form['username'] != i[0] and request.form['password'] == i[1]:  # if username was wrong
                flash('this username does not exist. please check the username and try again', 'login')
                return redirect(url_for('login.login'))
            elif request.form['username'] != i[0] and request.form['password'] != i[1]:  # if both username and password
                flash('this username does not exist. please check the username and try again', 'login')  # were wrong
                return redirect(url_for('login.login'))
            elif request.form['username'] == i[0] and request.form['password'] != i[1]:  # if username was correct
                flash('password is wrong. please check and try again', 'login')  # but password was not
                return redirect(url_for('login.login'))
            else:
                return redirect(url_for('login.logged_in'))  # if both username and password were correct


# redirect authenticated users to main page


@login_blueprint.route('/logged_in')
def logged_in():
    return '<h1>welcome !</h1>'

#
# @login_blueprint.route('/test1')
# def logged1():
#     flash("i'm coming from test1", 'login')
#     return 'this is test'
#
#
# @login_blueprint.route('/test2')
# def logged2():
#     return render_template('test.html')
