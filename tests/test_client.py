from base64 import b64encode
import json

import unittest
from werkzeug.exceptions import NotFound
from orders import create_app, db
from orders.models import User



class TestAPI(unittest.TestCase):
    default_username = 'admin'
    default_password = 'wangkai'

    def setUp(self):
        self.app = create_app('testing')
        self.ctx = self.app.app_context()
        self.ctx.push()


    def tearDown(self):
        self.ctx.pop()
