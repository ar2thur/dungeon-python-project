from player import Player

def main():
    name = input("What is your name?")
    player = Player(name)
    print(player.name)

    player.takeDamage(50)

    print(player.health)




if __name__ == "__main__":
    main()