def calc_score(score):
    if score <= 50 and score > 41:
        print("You got an A")

    elif score > 31 and score < 50:
        print("You got a B")

    elif score > 21 and score < 50:
        print("You got a C")

    elif score > 11 and score < 50:
        print("You got a D")

    elif score > 10 and score < 0:
        print("You got a U")

    else:
        print("Your score is either too high or too low!")

while 1:
    score = int(input("Please enter a score~ "))
    calc_score(score)
