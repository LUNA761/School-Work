def largest(num1: int, num2: int, num3: int):
    if num1 > num2 and num1 > num3:
        return num1
    
    elif num2 > num1 and num2 > num3:
        return num2
    
    elif num3 > num1 and num3 > num2:
        return num3

print(largest(int(input("Num1 ~ ")), int(input("Num2 ~ ")), int(input("Num3 ~ "))))

input()
