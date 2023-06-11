import pokebase as pb
from random import choice


def _get_move_by_name(name):
    return pb.APIResource('move', name)


def _get_pkmn_moves(pkmn):
    pk = pb.APIResource('pokemon', pkmn)
    return pk.moves


def get_random_move_set(pkmn):
    moves = _get_pkmn_moves(pkmn)
    move_set = dict()
    for i in range(4):
        move = choice(moves)
        move_set[f'move{i}'] = {
            'name': move.move.name,
            'power': move.move.power,
            'acc': move.move.accuracy,
            'dmg_class': move.move.damage_class.name,
            'pp': move.move.pp,
            'type': move.move.type.name,
            'description': move.move.flavor_text_entries[0].flavor_text,
            'target': move.move.target.name,
            'stat_change': move.move.stat_changes
        }
    return move_set
