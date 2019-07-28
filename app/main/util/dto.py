from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'nickName': fields.String(required=True, description='Wechat nick name'),
        'avatarUrl': fields.String(required=False, description='avatarUrl'),
        'city': fields.String(required=False, description='city'),
        'public_id': fields.String(description='user Identifier'),
        'country': fields.String(required=False, description='country'),
        'gender': fields.Integer(required=True, description='gender'),
        'language': fields.String(required=False, description='language'),
        'province': fields.String(required=False, description='province'),
        'child_school_id': fields.Integer(required=False, description='child_school_id'),
        'child_name': fields.String(required=False, description='child_name'),
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'nickName': fields.String(required=True, description='The Wechat nick name'),
    })