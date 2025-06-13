class Player:
    def __init__(self, health = 100,power = 90):
        self.health = health
        self.power = power

class Warrior(Player):
    def __init__(self, health=100, power=90):
        super().__init__(health, power)
    def attack(self):
        pass
class Archer(Player):
    pass
class Healer(Player):
    pass