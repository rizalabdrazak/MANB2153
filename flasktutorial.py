# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 15:32:13 2018

@author: PCPC
"""

from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')

def home():
    return render_template("home.html")

@app.route('/AboutUs/')

def about():
    return render_template("aboutus.html")

@app.route('/CompanyProfile/')

def CProfile():
    return render_template("cprofile.html")


if __name__ == "__main__":
    app.run(debug=True)