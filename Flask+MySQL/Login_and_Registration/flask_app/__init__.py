# __init__.py
from flask import Flask
app = Flask(__name__)
app.secret_key = "mi secreto"
DATABASE = "login_and_registration_schema"