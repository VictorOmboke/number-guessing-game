# import 'random' module for random operations
import random

def create_random_num():
    """
    Generate a random integer between 1 and 100
    """
    random_int = random.randint(1, 100)
    return random_int

print(f"Random Number: {create_random_num()}")

def get_upper_bound():
    """
    Prompt user to enter the upper limit of guessing game.
    """
    prompt = True
    while prompt:
        num = input("Please enter a number greater than 1. ")
        # Check if all characters in num are digits and if the num is greater than 1.
        if num.isdigit() == True and int(num) > 1:
            print(f"Your guess: {num}")
            prompt = False
        else:
            # Handle out of range and non-integer inputs
            print("Invalid input! Please try again.")

get_upper_bound()
            