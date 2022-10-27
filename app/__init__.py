from flask import Flask
from urllib.parse import quote
from flask import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:%@localhost/flashsaledb?charset=utf8mb4" % quote('Admin123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app = app)