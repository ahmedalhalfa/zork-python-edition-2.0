from modules.bricks import actions

class Event(object) :

    # events = {
    # "bear" : Bear(),
    # "dead" : Dead(),
    # "lion" : Lion(),
    # "ape" : Ape(),
    # "gorilla" : Gorilla()
    # }
    pass

class Bear(Event) :

    def __init__(self, player):
        print("You are now facing the bear , get ready to get wricked!")
        self.o_player = player

        print("do you dare to fight ?")
        ans = input("> ")
        if ans == "yes" :
            actions.Fight()
        else :
            actions.Go_home()
            
class Dead(Event) :
    pass

class Lion(Event) :
    pass

class Ape(Event) :
    pass

class Gorilla(Event):
    pass
