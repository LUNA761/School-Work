def calc_score(word: str):
    score = 0
    for letter in word:
        if letter not in ["a", "e", "i", "o", "u"]:
            continue

        if letter == "a":
            score += 5
        
        elif letter == "e":
            score += 4
        
        elif letter == "i":
            score += 3
        
        elif letter == "o":
            score += 2
        
        elif letter == "u":
            score += 1
    
    return score

score = calc_score(input("Word ~ "))

print(f"Score: {score}")

input()
