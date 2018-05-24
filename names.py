################## PART 1: ##################
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def print_dict(info):
    for values in info:
       print values['first_name'], values['last_name']

print_dict(students)

################## PART 2: ##################

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def print_nested_dict(info):
    for key in info:
        idNum = 1 
        print key 
        for value in info[key]:
            print idNum, '-', value['first_name'], value['last_name'], '-', (len(value['first_name'])+len(value['last_name']))
            idNum += 1

print_nested_dict(users)
