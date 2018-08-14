import os


import click
from flask  import Flask, url_for ,jsonify, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, '../test.db')

app  = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SERVER_NAME'] = 'localhost'
db = SQLAlchemy(app)

@app.errorhandler(500)
def app_internel_error(e):
    return  jsonify({'status': 500, 'error': 'app_internel_error',
                        'message': 'app_internel_error'}), 500

@app.errorhandler(404)
def not_found(e):

    return  jsonify({'status': 404, 'error': 'not found',
                        'message': 'invalid resource URI'}), 404



@app.route('/users/<int:id>', methods=['GET'])
def get_users(id):
    return jsonify(User.query.get_or_404(id).export_data())

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User)

print('db create....222')
db.create_all()



@app.cli.command()
def recreate_db():
    print('recreate_db....')
    db.drop_all()
    db.create_all()
    db.session.commit()

# if __name__ == '__main__':
#     print(__name__)
#     db.create_all()

