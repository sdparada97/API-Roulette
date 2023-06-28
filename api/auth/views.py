from flask_restx import Namespace, Resource

auth_namespace = Namespace('Auth', description="a namespace for Authentication")

@auth_namespace.route('/signup')
class Signup(Resource):
    
    def post(self):
        pass

@auth_namespace.route('/login')
class Signup(Resource):
    
    def post(self):
        pass