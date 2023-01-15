#Word - Play
#Author - itzOP
#info - program to play numbe guessing game

#Importing random
import random

#Generating number to be guessed
number = random.randint(1, 100)
#Getting input and proceeding with program
print('I am thinking of a number between 1 and 100 and you have 5 chance to get it right.')
try:
    for i in range(6):
        guess = int(input("Guess the number: "))
        if guess == number:
            print("You won!")
            exit()
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")
    print("You lost! The number was", number)
except Exception as e:
    print("OOPS",e)
