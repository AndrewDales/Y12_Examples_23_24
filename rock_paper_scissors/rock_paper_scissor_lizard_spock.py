import random

RULES = {'rps': {'rock': ['scissors', ],
                 'scissors': ['paper'],
                 'paper': ['rock'],
                 },
         'rpsls': {'rock': ['scissors', 'lizard'],
                   'scissors': ['paper', 'lizard'],
                   'paper': ['rock', 'spock'],
                   'lizard': ['paper', 'spock'],
                   'spock': ['scissors', 'paper'],
                   },
         }


class PlayerObject:
    """ A object representing something that a player may choose

        Class attributes
        ----------------
        rules: a dictionory of dictionaries giving the wins for the PlayerObjects. Default is 'rock paper scissors'
        allowable_objects: the types of object that the players may choose
        """

    rules = RULES['rps']
    allowable_objects = tuple(rules.keys())

    def __init__(self, name):
        """
        Constructs the attributes for the PlayerObject

        Parameter
        ---------
            name: str
                name of object - must be in allowable objects
        """

        self.name = name.lower()

    @classmethod
    def set_rules(cls, rules=None):
        """ Sets the victory rules for the PlayerObjects"""
        cls.rules = rules
        cls.allowable_objects = tuple(rules.keys())

    @classmethod
    def random_object(cls, rules=None):
        """
        Returns a random object from amongst the allowable objects
        """
        if rules:
            cls.set_rules(rules)
        return PlayerObject(random.choice(cls.allowable_objects))

    def __repr__(self):
        return f'PlayerObject({self.name})'

    def __str__(self):
        return self.name.title()

    def __gt__(self, other):
        return other.name in self.rules[self.name]

    def __eq__(self, other):
        return self.name == other.name


# The Player Class represents a player
class Player:
    """
    A class to represent a player of the game

    Attributes
    __________
        name: str
            Player name
        score: int
            Player score
        current_object: PlayerObject or None
            What the player's current object is None for not selected
    """

    def __init__(self, name=None):
        """
        Constructs the necessary attributes for the Player class
        """
        if name:
            self.name = name
        else:
            self.name = ""
        self.score = 0
        self.current_object = None

    def set_name(self, name):
        """ Sets name attribute to name """
        self.name = name

    def reset_object(self):
        """ Sets the current_object to None - not selected"""
        self.current_object = None

    def win_round(self):
        """ Increases score by one """
        self.score += 1

    def __repr__(self):
        """ Representation of the object """
        check_object_chosen = bool(self.current_object)
        return f'Player: {self.name}\nScore: {self.score}\nObject chosen: {check_object_chosen}'


# The HumanPlayer Class is a subclass of Player representing a human player
class HumanPlayer(Player):
    """ Subclass of Player representing a human player (PC) """

    def choose_object(self, choice):
        """ Chooses a PlayerObject for the player"""
        self.current_object = PlayerObject(choice)


# The ComputerPlayer Class is a subclass of Player representing a Computer player
class ComputerPlayer(Player):
    """ Subclass of Player representing a Computer player (NPC) """

    def __init__(self):
        """ Constructs super Player object with name "Computer """
        super().__init__('Computer')

    def choose_object(self):
        """ Computer chooses a random PlayerObject """
        self.current_object = PlayerObject.random_object()

if __name__ == "__main__":
    PlayerObject.set_rules(RULES['rpsls'])
    player = HumanPlayer('Andrew')
    computer = ComputerPlayer()
    player.choose_object()