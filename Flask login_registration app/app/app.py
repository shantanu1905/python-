from flask import Flask, render_template, request, flash ,redirect ,url_for , session , logging
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
#from passlib.hash import sha256_crypt
from datetime import datetime 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    birthday = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.now)






app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'your mail id'
app.config['MAIL_PASSWORD'] = 'your mail id password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

# time stamp

now = datetime.datetime.now()
local_time = (now.strftime("%Y-%m-%d %H:%M:%S"))
print(local_time)


### PRIVATE POLICES--------------
@app.route('/policy')
def policy():
    return render_template('private policy.html')


#### LOGIN-----------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        gmail = request.form['email-address']
        passwrd = request.form['password']

        if passwrd == "12345":
            msg = Message('Services.io@Auth-Team', sender='your mail id', recipients=[gmail])
            msg.body = "Hello " + gmail + " your are recently logged in from new device " + local_time
            msg.html = render_template('email.html', gmail=gmail)
            mail.send(msg)
            return "Welcome %s" % gmail
    return render_template('login.html')
    # request.method and request.form


### REGISTRATION---------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        uname = request.form['username']
        sex = request.form['gender']
        birth = request.form['birthday']
        gmail = request.form['email-address']
        passwrd = request.form['password']
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
