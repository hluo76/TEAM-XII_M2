from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '13645eeeb0e11277a226d0e2afe38aa0'

from DemoApp import main

