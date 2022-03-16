def input_values():
    for var in ["a","b","c","d","M","N"]:
        globals()[var] = int(input(f"Input {var} ~ "))

def calc_H():
    global a,b,d,c,M,N
    
    return (a + b) * M + (c + d) * N



input_values()
H = calc_H()

print(f"The value of H is {H}")

input() # Ignore this (for console)
