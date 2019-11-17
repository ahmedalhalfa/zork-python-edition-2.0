from modules.bricks import actions

class Place(object) :

    def __init__ (self) :
        print("This place is undefined!")


class Island_gate(Place) :

    def __init__(self):
        print("Island gate!!!!")
        reaction = input("> ")

        if reaction == "go home" :

            actions.Go_home()

        elif reaction == "explore" :

            actions.Explore()
class Gold_room_gate(Place) :
    pass

class Gold_room(Place) :
    pass

class Prison(Place) :
    pass

class Diamond_room(Place) :
    pass
