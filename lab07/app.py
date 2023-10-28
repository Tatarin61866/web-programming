#jpg png ограничение выдавать ошибку два поля, таблица со временем загрузки  номер надпись, темная тема
#картинка в папке статик реквест.файлс redirect 12 созвездий загрузить 6 фото,
#показать как загружаете еще 6.
#на 3 загрузка фото с полем имени и удаление 
#на 4 табличка номер, время загрузки, имя, сама фотка
#на 5 табличка с сайта
#https://flask.palletsprojects.com/en/2.3.x/patterns/fileuploads/
#https://sleepopolis.com/education/constellations-stars/ 

import os
from flask import Flask, request, redirect, flash, render_template
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = '/static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask('lab07')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/index')
def my_templates():
	return render_template('index.html')

def allowed_file(filename):
	return '.' in filename and \
		filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/download', methods=['POST'])
def upload_file():
	if request.method == 'POST':
		if 'file' not in request.files:
			flash('Не могу прочитать файл')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('Не выбран файл')
			return redirect(request.url)
			if file and allowed_file(file.filename):
				filename = secure_filename(file.filename)
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
				return redirect(url_for('download_file', name=filename))
	return render_template('index.html')			
