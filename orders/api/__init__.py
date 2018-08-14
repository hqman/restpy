
from functools import wraps
from flask import Blueprint, jsonify,request, Response

from orders.models.user import User

from orders.auth import requires_auth


api = Blueprint('api', __name__)


@api.route('/users/<int:id>', methods=['GET'])
@requires_auth
def get_users(id):
    print('get user ....')
    return jsonify(User.query.get_or_404(id).export_data())

from . import errors