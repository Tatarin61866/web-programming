
from flask import Flask, request, render_template, flash, url_for, redirect, config, abort

app = Flask('lab08')
app.config.from_object('config')

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/page1')
def page2():
	return render_template('page3.html')
	
@app.route('/page4')
def page5():
	return render_template('page6.html')
	
@app.route('/go_to_index')
def redir():
	return redirect(url_for('index'))
	
@app.route('/send_msg', methods=['POST' , 'GET'])
def send():
	if request.method == 'POST':
		m = request.form.get('txt')
		flash(m)
	return render_template('form.html')
	
#abort сделать код 403
