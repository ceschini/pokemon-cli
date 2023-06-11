class Pokemon:
    status = 'OK'

    def __init__(self, name, types, hp, attack,
                 defense, sp_atk, sp_def, speed, move_set):
        self.name = name
        self.types = types
        self.hp = hp
        self.attribs = {
            'atk': attack,
            'def': defense,
            'sp_atk': sp_atk,
            'sp_def': sp_def,
            'speed': speed,
        }
        self.move_set = move_set

    def buff(self, attrib, value):
        self.attribs[attrib] += value

    def heal(self, value):
        self.hp += value

    def hit(self, value):
        self.hp -= value

    def checkStatus(self, hp, status):
        if hp < 0:
            return 'Fainted'

    def getMoves(self):
        move_names = list()
        for move in self.move_set:
            move_names.append(move.name)
        return move_names
