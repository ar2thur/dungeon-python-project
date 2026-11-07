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
        
        self.helmet = False
        self.chestplate = False
        self.leggings = False
        self.boots = False
        self.shield = False
        self.accesory = []
        


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
    
    def takeItems(self, takeItem, count: int = 1):
        items = self.currentRoom.getItems()
        takenItems = False
        
        for i in range(count):
            for item in items:
                if takeItem == item.getName():
                    self.inventory[takeItem] = item
                    if self.countedInventory.get(takeItem) is not None:
                        self.countedInventory[takeItem] += 1
                    else:
                        self.countedInventory[takeItem] = 1
                    self.currentRoom.removeItemInRoom(self.inventory[takeItem]) #remove room item
                    takenItems = True
                    break
            
        if takenItems == True:
            print(f"You took {count} {takeItem}s")
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
                canEquip = False
                
                if object.getArmorType().lower() == "helmet" and self.helmet == False:
                    self.helmet = True
                    canEquip = True
                elif object.getArmorType().lower() == "chestplate" and self.chestplate == False:
                    self.chestplate = True
                    canEquip = True
                elif object.getArmorType().lower() == "leggings" and self.leggings == False:
                    self.leggings = True
                    canEquip = True
                elif object.getArmorType().lower() == "boots" and self.boots == False:
                    self.boots = True
                    canEquip = True
                elif object.getArmorType().lower() == "accesory":
                    if len(self.accesory) < 3:
                        self.accesory.append(True)
                        canEquip = True
                elif object.getArmorType().lower() == "shield"and self.shield == False:
                    self.shield = True
                    canEquip = True
                else:
                    print("You have too many of this item equipped.")
                    
                if canEquip == True:
                    self.armor += object.getArmorPower()
                    object.isEquipped = True
                    self.removeItem(item)
                    self.equippedItems[item] = object
                
            elif type(object) is Weapon:
                self.power += object.getAttackPower()
                object.isEquipped = True
                self.removeItem(item)
                self.equippedItems[item] = object
            elif type(object) is Potion:
                self.health += object.getHealingPower()
                if self.health > 100:
                    self.health = 100
                self.removeItem(item)
            else:
                print(f"You are unable to equip '{item}'.")
    
    def unEquip(self, item):
        if item in self.equippedItems:
            object = self.equippedItems[item]
            object.isEquipped = False
            self.addItem(item, object)
            self.equippedItems.pop(item)
            if type(object) is Weapon:
                self.power -= object.getAttackPower()
            if type(object) is Armor:
                self.armor -= object.getArmorPower()
                
                if object.getArmorType().lower() == "helmet":
                    self.helmet = False
                elif object.getArmorType().lower() == "chestplate":
                    self.chestplate = False
                elif object.getArmorType().lower() == "leggings":
                    self.leggings = False
                elif object.getArmorType().lower() == "boots":
                    self.boots = False
                elif object.getArmorType().lower() == "accesory":
                    self.accesory.remove(True)
                elif object.getArmorType().lower() == "shield":
                    self.shield = False

        else:
            print("You do not have that item equipped.")
    
    def getPlayerStats(self):
        equippedItems = list(self.equippedItems.keys())
        return f"Name: {self.name}\nHealth: {self.health}\nArmor: {self.armor}\nAttack Power: {self.power}\nEquipped Items: {equippedItems}\nInventory: {self.displayInventory()}"
    
    def removeItem(self, item):
        self.inventory.pop(item)
        if self.countedInventory.get(item,0) > 1:
            self.countedInventory[item] -= 1
        else:
            self.countedInventory.pop(item)
        
    def addItem(self, itemName, itemObject):
        self.inventory[itemName] = itemObject
        if self.countedInventory.get(itemName,0) > 1:
            self.countedInventory[itemName] += 1
        else:
            self.countedInventory[itemName] = 1
    
    def getCurrentRoom(self):
        return self.currentRoom
    
    def getCurrentRoomName(self):
        return self.currentRoom.getName()
    
    def getCurrentRoomDescription(self):
        return self.currentRoom.getDescription()
    
