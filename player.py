from room import Room
from item import Item
class Player:
    
    def __init__(self, name, currentRoom: Room):
        self.name = name
        self.health = 100
        self.power = 10
        self.armor = 0
        self.inventory = {}
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
                print(f"You took: {takeItem}")
                takenItems = True
                break
        
        if takenItems == False:
            print("You found no such item")
        else:
            self.currentRoom.removeItemInRoom(self.inventory[takeItem])
    
    def displayItem(self,item):
        if item in self.inventory:
            print(f"\n\nName: {self.inventory[item].getName()}\n\nDescription: {self.inventory[item].getDescription()}")
        else:
            print(f"You do not have {item}")
    
    def displayInventory(self):
        return list(self.inventory.keys())
    
    def getCurrentRoom(self):
        return self.currentRoom
    
    def getCurrentRoomName(self):
        return self.currentRoom.getName()
    
    def getCurrentRoomDescription(self):
        return self.currentRoom.getDescription()
    
