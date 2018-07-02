

"""from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from models import db

#create an application window object
app = Flask(__name__)

#initialize an app db
db = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'roopa'
app.config['MYSQL_DATABASE_PASSWORD'] = 'sathROO@315'
app.config['MYSQL_DATABASE_DB'] = 'dbtest1'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
db.init_app(app)
"""
"""import os
from flask import Flask, request, redirect, url_for,send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/roopa/others/RVS/internals/FlaskApp/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
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
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

#@app.route('/')
#def index():
#    return render_template('index1.html')


@app.route('/create_table', methods=['POST'])
def create_table():
    if request.method=="POST":
        try:
            table_name = request.form.get('table_name')
            field_name_list = request.form.getlist('fields[]')
            field_list = []
            for field in field_name_list:
                field_list.append(field+ " VARCHAR(50) DEFAULT NULL")
            field_query = " ( " + ", ".join(field_list) + " ) "
            create_table_query = 'CREATE TABLE `'+table_name+'`' + field_query
            conn = db.connect()
            cursor = conn.cursor()
            cursor.execute(create_table_query)
            return "Table: "+table_name+" created successfully"
        except Exception as e:
            return str(e)

#defining the route of the webpage
#@app.route("/")
#def main():
#	return render_template('index.html')


#run the application in debug  mode here
if __name__ == "__main__":
	app.config['DEBUG'] = True
	app.run()"""



from flask import Flask, request, jsonify
import pandas as pd

app=Flask(__name__)

@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print(request.files['file'])
        f = request.files['file']
        data_xls = pd.read_excel(f)
        return data_xls.to_html()
    return '''
    <!doctype html>
    <title>Upload an excel file</title>
    <h1>Excel file upload (csv, tsv, csvz, tsvz only)</h1>
    <form action="" method=post enctype=multipart/form-data>
    <p><input type=file name=file><input type=submit value=Upload>
    </form>
    '''

@app.route("/export", methods=['GET'])
def export_records():
    return

if __name__ == "__main__":
    app.run()