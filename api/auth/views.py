from flask_restx import Namespace, Resource, fields
from flask import request
from flask_jwt_extended import (create_access_token,
                                create_refresh_token,
                                jwt_required,
                                get_jwt_identity)

from ..models.users import User

from werkzeug.security import generate_password_hash,check_password_hash
from http import HTTPStatus

auth_namespace = Namespace('Auth', description="a namespace for Authentication")

signup_model = auth_namespace.model(
    'SignUp',{
        'email': fields.String(required=True, descripcion='an email'),
        'password': fields.String(required=True, descripcion='a password'),
        'available_credit': fields.Arbitrary()
    }
)

user_model = auth_namespace.model(
    'User',{
        'id':fields.Integer()
    }
)

login_model = auth_namespace.model(
    'Login',{
        'email': fields.String(required=True, descripcion='an email'),
        'password': fields.String(required=True, descripcion='a password')
    }
)

@auth_namespace.route('/signup')
class Signup(Resource):
    
    @auth_namespace.expect(signup_model)
    @auth_namespace.marshal_with(user_model)
    def post(self):
        """
            Create a new user
        """
        data = request.get_json()
        
        new_user = User(
            email = data.get('email'),
            password_hash = generate_password_hash(data.get('password')),
            available_credit = data.get('available_credit')
        )
        
        new_user.save()
        
        return new_user, HTTPStatus.CREATED


@auth_namespace.route('/login')
class Login(Resource):
    
    @auth_namespace.expect(login_model)
    def post(self):
        """
            Generate a JWT Authentication 
        """
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
        user = User.query.filter_by(email=email).first()
        if (user is not None) and check_password_hash(user.password_hash,password):
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)
            
            response = {
                'access_token':access_token,
                'refresh_token':refresh_token
            }
            
            return response, HTTPStatus.OK

@auth_namespace.route('/refresh')
class Refresh(Resource):
    
    @jwt_required(refresh=True)
    def post(self):
        id = get_jwt_identity()
        access_token = create_access_token(identity=id)
        return {'access_token':access_token},HTTPStatus.OK