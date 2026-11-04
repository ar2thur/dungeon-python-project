from item import Item

class Weapon(Item):
    def __init__(self, name, description, rarity, attackPower):
        super().__init__(name, description, rarity)
        self.attackPower = attackPower
        
    def getAttackPower(self):
        return self.attackPower