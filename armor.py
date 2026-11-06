from item import Item

class Armor(Item):
    def __init__(self, name, description, rarity, armorPower):
        super().__init__(name, description, rarity)
        self.armorPower = armorPower
        self.isEquipped = False
    
    def getArmorPower(self):
        return self.armorPower
    
    def getIsEquipped(self):
        return self.isEquipped