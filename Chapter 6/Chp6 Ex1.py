bank_holidays_in_month = [1, 0, 1, 1, 2, 0, 0, 1, 0, 0, 0, 2]

months = {
    "january": 0,
    "february": 1,
    "march": 2,
    "april": 3,
    "may": 4,
    "june": 5,
    "july": 6,
    "august": 7,
    "september": 8,
    "october": 9,
    "november": 10,
    "december": 11

}

def bank_holidays(month: str):
    return bank_holidays_in_month[months[user_month]]

while 1:
    user_month = input("Month ~ ").lower()

    if user_month not in months:
        print("That month does not exist.\nPlease try again.")
        continue
    
    else:
        break

print(f"{user_month.title()} has {bank_holidays(user_month)} bank holiday(s) in it.")

input()
