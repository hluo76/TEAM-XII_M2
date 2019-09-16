from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '34987rh3o4fhwofn23490'

from DemoApp import main

