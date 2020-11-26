from flask import Flask
from src.config import Config
from flask_mail import Mail

src = Flask(__name__)

src.config.from_object(Config)
mail = Mail(src)

from src import routes