from flask  import Flask, url_for ,jsonify, request

from werkzeug.security import generate_password_hash, check_password_hash
from orders import db

class User(db.Model):
    """docstring for Customer"""
    __tablename__ = 'usres'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))


    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_url(self):
        return url_for('api.get_users' , id=self.id , _external=True)

    def export_data(self):
        return {
            'self_url': self.get_url(),
            'username': self.username
        }


class Customer(db.Model):
    """docstring for Customer"""
    __tablename__ = 'customers'
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(64) , index= True)