from modules.bricks import actions

class Character(object):

    hp = 1000                       # class variable refered to the player remaining health
    def __init__(self,character) :

        self.player_name = character
        

class Start(object):

    # super().__init__(character)

    def __init__(self,player) :

        self.player = player         # object to our character
        actions.Explore(self.player)
