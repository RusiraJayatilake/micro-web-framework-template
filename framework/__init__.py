from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# ---- DB Connection ----
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = "random string"

# ---- SQLAlchemy for DB ----
db = SQLAlchemy(app) 

def run_app():

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    with app.app_context():
        db.create_all()
        print('Database created!')

    return app