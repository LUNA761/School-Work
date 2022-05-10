fruits_handle = open("fruits.txt", "r")
fruits = fruits_handle.readlines()

while 1:
    search_query = input("Query~")
    print("\nResults:")
    found = False
    for fruit in fruits:
        if search_query in fruit.lower():
            found = True
            fruit_found = fruit.split(",")
            print(f"Item: {fruit_found[0]}, Units: {fruit_found[1]} Price: {fruit_found[2]}")
        
    if not found:
        print("Not found")
