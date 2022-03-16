def discount_ten(l: list):
    nl = []
    for price in l:
        price -= price / 10
        nl.append(price)
    
    return nl

prices = discount_ten([100, 20, 40, 80, 200])

print(prices)

input()
