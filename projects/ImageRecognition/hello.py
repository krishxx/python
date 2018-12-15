# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 10:48:06 2017

@author: Srikrishna.Sadula
"""
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"