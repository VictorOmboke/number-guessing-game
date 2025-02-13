# import 'random' module for random operations
import random

def get_upper_bound():
    """
    Prompt user to enter the upper limit of guessing game.
    """
    prompt = True
    while prompt:
        num = input("Please enter a number greater than 1. ")
        # Check if all characters in num are digits and if the num is greater than 1.
        if num.isdigit() == True and int(num) > 1:
            num = int(num)
            prompt = False
            return num
        else:
            # Handle out of range and non-integer inputs
            print("Invalid input! Please try again.")


def create_random_num(upper_bound):
    """
    Generate a random integer between 1 and the users number.

    Parameter: num - the upper limit of the game.
    """
    random_int = random.randint(1, upper_bound)
    return random_int

print(f"Random Number: {create_random_num(get_upper_bound())}")
