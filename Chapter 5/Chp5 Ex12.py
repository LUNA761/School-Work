import random

magic_num = random.randint(0, 10)
correct = False
guesses = 5

def magic_number(guess: int):
    if guess > magic_num:
        print("Too High!")
    
    elif guess < magic_num:
        print("Too Low!")
    
    else:
        print("Correct!")
        correct = True

while not correct:
    magic_number(int(input("Guess ~ ")))
    guesses -= 1
    if guesses == 0:
        print("You have ran out of guesses")
        break

input()