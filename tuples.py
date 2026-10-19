#Tuples in Python
t = ("apple",) #Tuple with single element
fruits = ("apple", "banana", "cherry", "pineapple")
print(fruits[0]) #Accesssing elements in a tuple
print(len(fruits)) #Length of a tuple
#Updating a Tuple
temp_list = list(fruits)
temp_list[1] = "kiwi"
fruits = tuple(temp_list)
print(fruits)