from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restx import Namespace, Resource, fields

from ..models.bets import Bet, TypeBet, Color
from ..models.roulettes import Roulette
from ..models.users import User

from http import HTTPStatus

bet_namespace = Namespace('Bets', description="a namespace for Bets")

bet_expect_model = bet_namespace.model(
    'bet_expect',{
        'id_roulette': fields.Integer(required=True),
        'bet_amount': fields.Arbitrary(required=True),
        'type_bet': fields.String(enum=['NUMERIC','COLOR'], required=True),
        'color_bet': fields.String(enum=['ROJO','NEGRO']),
        'number_bet': fields.Integer()
    }
)

bet_response_model = bet_namespace.model(
    'bet_response',{
        'id': fields.Integer(),
        'message': fields.String()
    }
)

@bet_namespace.route('/bet')
class BetCreate(Resource):
    @bet_namespace.expect(bet_expect_model)
    @bet_namespace.marshal_with(bet_response_model)
    @jwt_required()
    def post(self):
        """
            Create a Bet
        """
        user_id = get_jwt_identity()
        user = User.query.filter_by(id=user_id).first()
        
        data = bet_namespace.payload
        roulette_id = data.get("id_roulette")
        roulette = Roulette.query.filter_by(id=roulette_id).first()
        
        bet_amount = data.get("bet_amount")
        type_bet = TypeBet.COLOR if data.get("type_bet") == TypeBet.COLOR.value else TypeBet.NUMBER
        color_bet = Color.RED if data.get("color_bet") == Color.RED.value else Color.BLACK
        
        new_bet = Bet(
            roulette=roulette,
            user=user,
            type_bet=type_bet,
            color_bet=color_bet,
            number_bet=data.get("number_bet"),
            bet_amount=bet_amount
        )
        
        new_bet.save()
        
        return {'id':new_bet.id,'message':'Create bet succesfull'}
