from tools.pokedex import Pokedex
from tools.movedex import get_random_move_set
from models.pokemon import Pokemon

dex = Pokedex('./data/Pokemon.csv')

pokemon = dex.get_rnd_pkmn()
pokemon = dex.df_to_list(pokemon)
pokemon.append(get_random_move_set(pokemon[0].lower()))
pokemon = Pokemon(*pokemon)
print(pokemon.name)
print(pokemon.getMoves())
