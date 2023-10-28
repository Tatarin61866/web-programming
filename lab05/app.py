
from flask import Flask, render_template
import datetime

app = Flask('lab05')

@app.route('/clock')
def my_clock():
	s = datetime.datetime.now()
	return render_template('clock.html', cur_time=s)
