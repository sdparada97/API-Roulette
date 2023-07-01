from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required

from .utils import play_roulette
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

result_bet = roulette_namespace.model(
    'Result_bet',{
        'id': fields.Integer(),
        "color": fields.String(),
        'number': fields.Integer(),
        "is_wins": fields.Boolean(),
        "bet_amount": fields.Arbitrary()
    }
)

roulette_response_close = roulette_namespace.model(
    'Roulette_response_close',{
        'id': fields.Integer(),
        'number_wins': fields.Integer(),
        'color_wins': fields.String(),
        'total_bet': fields.Arbitrary(),
        'bets_result':fields.List(fields.Nested(result_bet))
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
    @roulette_namespace.marshal_with(roulette_response_close)
    def patch(self,roulette_id):
        """
            Close a roulette
        """
        # Cerrar ruleta
        roulette = Roulette.query.filter_by(id=roulette_id).first()
        
        if not roulette:
            roulette_namespace.abort(404, f'roulette {roulette_id} not found')
        
        roulette.is_active = RouletteStatus.CLOSE
        
        # Calcular el numero y color ganador
        number_wins,color_wins = play_roulette()
        
        # Calcular Monto apostado
        roulette.total_bet = roulette.get_total_bets()
        
        # Calcular resultados de las apuestas
        bets_result = roulette.get_roulette_result(number_wins,color_wins)
        roulette.save()
        return {
            'id': roulette.id,
            'number_wins': number_wins,
            'color_wins': color_wins,
            'total_bet': roulette.total_bet,
            'bets_result':bets_result
        },HTTPStatus.OK