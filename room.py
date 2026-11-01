class Room:
    all_rooms = []
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        Room.all_rooms.append(self)
    
    def addExit(self, direction, room: "Room"):
        self.exits[direction.lower()] = room
    
    def setName(self, name):
        self.name = name
        
    def setDescription(self, description):
        self.description = description
    
    def getName(self):
        return self.name
    
    def getDescription(self):
        return self.description
        
    def getRooms(self):
        return self.all_rooms
    
    def getExit(self, direction):
        return self.exits.get(direction.lower())

    def getAllDirections(self):
        return [direction.capitalize() for direction in self.exits.keys()]
        
    
    def __str__(self):
        return f"Name: {self.name} Description: {self.description}"
