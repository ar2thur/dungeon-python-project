from item import Item

class Armor(Item):
    def __init__(self, name, description, rarity, armorPower, armorType):
        super().__init__(name, description, rarity)
        self.armorPower = armorPower
        self.isEquipped = False
        self.armorType = armorType
    
    def getArmorPower(self):
        return self.armorPower
    
    def getIsEquipped(self):
        return self.isEquipped
    
    def getArmorType(self):
        return self.armorType