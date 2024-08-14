from flask import Flask , render_template , request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/madhav_web'
db = SQLAlchemy(app)

# class Say():
#     sno = db.Column(db.Integer , primarykey = True)
#     name = db.Column(db.String(80) , nullable = False)
#     message = db.Column(db.String(150) , nullable = True)
class Loginform(db.Model):
    sno = db.Column(db.Integer , primary_key = True)
    firstname = db.Column(db.String(80) , nullable = False)
    lastname = db.Column(db.String(80))
    email = db.Column(db.String(80) , nullable = False)
    phone = db.Column(db.Integer(), nullable = False)
    message = db.Column(db.String(500), nullable = False)


@app.route("/" , methods = ['POST' , 'GET'])
def loginform():
    if (request.method == 'POST'):
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        entry =  Loginform(firstname=firstname , lastname= lastname , email=email,phone=phone,message=message)
        db.session.add(entry)
        db.session.commit()

    return render_template("index.html")

# @app.route("/submit")
# def submit():
#     return render_template("submit.html")


if __name__ == "__main__":
    app.run()(debug = True)

