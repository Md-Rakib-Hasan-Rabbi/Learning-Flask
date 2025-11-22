import os
import uuid
import pandas as pd
from flask import Flask, request, render_template, Response, send_from_directory


app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form.get('Username')
        password = request.form.get('password')


        if username == 'user' and password == '1234':
          return "Success"
        else:
          return "Failure"

@app.route('/upload_file',methods=['POST'])
def upload_file():
    file = request.files['file']


    if file.content_type == 'text/plain':
        return file.read().decode()
    elif file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file.content_type == 'application/vnd.ms-excel':
        return "Excel file uploaded" 
    






if __name__ == '__main__':
    app.run(host='0.0.0.0' , port = 5560 , debug=True)