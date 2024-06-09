import random


def dice_sum(num_dice: int = 1):
    """dice_sum(num_dice) returns the sum of num_dice 6-sided dice."""
    total = 0
    for i in range(num_dice):
        dice_roll = random.randint(1, 6)
        total += dice_roll
    return total


class Character:
    """ A Fighting Fantasy Character Object"""

    def __init__(self, name, skill=0, stamina=0):
        self.name = name
        self.skill = skill
        self.stamina = stamina
        self.roll = None
        self.score = None

    def find_score(self):
        self.roll = dice_sum(num_dice=2)
        self.score = self.roll + self.skill

    def fight_round(self, other):
        self.find_score()
        other.find_score()
        if self.score > other.score:
            result = 'won'
            other.stamina -= 2
        elif self.score < other.score:
            result = 'lost'
            self.stamina -= 2
        else:
            result = 'draw'
            self.stamina -= 1
            other.stamina -= 1
        return result

    def __repr__(self):
        return f"Character('{self.name}', skill={self.skill}, stamina={self.stamina})"


class PlayerCharacter(Character):
    def generate_stats(self):
        self.skill = 6 + dice_sum(1)
        self.stamina = 12 + dice_sum(2)


def fight_battle(player, opponent):
    continue_fighting = True
    while continue_fighting:
        print(f"Player {player.name} has skill {player.skill} and stamina {player.stamina}")
        print(f"Monster {opponent.name} has skill {opponent.skill} and stamina {opponent.stamina}")
        action = input("Would you like to fight a round (y/n)?")
        print()
        if action == 'n':
            print("You flee in terror!")
            continue_fighting = False
        else:
            result = player.fight_round(opponent)
            print(f"Player rolled {player.roll} for a total score of {player.score}")
            print(f"Opponent rolled {opponent.roll} for a total score of {opponent.score}\n")
            if result == 'won':
                print('You won this round')
            elif result == 'lost':
                print('You lost this round')
            else:
                print('This round was a draw')
            if player.stamina <= 0:
                print('You died')
                continue_fighting = False
            if opponent.stamina <= 0:
                print(f"You defeated the {opponent.name}")
                continue_fighting = False


if __name__ == "__main__":
    creatures = [Character("Dragon", 10, 22),
                 Character("Orc", 7, 10),
                 Character("Skeleton", 5, 8),
                 Character("Rat", 6, 6),
                 ]
    player_name = input("Enter the name for your character: ")
    PC = PlayerCharacter(player_name)
    PC.generate_stats()
    print(f"Welcome {PC.name}")
    monster = random.choice(creatures)
    print(f"You will be fighting {monster.name}\n")

    fight_battle(PC, monster)
