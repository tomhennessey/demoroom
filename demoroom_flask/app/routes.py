from flask import render_template, flash, redirect, send_from_directory
import os
from app import app
from app.forms import RequestForm
from app.models import Demo

# only used for debug
@app.route('/base')
def base():
    return render_template('base.html', title='DEBUG_BASE')

# homepage - query SLQdb to list demos in index.html
@app.route('/')
@app.route('/index')
def index():
    demos = Demo.query.order_by(Demo.category).all() 
    return render_template('index.html', title='Home', demo=demos)

@app.route('/request_page', methods=['GET', 'POST'])
def request_page():
    form = RequestForm()
    if form.validate_on_submit():
        return redirect('/index')
    return render_template('request_page.html', title='Request Page', form=form)

@app.route('/about_us')
def about_us():
    return render_template('about_us.html', title='About Us')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html', title='Contact Us')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/all.css')
def all_css():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'css/all.css', mimetype='text/css')

