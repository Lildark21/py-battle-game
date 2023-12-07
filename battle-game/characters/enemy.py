class Orc:
    def __init__(self, name, health=380, attack_power=25):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")

    def is_alive(self):
        return self.health > 0
