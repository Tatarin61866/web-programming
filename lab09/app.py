
from flask import Flask, request, render_template, url_for

app = Flask('lab09')

@app.route('/')
def index():
	return render_template('base.html')
	
@app.route('/p1')
def page1():
	return render_template('page1.html')

@app.route('/p2')
def page2():
	return render_template('page2.html')
	
	
@app.route('/p3')
def page3():
	return render_template('page3.html')
