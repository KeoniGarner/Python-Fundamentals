def stars(list):
    for element in list:
        if type(element) is str:
            print element[0].lower() * len(element)
        elif type(element) is int:
            print '\033[1;31m *\033[1;m' * element 

stars([1,2,3])
stars([4,5,'Hello',6,'World'])
stars([6,5,'Biggest and longest yet',4,3,2,11,'eleven'])


