import os
from flask import Flask, request, jsonify, render_template
from flaskext.mysql import MySQL


app = Flask(__name__)


mysql = MySQL()
mysql.init_app(app)

app.config['MYSQL_DATABASE_HOST'] = 'mysql.default.svc.cluster.local'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'DEMO'

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.auto_reload = True
app.jinja_env.cache = {}

@app.route('/', methods=['Get'])
def index():
    return render_template('login.html')

@app.route('/login', methods=['Get'])
def login_page():
    return render_template('login.html')


@app.route('/admin', methods=['Get'])
def admin_page():
    users = {
        'username': 'admin',
        'email': 'young@msoe.edu',
        'password': 'admin'
    }
    return render_template('admin.html', users = users)

@app.route('/signup/', methods=['POST'])
def signup():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    data = (username, email, password)
    
    print(data)
    data_json = {
        'username': username,
        'password': password,
        'email': email
    }
    
    if username and email and password and request.method == 'POST':
        print('test')
        sql = "INSERT INTO USERS(USER_NAME, USER_EMAIL, USER_PASSWORD) VALUES(%s, %s, %s)"
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            print('Data inserted successfully')
            cursor.close()
            conn.close()
            
            resp = jsonify("user added successfully")
            resp.status_code = 200
            return resp
        except Exception as e:
            return jsonify(str(e))
    else:
        return jsonify("Please provide name, email and password")
            


if __name__ == '__main__':
    extra_dirs = ['./templates', './static', './models']
    extra_files = [
        os.path.join(dirname, filename)
        for extra_dir in extra_dirs
        for dirname, _, files in os.walk(extra_dir)
        for filename in files
    ]
    app.run(host="0.0.0.0", port = 5000, extra_files=extra_files)