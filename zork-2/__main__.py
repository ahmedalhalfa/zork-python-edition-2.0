import sys

if __name__ == "__main__" :



    print("Hello, this is the zork adventures game!, Do you dare playing ?")
    print("1 --> play")
    print("2 --> i don't have the balls to do it")
    next = input("> ")

    if next == '1' :

        from modules.utilities import utils

        print("enter your name > ",end=" ")
        player = input()

        o_player = utils.Character(player)
        start = utils.Start(o_player)

    else :
        print("Oh such a pussy sucker!")
        print("Press any key to exit ...")
        input("> ")
        exit(0)
