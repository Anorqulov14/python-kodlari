class Player:
    def __init__(self,name, health = 100,power = 90):
        self.name = name
        self.health = health
        self.power = power
    def status(self):
        print(f"{self.name} - Health: {self.health}, Power: {self.power}")

class Warrior(Player):
    def __init__(self, health=100, power=90):
        super().__init__(health, power)
        self.attack_power = 25
        self.power_cost = 30
    def attack(self,target):
        if self.power >= self.power_cost:
            target.health -= self.attack_power
            self.power -= self.power_cost
            print(f"{self.name} attacked {target.name} for {self.attack_power} damage.")
        else:
            print(f"{self.name}")
class Archer(Player):
    def __init__(self, health=100, power=90):
        super().__init__(health, power)
class Healer(Player):
    def __init__(self, health=100, power=90):
        super().__init__(health, power)



p1 = Warrior("Temur")
p2 = Archer("Ilyos")
p3 = Healer("Lola")

p1.status()
p2.status()
p3.status()

p1.attack(p2)
p2.attack(p1)
p3.heal(p1)

p1.status()
p2.status()
p3.status()
