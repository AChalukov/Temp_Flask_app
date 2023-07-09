#!/usr/bin/python

from flask import Flask
from flask import render_template
import os

app = Flask(__name__)

env=os.getenv('ENV')

@app.route("/")
def home():
    return "Hello Nik"

if __name__ == "__main__":  
         app.run(host='0.0.0.0',port=80,debug=True)
