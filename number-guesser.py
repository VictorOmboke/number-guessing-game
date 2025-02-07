# import 'random' module for random operations
import random

def create_random_num():
    """
    Generate a random integer between 1 and 100
    """
    random_int = random.randint(1, 100)
    return random_int

def get_user_guess():
    """
    Get users input to guess the correct number.
    """
    try: 
        user_guess = int(input("Pick a number between 1 and 100. "))
        if user_guess < 0 or user_guess > 100:
            raise ValueError(f"'{user_guess}' is out of range! Enter a number between 1 and 100.")
    except ValueError as e: 
        print(f"'{user_guess}' is not a number. Enter a number between 1 and 100.")
        print(e)
    else:
        print(user_guess)
        

get_user_guess()