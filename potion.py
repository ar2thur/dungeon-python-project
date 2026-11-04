from item import Item

class Potion(Item):
    def __init__(self, name, description, rarity, healingPower):
        super().__init__(name, description, rarity)
        self.healingPower = healingPower
        
    def getHealingPower(self):
        return self.healingPower