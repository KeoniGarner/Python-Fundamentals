name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]


def lists_to_dict(list_1, list_2):
    new_dict = {} 
    for i in range(0, len(list_1)-1):
        new_dict[list_1[i]] = list_2[i]
    return new_dict

print lists_to_dict(name, favorite_animal)
