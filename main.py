from player import Player
from room import Room
from item import Item
from weapon import Weapon
from armor import Armor

def main():
    
    #Items
    coin = Weapon("Coin","A circular form of exchange","Common",200)
    helmet1 = Armor("Helmet1","A basic helmet", "Common", 10, "helmet")
    helmet2 = Armor("Helmet2","A basic helmet", "Common", 10, "helmet")
    helmet3 = Armor("Helmet3","A basic helmet", "Common", 10, "helmet")
    
    #Rooms
    hallway = Room("Hallway", "You come to a hallway that goes 4 directions")
    entrance = Room("Entrance", "You arrive to a giant stone door, careful...",[helmet1, helmet2, helmet3])
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

        choiceArr = choice.split()

        if choiceArr[0] == "exit":
            game = "off"
        
        elif choiceArr[0] == "take":
            item = choiceArr[1] #item
            if len(choiceArr) > 2:
                num = int(choiceArr[2]) #amount
                player.takeItems(item,num)
            else:
                player.takeItems(item)
        
        elif choiceArr[0] == "info":
            item = choiceArr[1]
            player.displayItem(item)
        
        elif choiceArr[0] == "equip":
            item = choiceArr[1]
            player.equip(item)
        
        elif choiceArr[0] == "unequip":
            item = choiceArr[1]
            player.unEquip(item)
        
        elif choiceArr[0] == "stats":
            print(player.getPlayerStats())
            
        elif choiceArr[0] == "inventory":
            print(player.displayInventory())
        
        elif choice[0] in ["north", "east", "south", "west"]:
            player.move(choice.lower())
        
        else: print("Invalid Command")
            


def link_rooms(room1, direction, room2, opposite_direction):
    room1.addExit(direction, room2)
    room2.addExit(opposite_direction, room1)



if __name__ == "__main__":
    main()