# Question 1a
import random

myList = []
for i in range(0,30):
    myList.append(random.randint(0,100))

print(myList)

# Question 1b
filtered = []
for num in myList:
    if num > 60:
        filtered.append(num)
print(filtered)

total = 0;
for num in filtered:
    total += num
print(total)

import pickle as pkl
with open("cbento23_1b.txt", "wb") as f:
    pkl.dump(filtered, f)

# Question 1c

newFiltered = list(filter(lambda x : x>60, myList))
print(newFiltered)
print(sum(newFiltered))

with open("cbento23_1c.txt", "wb") as f:
    pkl.dump(newFiltered, f)