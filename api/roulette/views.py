from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required

from ..models.roulettes import Roulette, RouletteStatus

from http import HTTPStatus

roulette_namespace = Namespace('Roulettes', description="a namespace for Roulettes")

roulette_model = roulette_namespace.model(
        'Roulette',{
            'id':fields.Integer()
    }
)

patch_model = roulette_namespace.model(
        'Roulette_Patch',{
            'id':fields.Integer(),
            'message': fields.String()
    }
)


@roulette_namespace.route('/Roulette')
class RouletteCreate(Resource):
    @roulette_namespace.marshal_with(roulette_model)
    @jwt_required()
    def post(self):
        """
            Create a roulette
        """
        new_roulette = Roulette()
        new_roulette.save()
        return {'id':new_roulette.id},HTTPStatus.CREATED

@roulette_namespace.route('/Roulette/open/<int:roulette_id>')
class RouletteOpen(Resource):
    @roulette_namespace.marshal_with(patch_model)
    @jwt_required()
    def patch(self,roulette_id):
        """
            Open a roulette
        """
        roulette = Roulette.query.get(roulette_id)
        
        if not roulette:
            roulette_namespace.abort(404, f'roulette {roulette_id} not found')
        
        roulette.is_active = RouletteStatus.OPEN
        roulette.save()
        
        return {'id': roulette.id,'message': 'ROULETTE IS OPEN '}, HTTPStatus.OK

@roulette_namespace.route('/Roulette/close/<int:roulette_id>')
class RouletteClose(Resource):
    def patch(self,roulette_id):
        pass