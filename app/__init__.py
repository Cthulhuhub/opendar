import os
from flask import Flask, render_template, request, session
from flask_cors import CORS
from flask_migrate import Migrate

app = Flask(__name__)

from .config import Config

app.config.from_object(Config)