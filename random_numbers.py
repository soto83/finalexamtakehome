import random as r
# list of numbers to be 500
l = []

for x in range(0, 500):
	l.append(r.randint(0, 1000))

# sort 
l.sort()
# reverse it to get nth sorted position
l.reverse()

print("Here are the random numbers", l)
n = int(input("Please pass in nth position to be printed "))

print("The number at position", n, "is", l[n])

# print answer before exiting
input()
