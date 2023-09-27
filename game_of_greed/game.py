from game_of_greed.game_logic import *
from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
from collections import Counter
from random import randint
import sys

class Game():
    def __init__(self):
        self.round = 1
        self.dice_remain = 6
        self.dice = ()
        self.text_of_string = ''

    def main(self, roller, banker):
        print(f"Starting round {self.round}")
        print(f"Rolling {self.dice_remain} dice...")
        self.rolling(roller, banker)

    def rolling(self, roller, banker):
        self.dice = roller(self.dice_remain)
        self.text_of_string = ' '.join(map(str, self.dice))
        self.check_for_cheat(roller, banker)
    
    def check_for_zelch(self, roller, banker):
        if not GameLogic.calculate_score(self.dice):
            print("****************************************\n**        Zilch!!! Round over         **\n****************************************")
            print(f"You banked {0} points in round {self.round}")
            print(f"Total score is {banker.balance} points")
            self.round += 1
            self.dice_remain = 6
            self.main(roller, banker)

    def check_for_cheat(self, roller, banker):
        print(f'*** {self.text_of_string.strip()} ***')
        self.check_for_zelch(roller, banker)
        print('Enter dice to keep, or (q)uit:')
        prompt = input("> ").lower()
        if prompt == 'q':
            print(
                f"Thanks for playing. You earned {banker.balance} points")
            sys.exit()
        else:
            shelf = [int(n) for n in prompt if n.isdigit()]
            current_dice = Counter(self.dice)
            if not GameLogic.validate_keepers(current_dice, shelf):
                print("Cheater!!! Or possibly made a typo...")
                self.check_for_cheat(roller, banker)
            banker.shelf(GameLogic.calculate_score(shelf))
            self.dice_remain = len(self.dice) - len(shelf)
            print(
                f"You have {banker.shelved} unbanked points and {self.dice_remain} dice remaining")

            print("(r)oll again, (b)ank your points or (q)uit:")
            prompt = input("> ")
            if prompt == "b":
                self.dice_remain = len(self.dice) - len(shelf)
                print(
                    f"You banked {banker.shelved} points in round {self.round}")
                banker.bank()
                print(f"Total score is {banker.balance} points")
                self.round += 1
                self.dice_remain = 6
                self.main(roller, banker)
            elif prompt == 'r':
                self.dice_remain = len(self.dice) - len(shelf)
                if self.dice_remain == 0:
                    self.dice_remain = 6
                    print(f"Rolling {self.dice_remain} dice...")
                else:
                    print(f"Rolling {self.dice_remain} dice...")
                self.rolling(roller, banker)

            elif prompt == 'q':
                print(
                    f"Thanks for playing. You earned {banker.balance} points")
                sys.exit()

    def play(self, roller=GameLogic.roll_dice):
        print("Welcome to Game of Greed\n(y)es to play or (n)o to decline")
        self.choice = input('> ').lower()
        banker = Banker()
        if self.choice == 'y':
            self.main(roller, banker)
        else:
            print('OK. Maybe another time')
            sys.exit()


if __name__ == "__main__":
    g = Game()
    g.play()
