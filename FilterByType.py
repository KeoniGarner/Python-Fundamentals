def filterByType(obj):
    if type(obj) is int:
        if obj >= 100:
            print("That's a big number!")
        else:
            print("That's a small number")
    elif type(obj) is str:
        if len(obj) >= 50:
            print("Long sentence.")
        else:
            print("Short sentence.")
    elif type(obj) is list:
        if len(obj) >= 10:
            print("Big list!")
        else:
            print("Short list.")
       