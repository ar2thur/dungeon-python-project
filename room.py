from item import Item
class Room:
    all_rooms = []
    def __init__(self, name, description, items: list[Item] = None):
        self.name = name
        self.description = description
        self.exits = {}
        if items is not None:
            self.items = items
        else:
            self.items = []
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
    
    def getItems(self):
        return self.items
    
    def getItemNames(self):
        itemNames = []
        itemCounts = {}

        for item in self.items:
            itemNames.append(item.getName())

        for name in itemNames:
            if name in itemCounts:
                itemCounts[name] += 1
            else:
                itemCounts[name] = 1
        
        itemNamesFormatted = []

        for name in itemCounts:
            count = itemCounts[name]
            if count > 1:
                itemNamesFormatted.append(f"{name} * {count}")
            else:
                itemNamesFormatted.append(name)

        return itemNamesFormatted
    
    def hasItems(self):
        if self.items:
            return True
        else: return False
    
    def removeItemInRoom(self, item: Item):
        self.items.remove(item)
    
    def removeAllItemsInRoom(self):
        self.items = None
    
    def __str__(self):
        return f"Name: {self.name} Description: {self.description}"
