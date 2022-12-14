from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_babelex import Babel
import cloudinary

app = Flask(__name__)
app.secret_key = '^%#$%BGHB5yy542@$%@%$gv4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/it02saledbv1?charset=utf8mb4' % quote('Admin@123')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['CART_KEY'] = 'cart'

db = SQLAlchemy(app=app)

login = LoginManager(app=app)

cloudinary.config(cloud_name='', api_key='', api_secret='')

babel = Babel(app=app)


@babel.localeselector
def load_locale():
    return "vi"
