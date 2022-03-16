def input_values():
	a = int(input("Input a ~ "))
	b = int(input("Input b ~ "))
	c = int(input("Input c ~ "))
	d = int(input("Input d ~ "))
	M = int(input("Input M ~ "))
	N = int(input("Input N ~ "))

	return a,b,d,c,M,N

def calc_H(a,b,d,c,M,N):
	return (a + b) * M + (c + d) * N



a,b,d,c,M,N = input_values()
H = calc_H(a,b,d,c,M,N)

print(f"The value of H is {H}")

input() # Ignore this (for console)