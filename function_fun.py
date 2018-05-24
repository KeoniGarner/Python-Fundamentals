# Odd/Even

def odd_even():
    for number in range(1,2001):
        if number % 2 == 1:
            print 'The number is {}. This is an odd number.'.format(number)
        else:
            print 'The number is {}. This is an even number.'.format(number)

odd_even()

# Multiply

x = [1,2,3,4,5]
y = [-2,-5,0,5,11]

def multiply(num_list, n):
    for i in range(0,len(num_list)):
       num_list[i] = num_list[i] * n
    return num_list


print multiply(x,5)
print multiply(y,-2.5)


# Hacker Challenge

def layered_multiples(arr):
    new_arr = []
    for i in range (0, len(arr)):
        #create new sublist
        new_arr.append([])  
        #variable to hold current number in arr
        num = arr[i]
        #append 1's to sublist (num/num will always equal to 1)
        while num > 0:
            new_arr[i].append(num/num)
            num -= 1
    return new_arr

x = layered_multiples(multiply([2,4,5],3))
print x