a = [1,2,False,6,2]
b = [1,2,False,6,2]

x = [1,2,5,6,2]
y = [1,2,5,6,5,3]

l = [1,2,5,6,5,16]
m = [1,2,5,6,5]

a1 = ['this', 'is', 'a', 'list', 'of', 'strings', True]
b1 = ['this', 'is', 'a', 'list', 'of', 'strings', True]

x1 = ['celery','carrots','bread','milk']
y1 = ['celery','carrots','bread','cream']



def list_compare(list_1, list_2):
    if list_1 == list_2:
        print 'The lists are the same'
    else:
        print 'The lists are not the same'


list_compare(a,b)
list_compare(x,y)
list_compare(l,m)
list_compare(a1,b1)
list_compare(x1,y1)
