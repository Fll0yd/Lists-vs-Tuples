#alist = ["Ken", "Beebz", 1]
#alist[0] = "Flloyd"
#print(alist)

#atuple = ("Ken", "Beebz", 1)
#atuple[0] = "Flloyd"
#print(atuple)

import timeit

#2block of memory
print(timeit.timeit(stmt='["red", "blue", "green", 5, 7, 12, 18, "dude"]' , number=10000000))
      
#1block of memory            
print(timeit.timeit(stmt='("red", "blue", "green", 5, 7, 12, 18, "dude")' , number=10000000))

#lists

drank = ["Bang", "Reign", "Redbull", "Monster"]

youtubers = ["NetworkChuck", "InternetMadeCoder", "Lazarbeam"]

#tuples

youtuber = ("NetworkChuck",  2.89000000000, "IT Tutorials")

#tuples can be unpacked...but so can lists

Flloyd = ("Ken", 34, "Bang")

(name, age, drink) = Flloyd

print(name)
print(age)
print(drink)

#no parenthesis or quotes and only one peice of data but still a tuple.
totallyatuple = 1,

print(type(totallyatuple))