
from flask import Flask, send_from_directory
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin

import os


UPLOAD_FOLDER = 'upload' + os.sep
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__, static_folder="dist")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'hard to guess string'
cors = CORS(app, resources={r"/rest/*": {"origins": "*"}})

front_end_folder = 'dist'
host = 'localhost'
port = '5000'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/rest/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('/')
    return redirect('/')


@app.route('/')
def root():
    url_link = {'link': 'http://'+str(host)+':'+str(port)+'/'+front_end_folder+'/'}
    return redirect(url_link['link'], code=302)


@app.route("/"+ front_end_folder +"/")
def index_page():
    return app.send_static_file('index.html')


@app.route('/<path:path>')
def static_file_all(path):
    print('path ', path)
    return redirect('/'+ front_end_folder + '/' +path)


@app.route('/'+ front_end_folder + '/<path:path>')
def static_file(path):
    return app.send_static_file(path)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

if __name__ == "__main__":
    app.run(host=host, port=port)
