from random import randrange

from ..models.bets import Color

def play_roulette():
    num_wins = randrange(36)
    color_wins = Color.RED.value if num_wins%2 == 0 else Color.BLACK.value
    return (num_wins,color_wins)

