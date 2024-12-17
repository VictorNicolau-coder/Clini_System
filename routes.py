from flask import render_template, request
import sqlite3

from main import app

@app.route('/')
def home():
    return "Receba"