from flask import Flask, request, render_template, redirect, url_for
from static import bootstrap
import psycopg2

app = Flask('lab10')

con = psycopg2.connect('host=pg.spb-kit.online port=54321 user=g12_haliullin password=password dbname=g12_haliullin')

@app.route('/list')
def list_notes():
	cur = con.cursor()
	cur.execute("SELECT id, title, txt, color, to_char(ts, 'DD Mon YYYY HH24:MI') FROM lab10.notes;")
	arr = cur.fetchall()
	cur.close()
	return render_template('list.html', items=arr) 
	
@app.route('/add', methods=['POST'])
def add_note():
	ti = request.form.get("title")
	t = request.form.get("content")
	c = request.form.get('color')
	cur = con.cursor()
	cur.execute("INSERT INTO lab10.notes (title, txt, color) VALUES (%s, %s, %s);",[ti,t,c])
	cur.close()
	con.commit()
	return redirect(url_for('list_notes'))

	

	
#if __name__ == "__main__":
#	app.run(host='0.0.0.0', port=5000, debug=True)

	#http://pg.spb-kit.online:50505/ там бд хранить (РОДЯ, ТАМ ВСЕГО 3 ПОЫТКИ МАТЬ ЕГО, так что не ошибайся, а то все ляжет)
	# логин student@test.lab
	# пароль stud_pass
	# создать таблицу бд в notes
	# host: pg.spb-kit.online
	# port: 54321
	# user: student
	# password studpass(stud_pass)
	# dbname: g12_haliuliln lab10
	
	# создать бд, потом схему(папку с названием лабы)
	# сделать шаблон вывода записей из бд
	# создать таблицу с именем notes
	# столбцы id serial(integer) NN default nextval('')
	# txt CHARACTER VARYTING (50) NN 
	# ts TIMESTAMP WITHOUT TIMEZONE nn default(now())
	# создать запись INSERT INTO lab10.notes (txt) values ('dwd');
	# pk-notes-id sq-notes-id
	# Добваить цвет к заметкам
	# добавить название к заметкам жирным
	# все в квадратиках
