def perimeter_of_rectangle(length: float, width: float):
    return (length + width) * 2

l = float(input("Length~ "))
w = float(input("Width~ "))

perimeter = perimeter_of_rectangle(l, w)

print(perimeter)

input()
