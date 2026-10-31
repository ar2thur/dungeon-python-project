class Player:
    
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.power = 10

    def takeDamage(self, damage):
        self.health -= damage
    