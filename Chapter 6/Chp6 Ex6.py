def is_palindrome(s: str):
    if s == s[::-1]:
        return True
    else:
        return False

my_str = input("Word ~ ")

print(is_palindrome(my_str))

input()
