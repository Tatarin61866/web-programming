

from flask import Flask, request

app = Flask('lab03')

@app.route('/hello', methods=['GET', 'POST'])
def my_form():

	

	if request.method == 'GET':
		value = request.args.get('param')
	
	
		doc = ''
		doc += '<!doctype html>'
		doc += '<html lang="en">'
		doc += '<head>'
		doc += '</head>'
		doc += '<body>'
		doc += '<h1>result with GET method</h1>'
		doc += '<hr>'
		doc += 'hello, ' + value + '!'
		doc += '</body>'
		doc += '</html>'
	
		
	
	#if request.method == 'POST':
	else:	
		value = request.form['parn']
	
		doc = ''
		doc += '<!doctype html>'
		doc += '<html lang="en">'
		doc += '<head>'
		doc += '</head>'
		doc += '<body>'
		doc += '<h1>result with POST method</h1>'
		doc += '<hr>'
		doc += 'hello, ' + value + '!'
		doc += '</body>'
		doc += '</html>'
		
	return doc
	
@app.route('/calc', methods=['GET'])
def my_calc():

	btnpl = request.form.get('pl')
	
	doc = ''
	if btnpl == 'true':
		value = request.args.get('element1')
		value2 = request.args.get('element2')
		value3 = value + value2
		
			
		doc += '<!doctype html>'
		doc += '<html lang="en">'
		doc += '<head>'
		doc += '</head>'
		doc += '<body>'
		doc += '<h1>calc plus</h1>'
		doc += '<hr>'
		doc += value + ' + ' + value2 + ' = ' + value3
		doc += '</body>'
		doc += '</html>'
		
	return doc
