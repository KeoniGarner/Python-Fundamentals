my_info = {
    'name': 'Keoni Garner',
    'age': 21,
    'hometown': 'Bakersfield, CA',
    'favorite_language': 'Python'
}

def print_dict(dictionary):
    for key, value in dictionary.iteritems():
        print 'My', key, 'is', value

print_dict(my_info)
