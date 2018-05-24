def listTypeChecker(a_list):
    newString = ""  
    stringType = False  
    Sum = 0    
    for element in a_list:
        if isinstance(element, str):
            newString += element + " "  
            stringType = True 
        elif isinstance(element, int):
            total += element  
        elif isinstance(element, float):
            total += element  

    if total > 0 and stringType == False:
        print 'The list in question only contained numbers. Their total is:', total
    elif total == 0 and stringType == True:
        print "This list in question only contained strings. Their content is:", newString
    else:
            print 'The list is of mixed type of values.' 
            print 'The numbers in the list total to:', total
            print "The string content is:", newString




listTypeChecker([-25, 'all', 'about', 30.5, 'that', 15, 'bass', 100])
listTypeChecker([1.25,2,3,4,5, -15, 20, 0, -5.07])
listTypeChecker(['hello','world,','this', 'is', 'a', 'string.'])