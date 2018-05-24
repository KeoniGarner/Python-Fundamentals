word_list = ['hello','world','my','name','is','Anna']
char = 'o'
char2 = "m"
char3 = "n"
subStr1 = "ll" 

def characterChecker(my_list, subString):
    new_list= []
    for element in my_list:
        if subString in element:   
            new_list.append(element) 
    print new_list


characterChecker(word_list, char)
characterChecker(word_list, char2)
characterChecker(word_list, char3)
characterChecker(word_list, subStr1)