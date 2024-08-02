from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from config import Config
import base64

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        flash('User Added successfully')
        return "User Added successfully"

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_user(id):
    user = User.query.get(id)

    if request.method == 'POST':
        user.name = request.form['name']
        user.email = request.form['email']
        db.session.commit()
        flash('User Updated successfully')
        return redirect(url_for('index'))

    return render_template('edit.html', user=user)

@app.route('/delete/<id>', methods=['GET'])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    flash('User Deleted successfully')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
