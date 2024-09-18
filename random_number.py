import random


def guess(a):
    # function to return a random integer
    random_number = random.randint(1, a)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {a}: "))
        if guess < random_number:
            print("Sorry, Too low")
        elif guess > random_number:
            print("Sorry, Too high")
    print(f"You have guessed the number {random_number}")

guess(100)
