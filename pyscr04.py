#Data types in Python - Dynamic Typing

#Multiple Assignment
a = b = c = 123
print("a = ", a, "b = ", b, "c = " ,c, "\n")

#Also
x, y, z = "Allwyn", 27, "Computer Engineer"
print("x = ", x, "\ny = ", y, "\nz = ", z)

#Variables can also be deleted, for example...
try:
	del x	#This will give a "x not defined" error
	print("x = ", x, "\ny = ", y, "\nz = ", z)
except Exception as error:
	print("Caught Error : ", error, "\n");

#String in Python
str = "Hello World"
print(str)
print(str[0])
print(str[6:11])	#This one is a little tricky ;)
print(str[4:])
print(str * 2)
print(str + "!!!\n")

#LISTs - Like arrays with inner dynanic typing. Values can be changed
list = ["Apple", 3, "Banana", 20, 8888788338]
tinylist = ["Safari", '1500']
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist * 2)
print(list + tinylist)
del list[2]
print(list, "\n")

#Tuple - similar to lists, but values once set cannot be changed
tuple = ('Mars', 4, 'Earth', 3, 'Jupiter', 5)
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
try:
	tuple[4] = "Uranus"
except Exception as error:
	print("Caught Error : ", error, "\n")
	
#Dictionary - Kind of hash table that stores data in key-value pairs
dict = {}
dict['one'] = "This is One"
dict[2] = "This is two"
print(dict['one'], " & ", dict[2], "\n")

tinydict = {'name' : 'Allwyn', 'code' : 34, 'dept' : 'Forensics'}
print(tinydict)
print(tinydict.keys())
print(tinydict.values())




















