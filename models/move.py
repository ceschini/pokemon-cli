class Move:
    def __init__(self, name, power, accuracy, target,
                 dmg_class, type, pp, description, stat_change):
        self.name = name
        self.power = power
        self.acc = accuracy
        self.dgm_class = dmg_class
        self.type = type
        self.pp = pp
        self.description = description
        self.target = target
        self.stat_change = stat_change

    def use(self):
        if self.pp > 0:
            self.pp -= 1
            return self
        else:
            return -1
