from player import Player
from room import Room
from item import Item
from weapon import Weapon

def main():
    
    #Items
    coin = Item("Coin","A circular form of exchange","Common")
    
    #Rooms
    hallway = Room("Hallway", "You come to a hallway that goes 4 directions")
    entrance = Room("Entrance", "You arrive to a giant stone door, careful...",[coin,coin,coin,coin])
    treasure = Room("Treasury", "You found treasure! Congrats!",[])
    library = Room("Library", "There are books everywhere here",[])
    armory = Room("Armory", "You see lines of armor and tools across the walls.",[])
    bossRoom = Room("Boss Room", "You come accross a giant figure in the middle of the room")
    
    # answer = "y"
    # while answer == "y":
    #     name = input("What is your name? ")
    #     answer = input("You current name is "+name+", Would you like to change it? y/n ")

    link_rooms(hallway, "north", armory, "south")
    link_rooms(hallway, "east", library, "west")
    link_rooms(hallway, "south", treasure, "north")
    link_rooms(hallway, "west", entrance, "east")
    link_rooms(treasure, "south", bossRoom, "north")

    player = Player("name", entrance)

    game = "on"
    
    while game == "on":
        
        if player.getCurrentRoom().hasItems():
            itemNames = player.getCurrentRoom().getItemNames()
            print(f"\n\nYou locate the following items: {itemNames}")
        else:
            print(f"\n\nThis room has no items")
        
        choice = input(f"\nYou are in {player.getCurrentRoomName()}\n{player.getCurrentRoomDescription()}\n\nAvailable exits: {player.getCurrentRoom().getAllDirections()}\n\n>")

        if choice.lower() == "exit":
            game = "off"
        
        elif choice[0:4].lower() == "take":
            item = choice[5:]
            player.takeItem(item)
        
        elif choice[0:4].lower() == "info":
                item = choice[5:]
                player.displayItem(item)
        
        elif choice[0:5].lower() == "equip":
            item = choice[6:]
            player.equip(item)
        
        elif choice.lower() == "stats":
            print(player.getPlayerStats())
            
        elif choice.lower() == "inventory":
            print(player.displayInventory())
        
        elif choice.lower() in ["north", "east", "south", "west"]:
            player.move(choice.lower())
        
        else: print("Invalid Command")
            


def link_rooms(room1, direction, room2, opposite_direction):
    room1.addExit(direction, room2)
    room2.addExit(opposite_direction, room1)



if __name__ == "__main__":
    main()