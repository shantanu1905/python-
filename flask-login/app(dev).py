from flask import Flask, render_template, request, flash ,redirect ,url_for , session , logging
import sqlite3
con=sqlite3.connect('users.db',check_same_thread=False)
cursor=con.cursor()


app = Flask(__name__)
app.config['SECRET_KEY']= 'Sm9obiBTY2hyb20ga2lja3MgYXNz'


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ""
    if(request.method == 'POST'):
        username=request.form["username"]
        #email=request.form["email"]
        password=request.form["password"]
        cursor.execute("SELECT * FROM users WHERE username ='"+username+"' and password = '"+password+"'" )
        r = cursor.fetchall()
        for i in r:
            if(username == i[1] and password == i[3]):
                session["logedin"]= True
                session["username"]= username
                return redirect(url_for("profile"))
            else:
                msg="please enter valid crediential"
    return render_template("login.html" , msg=msg)


@app.route('/register', methods=['GET','POST'])
def register():
    msg = None
    if(request.method == 'POST'):
        if(request.form["username"]!="" and request.form["password"]!= "" and request.form["email"]!= ""):
            global username
            username = request.form['username']
            email= request.form['email']
            password= request.form['password']
            cursor.execute("INSERT INTO users (username,email,password) VALUES (?,?,?)",(username,email,password) )
            #cursor.execute("INSERT INTO users VALUES('"+username+"','"+email+"', '"+password+"')" )
            msg="Account has created Successfully !!"
            con.commit()
            #con.close()
        else:
            msg =" Some thing went wrong "
    return render_template("register.html", msg=msg)

@app.route('/logout') 
def logout(): 
    session.clear() 
    return redirect(url_for('login')) 

@app.route('/profile')
def profile():
    user=username
    return render_template("profile.html",user=username)


if __name__ == '__main__':
    app.run(debug=True)