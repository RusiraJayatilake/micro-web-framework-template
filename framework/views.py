from flask import Blueprint, render_template, request, redirect, jsonify

views = Blueprint('views', __name__)

# @views.route('/')
# def front_page():
#     msg = "Application Running Successfully"
#     return jsonify(msg)


@views.route('/')
def front_page():
    return render_template('index.html')