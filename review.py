'''
Parameters vs. Arguments
'''
# In this case, a is a parameter.
def func(a):
    return a**2

# In this case, the value we input (5) is an argument.
print(func(5))



'''
Opening, reading, and writing files.
'''
# With w, you can write.
with open("sample_file.txt", "w") as f:
    f.write("apples")

# With r, you can read.
with open("sample_file.txt", "r") as f:
    print(f.read())

# With w+, you can write then read.
with open("sample_file.txt", "w+") as f:
    f.write("bananas")
    f.seek(0)
    print(f.read())

# With a+, you can append.
with open("sample_file.txt", "a+") as f:
    f.write("lemons")
    f.seek(0)
    print(f.read())



'''
The above methods work for strings, but what if we want to read and write lists?
We use a package called pickle.
To write, we use the method pkl.dump().
To read, we use the method pdk.load().
'''
import pickle as pkl

l1 = [2, 3, 4, 5]

# We put the list inside our file.
with open("sample_list_file.txt", "wb") as f:
    pkl.dump(l1, f)

# We read the list from the file and print it.
with open("sample_list_file.txt", "rb") as f:
    print(pkl.load(f))



'''
What if we want to concatenate strings together?
Concatenating strings is literally just putting them together.
Consider the following example:
'''
s1 = "apples"
s2 = "bananas"
print(s1 + s2)



'''
An index is just a position in a string or list
'''
l1 = [2, 3, 4, 5]

print(l1[0])  #Prints the very first element.
print(l1[3])  #Prints the fourth element.
print(l1[-1]) #Prints the last element.



'''
Importing specific functions from package.
For example, I only want to use the sqrt function from the math library.
If we use 'import math', it imports every function in the math library.
'''
from math import sqrt

print(sqrt(4))



'''
Lists, Sets, Tuples, and Dictionaries
'''
l1 = [2, 3, 4, 5]
l1.append(4) # Adds 4 to the end of the list.
print(l1)

# We can take the list and convert it to a set. Sets only consider unique values.
s = set(l1)
print(s)

# Lists are mutable.
l1[3] = 0
print(l1)

# Tuples are immutable and can repeat values.
t1 = tuple(l1)
print(t1)


# The following is a dictionary.
d1 = {1:"apples", 2:"oranges", 5:"lemons"}

#The keys are to the left of the colon and the values are to the right of the colon.
print(d1.keys())
print(d1.values())
print(d1[1])



'''
For Loops
'''
# Prints all values from 1-10 inclusive.
for i in range(1, 11):
    print(i)

# Doubles all the elements in the lists by accessing each element.
for i in l1:
    print(2 * i)

# Iterating over dictionary.
for k,v in d1.items():
    print(k,v)

# Create an empty list and fill it with the first 10000 numbers.
l2 = []
for i in range(1, 10001):
    l2.append(i)

# Square each element directly.
#for i in l2:
    #print(i**2)

'''
Maps and Filters
As seen from the last example, these for loops can take a while to compute.
To combat using a for loop directly, we can use the map function.
'''

# Squares each element of l2 without using a for loop. Since the function is simple, we
# can use a lambda function in this case.
print(list(map(lambda x: x**2, l2)))

def func(a):
    if a < 5000:
        return a
    else:
        return 0

# Returns a list of numbers 1-4999
print(list(filter(func, l2)))



'''
List Comprehension
'''
l1 = [5, 7, 6, 3]
print([x*x for x in l1])