import random




class Die:
    """A die to play with."""

    def __init__(self):
        self.value = random.randint(1, 6)

    def roll(self):
        """Returns the rolled dice, or raises RolledOneException if 1."""

       
        return self.value

class HumanPlayer(object):
    """This class if for the player. they will tell the game if they want to hold or roll again"""

    def __init__(self, name=None):
        self.name = name
        self.score = 0


    def add_score(self, player_score):
        """Adds player_score to total score."""

        self.score += player_score


    def __str__(self):
        """Returns player name and current score."""

        return str(self.name) + ": " + str(self.score)


# class ComputerPlayer(Player):
#      """This is the computer player, responsiblity to compile turn scores from scoresheet"""
#      def __init__(self, number):


class ScoreSheet:
    """score box holder class."""

    def __init__(self):
        self.value = 0

if __name__ == "__main__":
    # main() 
    pass