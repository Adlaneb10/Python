#Random number game
import random
random_num = random.randint(0,10)

guess = int(input("Please guess a number from 0 to 10:"))

while(0<= guess <= 10):
    if guess == random_num:
        print("You win!")
        break
    if guess > random_num:
        print("Guess is too high")
    else:
        print("Guess too low")

    guess = int(input("Please guess another number from 0 to 10:"))
else:
        print("You left")