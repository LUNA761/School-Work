import os

if not os.path.exists("my_quotes.txt"):
    with open("my_quotes.txt", "w+") as f:
        f.close()

with open("my_quotes.txt", "a") as f:
    for i in range(3):
        q = input(f"Quote #{i+1} ~ ")
        f.write("\n{}".format(q))
        print(f"Added: '{q}' to the file!")
    f.close()

