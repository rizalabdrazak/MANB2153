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

@app.route('/aboutus/')

def about():
    return render_template("aboutus.html")

@app.route('/contact/')

def contact():
    return render_template("contact.html")

@app.route('/clients/')
def clients():
    return render_template("client.html")

@app.route('/partners/')
def partners():
    return render_template("partners.html")

@app.route('/demo/')
def demo():
    return render_template("demo.html")

if __name__ == "__main__":
    app.run(debug=True)
