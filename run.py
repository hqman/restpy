from orders import create_app ,db

from orders.models.user import User

app = create_app('development')


@app.cli.command()
def recreate_db():
    print('recreate_db....')
    db.drop_all()
    db.create_all()
    db.session.commit()

@app.cli.command()
def seed_db():
    admin = User(username='admin' , email = 'hqmank@gmail.com')
    admin.set_password('wangkai')
    db.session.add(admin)
    db.session.commit()

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User)


# if __name__ == '__main__':
#     app = create_app('development')
#     with app.app_context():
#         print('init ....db')
#     app.run()
#     print('app run...')