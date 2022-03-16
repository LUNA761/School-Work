import random

magic_num = random.randint(0, 10)

correct = False

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

input()