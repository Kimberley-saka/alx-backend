#!/usr/bin/env python3
"""
simple flask app
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello():
    """
    displays hello world
    """
    return render_template('0-index.html')
