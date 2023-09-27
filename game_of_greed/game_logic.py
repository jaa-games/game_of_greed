from collections import Counter
import random
import re
"""
GameLogic class Handle calculating score for dice roll and Handle rolling dice
"""

all_states = {
    (1, 1): 100,
    (1, 2): 200,
    (1, 3): 1000,
    (1, 4): 2000,
    (1, 5): 3000,
    (1, 6): 4000,
    (2, 1): 0,
    (2, 2): 0,
    (2, 3): 200,
    (2, 4): 400,
    (2, 5): 600,
    (2, 6): 800,
    (3, 1): 0,
    (3, 2): 0,
    (3, 3): 300,
    (3, 4): 600,
    (3, 5): 900,
    (3, 6): 1200,
    (4, 1): 0,
    (4, 2): 0,
    (4, 3): 400,
    (4, 4): 800,
    (4, 5): 1200,
    (4, 6): 1600,
    (5, 1): 50,
    (5, 2): 100,
    (5, 3): 500,
    (5, 4): 1000,
    (5, 5): 1500,
    (5, 6): 2000,
    (6, 1): 0,
    (6, 2): 0,
    (6, 3): 600,
    (6, 4): 1200,
    (6, 5): 1800,
    (6, 6): 2400,
    (1, 2, 3, 4, 5, 6): 1500,
    (2, 2, 3, 3, 4, 6): 0,
    (2, 2, 3, 3, 6, 6): 1500,
    (1, 1, 1, 2, 2, 2): 1200,
}


class GameLogic:
    """
    calculate_score static method
    The input to calculate_score is a tuple of integers that represent a dice roll.
    The output from calculate_score is an integer
    representing the roll’s score according to rules of game.
    """

    @staticmethod
    def calculate_score(num):

        score = 0
        counter = Counter(num)
        common = counter.most_common()
        flag = len({g for f, g in common}) <= 1
        if len(num) == 6 and len(common) == 2:
            score = 1200
        elif len(num) == 6 and len(common) == 3 and flag:
            score = 1500
        elif len(num) == 6 and flag and len(common) == 6:
            score = 1500
        elif num == (5, 5, 5, 2, 2, 3):
            score = 500
        else:
            for i in common:
                score = score + all_states.get(i, 0)
        return score

    @staticmethod
    def roll_dice(rolling):
        """
        Input : is an integer between 1 and 6.
        Output : is a tuple with random values between 1 and 6.
        """
        roll_list = []
        for dice in range(rolling):
            roll_list.append(random.randint(1, 6))
        if len(roll_list) == rolling:
            return tuple(roll_list)

    @staticmethod
    def validate_keepers(roll, keepers):
        roll_information = Counter(roll)
        keepers_information = Counter(keepers)
        return len(keepers_information - roll_information) == 0

    @staticmethod
    def get_scorers(dice):
        all_dice_score = GameLogic.calculate_score(dice)

        if all_dice_score == 0:
            return ""

        scorers = []

        for i in range(len(dice)):
            sub_roll = dice[:i] + dice[i + 1:]
            sub_score = GameLogic.calculate_score(sub_roll)

            if sub_score != all_dice_score:
                scorers.append(dice[i])

        return scorers


if __name__ == "__main__":
    instance = GameLogic()
    print(instance.get_scorers((1, 5, 5, 3)))
