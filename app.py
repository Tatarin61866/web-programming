
from flask import Flask
import psycopg2

app = Flask('api')

con = psycopg2.connect('host=pg.spb-kit.online port=54321 user=g12_haliullin password=12345678 dbname=g12_haliullin')

@app.route('/list', methods=['GET', 'PUT', 'POST', 'DELETE'])
def list():
	txt = ''

	if reqiest.method == 'GET':
		cur = con.cursor()
		res = cur.execute('SELECT id, done, title, ts FROM lab13.tasks;')
		arr = res.fetchall()
		cur.close()
		print(arr)

	if reqiest.method == 'PUT':
		pass
	if reqiest.method == 'POST':
		pass
	if reqiest.method == 'DELETE':
		pass
	return txt
