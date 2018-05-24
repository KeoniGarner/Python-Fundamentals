####### Multiples

# Part 1: Prints all odd numbers from 1 - 1,000
for count in range(1, 1000, 2): # range defines the looping range
    print(count)

# Part 2: Prints all multiples of 5 from 5 to 1,000,000
for count in range(5, 1000000, 5):
    if count % 5 == 0:
        print(count)

####### Sum List

a = [1, 2, 5, 10, 255, 3]
list_sum = 0
for i in range(0, len(a)-1): # range from beginning to end of list
    list_sum += a[i] # add to running total

print(list_sum) # print sum

####### Average List

print(list_sum / len(a)) # take sum from before and divide it by length of list