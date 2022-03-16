def long_name(name: str):
    if len(name) >= 14:
        return True
    else:
        return False

print(long_name(input("Name ~ ")))

input()