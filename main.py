from player import Player
from room import Room

def main():
    
    hallway = Room("Hallway", "You come to a hallway that goes 4 directions")
    entrance = Room("Entrance", "You arrive to a giant stone door, careful...")
    treasure = Room("Treasury", "You found treasure! Congrats!")
    library = Room("Library", "There are books everywhere here")
    armory = Room("Armory", "You see lines of armor and tools across the walls.")
    
    answer = "y"
    while answer == "y":
        name = input("What is your name? ")
        answer = input("You current name is "+name+", Would you like to change it? y/n ")

    link_rooms(hallway, "north", armory, "south")
    link_rooms(hallway, "east", library, "west")
    link_rooms(hallway, "south", treasure, "north")
    link_rooms(hallway, "west", entrance, "east")


    print(hallway.getAllDirections())
    player = Player(name, entrance)
    
    game = "on"
    
    while game == "on":
        move = input(f"\nYou are in {player.getCurrentRoomName()}\n{player.getCurrentRoomDescription()}\n\nAvailable exits: {player.getCurrentRoom().getAllDirections()}\n\n>")
        if move.lower() == "exit":
            game = "off"
        player.move(move.lower())
            
    
def link_rooms(room1, direction, room2, opposite_direction):
    room1.addExit(direction, room2)
    room2.addExit(opposite_direction, room1)



if __name__ == "__main__":
    main()