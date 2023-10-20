
from flask import Flask, request, render_template

app = Flask('lab03')

@app.route('/')
def my_index():
    return render_template('index.html')

@app.route('/hello', methods=['GET', 'POST'])
def my_form():
    
    doc = ''   
    if request.method == 'GET':

        value = request.args.get('param')
        
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
        return doc
    
    else:
        value1 = request.form.get('par')
      #  doc = ''
        doc += '<!doctype html>'
        doc += '<html lang="en">'
        doc += '<head>'
        doc += '</head>'
        doc += '<body>'
        doc += '<h1>result with GET method</h1>'
        doc += '<hr>'
        doc += 'hello, ' + value1 + '!'
        doc += '</body>'
        doc += '</html>'
        return doc
    
@app.route('/calc', methods=['GET', 'POST'])
def my_calc():
 
    doc = ''
    doc += '<!doctype html>'
    doc += '<html lang="en">'
    doc += '<head>'
    doc += '</head>'
    doc += '<body>'
    doc += '<h1>result</h1>'
    doc += '<hr>'
    if request.method == 'GET':
        if request.args.get('pl'):
            value = int(request.args.get('val'))
            value1 = int(request.args.get('val1'))
            value3 = value + value1
            doc +=  str(value) + ' + ' + str(value1) + ' = ' + str(value3)
        
        elif request.args.get('sb'):
            value = int(request.args.get('val'))
            value1 = int(request.args.get('val1'))
            value3 = value - value1
            doc +=  str(value) + ' - ' + str(value1) + ' = ' + str(value3)

        elif request.args.get('ml'):
            value = int(request.args.get('val'))
            value1 = int(request.args.get('val1'))
            value3 = value * value1
            doc +=  str(value) + ' * ' + str(value1) + ' = ' + str(value3)

        elif request.args.get('dv'):
            value = int(request.args.get('val'))
            value1 = int(request.args.get('val1'))
            value3 = value / value1
            doc +=  str(value) + ' / ' + str(value1) + ' = ' + str(value3)

       ## return 'Error method'
    doc += '</body>'
    doc += '</html>'
    return doc
 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)