
from flask  import  jsonify
from . import api


@api.errorhandler(500)
def app_internel_error(e):
    return  jsonify({'status': 500, 'error': 'app_internel_error',
                        'message': 'app_internel_error'}), 500


@api.errorhandler(404)
def not_found(e):

    return  jsonify({'status': 404, 'error': 'not found',
                        'message': 'invalid resource URI'}), 404
