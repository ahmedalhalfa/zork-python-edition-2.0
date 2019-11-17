from modules.bricks import places , events

class Action(object) :
    pass
    # places = {
    #         "island_gate" :  places.Island_gate(),
    #         "gold_room_gate" : places.Gold_room_gate(),
    #         "gold_room" : places.Gold_room(),
    #         "prison" : places.Prison(),
    #         "diamond_room" : places.Diamond_room()
    # }
    #
    # actions = {
    # "enter" : Enter(),
    # "explore" : Explore(),
    # "go_home" : Go_home(),
    # "open_door" : Open_door(),
    # "fight" : Fight(),
    # "run" : Run(),
    # "shoot" : Shoot(),
    # "take_key" : Take_key()
    # }

# class Enter_island(Action) :
#
#     def __init__(self,current_place) :
#         places.get(current_place)
class Explore(Action) :

    def __init__(self,player) :

        self.player = player
        print("Welcome to the island of treasures , You either win the big prize or get killed (or maybe arrested)" , self.player.player_name)

        events.Bear(self.player)

class Go_home(Action) :

    def __init__(self) :

        print("okay Good luck")
        print("Game over")
        print("press any button to exit")
        input("> ")
        exit(0)


class Open_door(Action) :
    pass

class Fight(Action) :

    print("Fighting !")
    exit(0)

class Run(Action) :
    pass

class Shoot(Action) :
    pass

class Take_key(Action) : # kinda
                         # useless
    pass
