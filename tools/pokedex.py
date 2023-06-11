import pandas as pd
import random


class Pokedex:

    def __init__(self, filename):
        self.pokemons = pd.read_csv(filename)
        self.pokemons.drop(columns=['ID'], inplace=True)

    def get_pkmn_by_name(self, name):
        return self.pokemons[self.pokemons['Name'] == name]

    def get_pkmn_by_id(self, id):
        return self.pokemons.iloc[[id]]

    def get_rnd_initial(self):
        idx = random.randrange(2)
        return self.get_pkmn_by_id(idx)

    def get_rnd_pkmn(self):
        idx = random.randrange(721)
        pkmn = self.get_pkmn_by_id(idx)
        return pkmn

    def df_to_list(self, df):
        types = list()
        types.append(df['Type 1'].to_numpy()[0])
        if df['Type 2'].bool:
            pass
        else:
            types.append(df['Type 2'].to_numpy()[0])
        lst = [
            df['Name'].to_numpy()[0],
            types,
            df['HP'].to_numpy()[0],
            df['Attack'].to_numpy()[0],
            df['Defense'].to_numpy()[0],
            df['Sp. Atk'].to_numpy()[0],
            df['Sp. Def'].to_numpy()[0],
            df['Speed'].to_numpy()[0]
        ]
        return lst
