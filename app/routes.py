from flask import render_template, flash, redirect, send_from_directory, request, flash
import os
from app import app, db
from app.forms import RequestForm, SearchForm
from app.models import Demo, DemoRequest

# only used for debug
@app.route('/base')
def base():
    return render_template('base.html', title='DEBUG_BASE')

# homepage - query SLQdb to list demos in index.html
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    demos = Demo.query.order_by(Demo.category).all() 
    form = SearchForm()
    if request.method == 'POST' and form.validate_on_submit():
        return redirect('/search', code=307)
    return render_template('index.html', title='Home', demo=demos, form=form)

@app.route('/request_page', methods=['GET', 'POST'])
def request_page():
    form = RequestForm()
    if form.validate_on_submit() and request.method == 'POST':
        demo = DemoRequest(name=request.form['name'],
            email=request.form['email'],
            demo=request.form['demo'],
            date_request=request.form['date_request'],
            comments=request.form.get('comments'))
        db.session.add(demo)
        db.session.commit()
        flash('Your demo request was successfully submitted. You should receive an email confirmation shortly. If you do not, please contact the demoroom at chemdemoroom@illinois.edu')
    return render_template('request_page.html', title='Request Page', form=form)

@app.route('/about_us')
def about_us():
    return render_template('about_us.html', title='About Us')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html', title='Contact Us')

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    query = []
    results = []
    if request.method == 'POST':
        query = request.form['name']
        results = Demo.query.filter(Demo.text.like('%' + query + '%'))
    return render_template('search.html', title='Home', form=form, query=query, results=results)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/all.css')
def all_css():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'css/all.css', mimetype='text/css')

