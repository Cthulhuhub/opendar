import os
from flask import Flask, render_template, request, session
from flask_cors import CORS
from flask_migrate import Migrate

app = Flask(__name__)

from .config import Config
from .models import db

app.config.from_object(Config)
app.config['JSON_SORT_KEYS'] = False

db.init_app(app)

migrate = Migrate(app, db)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def react_root(path):
    print("path", path)
    if path == 'favicon.ico':
        return app.send_static_file('favicon.ico')
    return app.send_static_file('index.html')