from flask import Flask, request, render_template
from static import bootstrap

app = Flask('lab10')

@app.route('/')
def index():
	return render_template('index.html')

	
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)
	##http://pg.spb-kit.online:50505/ там бд хранить (РОДЯ, ТАМ ВСЕГО 3 ПОЫТКИ МАТЬ ЕГО, так что не ошибайся, а то все ляжет)
	## логин student@test.lab
	## пароль stud_pass
	## создать таблицу бд в notes
	## host: pg.spb-kit.online
	## port: 54321
	## user: student
	## password studpass(stud_pass)
	## dbname: g12_haliuliln lab10
	
	## создать бд, потом схему(папку с названием лабы)
	## сделать шаблон вывода записей из бд
	## создать таблицу с именем notes
	## столбцы id serial(integer) NN default nextval('')
	## txt CHARACTER VARYTING (50) NN 
	## ts TIMESTAMP WITHOUT TIMEZONE nn default(now())
	## создать запись INSERT INTO lab10.notes (txt) values ('dwd');
	## pk-notes-id sq-notes-id
