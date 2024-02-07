#!/usr/bin/env python3
"""
Basic Flask app for deploying Flask based application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    hello world template
    """
    return render_template('0-index.html')
