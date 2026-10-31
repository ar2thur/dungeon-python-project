from room import Room
class Player:
    
    def __init__(self, name, currentRoom: Room):
        self.name = name
        self.health = 100
        self.power = 10
        if self.name == "y" or self.name == "":
            self.name == "William"
        self.currentRoom = currentRoom
        

    def takeDamage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
    
    def moveNorth(self):
        try:
            if self.currentRoom.getNorthExit() != None:
                self.currentRoom = self.currentRoom.getNorthExit()
        except Exception:
            print("\nThere is no room there")
    
    def moveEast(self):
        try:
            if self.currentRoom.getEastExit() != None:
                self.currentRoom = self.currentRoom.getEastExit()
        except Exception:
            print("\nThere is no room there")
        
    def moveSouth(self):
        try:
            if self.currentRoom.getSouthExit() != None:
                self.currentRoom = self.currentRoom.getSouthExit()
        except Exception:
            print("\nThere is no room there")
        
    def moveWest(self):
        try:
            if self.currentRoom.getWestExit() != None:
                self.currentRoom = self.currentRoom.getWestExit()
        except Exception:
            print("\nThere is no room there")
    
    def getCurrentRoom(self):
        return self.currentRoom
    
    def getCurrentRoomName(self):
        return self.currentRoom.getName()
    
    def getCurrentRoomDescription(self):
        return self.currentRoom.getDescription()
    
    def getCurrentRoomExits(self):
        return self.currentRoom.getAllExits()