from room import Room
from item import Item
from weapon import Weapon
from potion import Potion
from armor import Armor
class Player:
    
    def __init__(self, name, currentRoom: Room):
        self.name = name
        self.health = 100
        self.power = 10
        self.armor = 0
        self.inventory = {}
        self.countedInventory = {}
        self.equippedItems = {}
        if self.name == "y" or self.name == "":
            self.name = "William"
        self.currentRoom = currentRoom


    def takeDamage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
    
    def move(self, direction):
        
        exit = self.currentRoom.getExit(direction.lower())
        
        if exit is not None:
            self.currentRoom = exit
        else:
            print("\nThere is no room there")
    
    def takeItem(self, takeItem):
        items = self.currentRoom.getItems()
        takenItems = False
        
        for item in items:
            if takeItem == item.getName():
                self.inventory[takeItem] = item
                if self.countedInventory.get(takeItem) is not None:
                    self.countedInventory[takeItem] += 1
                else:
                    self.countedInventory[takeItem] = 1
                print(f"You took: {takeItem}")
                takenItems = True

                break
        
        if takenItems == True:
            self.currentRoom.removeItemInRoom(self.inventory[takeItem])
        else:
            print(f"\nYou found no such item.")
    
    def displayItem(self,item):
        if item in self.inventory:
            print(f"\n\nName: {self.inventory[item].getName()}\n\nDescription: {self.inventory[item].getDescription()}")
        else:
            print(f"You do not have {item}")
    
    def displayInventory(self):
        inventoryD = []
        for item in self.countedInventory:
            count = self.countedInventory[item]
            if count > 1:
                formatted_string = f"{item} * {count}"
                inventoryD.append(formatted_string)
            if count == 1:
                inventoryD.append(f"{item}")
        
        return inventoryD
    
    def equip(self,item):
        if item in self.inventory:
            object = self.inventory[item]
            if type(object) is Armor:
                self.armor += object.getArmorPower()
                object.isEquipped = True
                self.inventory.pop(item)
                self.equippedItems[item] = object
            elif type(object) is Weapon:
                self.power += object.getAttackPower()
                object.isEquipped = True
                self.inventory.pop(item)
                self.equippedItems[item] = object
            elif type(object) is Potion:
                self.health += object.getHealingPower()
                if self.health > 100:
                    self.health = 100
                self.inventory.pop(item)
            else:
                print(f"You are unable to equip '{item}'.")
    
    def unEquip(self, item):
        if item in self.equippedItems:
            object = self.equippedItems[item]
            object.isEquipped = False
            self.inventory[item] = object
            self.equippedItems.pop(item)
        else:
            print("You do not have that item equipped.")
    
    def getPlayerStats(self):
        equippedItems = list(self.equippedItems.keys())
        return f"Name: {self.name}\nHealth: {self.health}\nArmor: {self.armor}\nAttack Power: {self.power}\nEquipped Items: {equippedItems}\n"
    
    def getCurrentRoom(self):
        return self.currentRoom
    
    def getCurrentRoomName(self):
        return self.currentRoom.getName()
    
    def getCurrentRoomDescription(self):
        return self.currentRoom.getDescription()
    
