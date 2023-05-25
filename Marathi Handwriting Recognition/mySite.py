# import the necessary packages
from flask import Flask, render_template, redirect, url_for, request,session,Response
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense, Dropout
from keras import optimizers
from supportFile import predictor
import cv2
import os
from werkzeug import secure_filename
import time
import pyttsx3

app = Flask(__name__)

app.secret_key = '1234'
app.config["CACHE_TYPE"] = "null"

@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid Credentials. Please try again.'
		else:
			return redirect(url_for('testing'))
	return render_template('login.html', error=error)
	



@app.route('/testing',methods=['GET', 'POST'])
def testing():

	if request.method == 'POST':
		savepath = r'upload/'
		photo = request.files['photo']
		#image = cv2.imread("test_images/"+ photo.filename)
		photo.save(os.path.join(savepath,(secure_filename(photo.filename))))
		
		image = cv2.imread(os.path.join(savepath,secure_filename(photo.filename)))
		original = image.copy()
		output = image.copy()

		preds = predictor(os.path.join(savepath, secure_filename(photo.filename)))
		
		#color = (0, 255, 0) if preds == 0 else (0, 0, 255)
		'''
		cv2.putText(output, preds, (3, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
			(0, 0, 255), 2)
		'''
		#output=cv2.resize(output,(370,300))
		#original=cv2.resize(original,(370,300))
		cv2.imwrite(os.path.join("static/images/","original.jpg"),original)
		cv2.imwrite(os.path.join("static/images/","output.jpg"),output)
		if(preds):
			engine = pyttsx3.init()
			engine.say(preds)
			engine.runAndWait()			

		return render_template('testing.html',txt = preds)

	return render_template('testing.html')
	


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, threaded=True)
