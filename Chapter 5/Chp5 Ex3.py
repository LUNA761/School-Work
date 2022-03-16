score = float(input("Score~ "))

if score >= 80:
    print("You passed, well done!")

elif score >= 50 :
    print("You passed!")

elif score <= 49 and score > 20:
    print("You failed.")

else:
    print("You need to try harder.")

input()
