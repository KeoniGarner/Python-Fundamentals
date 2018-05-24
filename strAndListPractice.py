import math

# Find and Replace
words = "It's thanksgiving day. It's my birthday,too!"

print(words.find("day"))

new_str = words.replace("day", "month")

print(new_str)

# Min and Max
x = [2,54,-2,7,12,98]

print(min(x))
print(max(x))

# First and Last
x = ["hello",2,54,-2,7,12,98,"world"]

print(x[0])
print(x[len(x)-1])

new_list = [x[0], x[-1]]

print(new_list)

# New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]

x.sort()
index = math.floor(len(x)/2)
first_half = x[:index]
second_half = x[index:]
second_half = [0] + second_half
second_half[0] = first_half
print(second_half)