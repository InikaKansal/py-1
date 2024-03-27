import random
number = random.randint(1,10)
chances = 0
while chances<5:
    chances = chances + 1
    guess = int(input("Enter a number"))
    if guess > number:
        print("Too High! Enter a lower number.")
    elif guess < number:
        print("Too Low! Enter a higher number.")
    elif guess == number:
        print("You Won!") 
        break
if chances == 5:
    print("You Lose!")
    print("The number was " + str(number))