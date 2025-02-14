# import 'random' module for random operations
import random

def get_upper_bound():
    """
    Prompt user to enter the upper limit of guessing game.

    Return: upper_bound - the highest number in the range of numbers.
    """
    prompt = True
    while prompt:
        upper_bound = input("Please enter a number greater than 1. ")
        # Check if all characters in upper_bound are digits and if the upper_bound is greater than 1.
        if upper_bound.isdigit() == True and int(upper_bound) > 1:
            upper_bound = int(upper_bound)
            prompt = False
            return upper_bound
        else:
            # Handle out of range and non-integer inputs
            print("Invalid input! Please try again.")


def create_random_num(upper_bound):
    """
    Generate a random integer between 1 and the users upper bound.

    Parameter: num - the upper limit of the game.
    Return: random_int - a random number to be guessed
    """
    random_int = random.randint(1, upper_bound)
    return random_int

def play_game(upper_bound, random_num):
    """
    Have user guess the random number while giving hints.

    Parameter: 
    upper_bound - the largest number in the range of numbers
    random_num - the random number the user has to guess.
    """
    count = 1
    prompt = True
    while prompt:
        guess = input(f"Please enter a number between 1 and {upper_bound}: ")
        if guess.isdigit() == True and int(guess) > 1:
            guess = int(guess)
            #Conditions to give the user hints
            if guess < random_num:
                print("- - Nope, your guess is too low. Try again! - -")
                count += 1
            elif guess > random_num:
                print("- - Nope, your guess is too high. Try again! - -")
                count += 1
            else:
                prompt = False
                print("Congrats, your guess is correct.")
                print(f"Secret number: {random_num}")
                print(f"Your guess: {guess}")
                print(f"Total attempts: {count}")
                print("Thanks for playing!")
        else:
            print("Invalid input. Please try again!")

def main():
    """
    Handle game flow
    """
    upper_bound = get_upper_bound()
    secret_number = create_random_num(upper_bound)
    play_game(upper_bound, secret_number)

main()
