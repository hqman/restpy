from base64 import b64encode
import json

import unittest
from werkzeug.exceptions import NotFound
from orders import create_app, db
from orders.models import User



# class TestAPI(unittest.TestCase):
#     default_username = 'admin'
#     default_password = 'wangkai'

#     def setUp(self):
#         self.app = create_app('testing')
#         self.ctx = self.app.app_context()
#         self.ctx.push()


#     def tearDown(self):
#         self.ctx.pop()


import pytest

# entire model calls this only once.
@pytest.fixture(scope='module')
def app(request): # depends on "request" (dependency injection)
    from orders import create_app, db
    app = create_app('testing')
    ctx = app.app_context()
    ctx.push()
    db.drop_all()
    db.create_all()
    db.session.commit()
    # request.addfinalizer(ctx.pop)
    yield app
    db.session.remove()
    db.drop_all()
    ctx.pop()



def test_app_name(app): # inject app fixture here.
    print(app.name)
    assert app.name == 'orders'



def test_app_user(app):
    admin = User(username='admin' , email = 'hqmank@gmail.com')
    admin.set_password('wangkai')
    db.session.add(admin)
    db.session.commit()

    print(admin)
    assert admin.id == 1

    u = User.query.filter_by(username='admin')
    assert u != None








