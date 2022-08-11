from flask import Flask
from app.config import FLASK_DEBUG, FLASK_SECRET
# from app.forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.secret_key = FLASK_SECRET
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://t_meet_admin:admin@localhost/t_meet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from app import routes