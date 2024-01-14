from flask import Blueprint, render_template, request, redirect, jsonify

views = Blueprint('views', __name__)

# @views.route('/')
# def front_page():
#     msg = "Application Running Successfully"
#     return jsonify(msg)

@views.route('/')
def front_page():
    return render_template('index.html')


# CRUD Operations
@views.route('/add')
def add():
    # operation logic
    return render_template('add.html')

@views.route('/read')
def read():
    # operation logic
    return render_template('read.html')

@views.route('/update')
def update(id):
    # operation logic
    return render_template('update.html')

@views.route('/delete')
def delete(id):
    # operation logic
    return render_template('delete.html')


# Other Operations
@views.route('/search')
def search(id):
    # logic
    return render_template('search.html')
