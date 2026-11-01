from room import Room
class Player:
    
    def __init__(self, name, currentRoom: Room):
        self.name = name
        self.health = 100
        self.power = 10
        if self.name == "y" or self.name == "":
            self.name = "William"
        self.currentRoom = currentRoom
        

    def takeDamage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
    
    def move(self, direction):
        if self.currentRoom.getExit(direction.lower()) != None:
            self.currentRoom = self.currentRoom.getExit(direction.lower())
        else:
            print("\nThere is no room there")
    
    def getCurrentRoom(self):
        return self.currentRoom
    
    def getCurrentRoomName(self):
        return self.currentRoom.getName()
    
    def getCurrentRoomDescription(self):
        return self.currentRoom.getDescription()
    
    def getCurrentRoomExits(self):
        return self.currentRoom.getAllExits()
    
