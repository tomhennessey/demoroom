from flask import render_template, flash, redirect, send_from_directory
import os
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Tom'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/request_page')
def request_page():
    return render_template('request_page.html', title='Request Page')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html', title='About Us')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html', title='Contact Us')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon.ico', mimetype='image/vnd.microsoft.icon')
