# print( "Hello, World!" )
# print(type("Hello, World!")) # data type of string
# print(type(42.4))# data type of float
# print(type(42))# data type of integer
# print(type(True))# data type of boolean
# print(type(2==2))# data type of boolean
# print(type([1, 2, 3]))# data type of list
# print(type((1, 2, 3)))# data type of tuple
# print(type({1, 2, 3}))# data type of set
# print(type({"a": 1, "b": 2}))# data type of dictionary

# ! variables
# can start with a letter or underscore, but not a number
# can not contain spaces or special characters except for underscores
# can not be a reserved word (like print, if, else, etc.)
# can not start with a number
# name not like my_var

# my_var = 42
# print(type(my_var))
# name = "Osama Elzero" # Single Word => Normal
# myName = "Osama Elzero" # Two Words => camelCase
# my_name = "Osama Elzero" # Two Words = snake Case

# variables part Two
# source code => code that is written by a programmer
# translation => converting source code into machine code
# compilation => converting source code into machine code before running the program
# runtime => converting source code into machine code while running the program
# interpreter => a program that translates source code into machine code while running the program

# x = 10
# x = 20
# print(x)
# help("keywords") # reserved words in python

# x , y , z = 1, 2, 3
# print(x)
# print(y)
# print(z)


# ! escape sequences characters

# print("Hello, World!") # Normal Print
# print("Hello, \nWorld!") # New Line
# print("Hello, \tWorld!") # Tab
# print("Hello, \\World!") # Backslash
# print("Hello, \bWorld!") # Backspace b will remove the space before it or the first character before it
# # Escape Single Quote
# print('I Love Single Quote \'Testl\'')
# # Escape Double Quotes
# print("I Love Double Quotes \"Testl\"")
# print("hello, \rWorld!") # Carriage Return useed to move the cursor to the beginning of the line
# print("123447, \rabvcf") # Carriage Return
# print("Hello, \fWorld!") # Form Feed
# print("Hello, \vWorld!") # Vertical Tab
# print("\x41") # Hexadecimal Value xhh character hex value
# print("\101") # Octal Value


# ! string concatenation
# can not concatenate string with number or other data types

# print("Hello, " + "World!") # Concatenation

# # Concatenation

# x = "Hello "
# y = "World"
# print(x +"    " + y) # "    " to define the space between the two strings

# full = x +"    " + y # Concatenation
# print(full) output: Hello World

# a = "first \
# second \
# third"

# v = "fourth"
# print(a+"\n" + v) # "\n" to define new line


# ! string Indexing and Slicing
# all data in python are objects and have methods and attributes
# object contains elements and each element has an index starting from 0 and going to n-1
# use square brackets to access the elements of an object
# indexing enables you to access individual elements of an object, while slicing allows you to access a range of elements.

# indexing accessing single element
# my_string = "Hello World!"
# print(my_string[0]) # H
# print(my_string[6]) # W
# print(my_string[-1]) # ! last element
# print(my_string[-6]) # W

# ! slicing accessing range of element
# #[start:stop] end index is not included, if stop index is not specified, it will default to the end of the string
# #[start:stop:step] step is optional and default is 1, if step is not specified, it will default to 1
# #[start:stop:step] step is optional and default is 1

# print(my_string[0:5]) # Hello
# print(my_string[:5]) # Hello if start index is not specified, it will default to 0
# print(my_string[6:]) # World! if stop index is not specified, it will default to the end of the string
# print(my_string[6:11]) # World!
# print(my_string[0:11:2]) # HloWrd step meen skipping every second character becouse step is 2
# print(my_string[::2]) # HloWrd


# ! string methods
# my_string = "Hello World!"
# my_stringg = "###@####Hello World!####@####"
# name = "mahmoud_elsayed-mahmoud"
# print(my_string.upper()) # HELLO WORLD! convert to uppercase
# print(my_string.lower()) # hello world! convert to lowercase
# print(my_string.capitalize()) # Hello world! convert first character to uppercase
# print(my_string.title()) # Hello World! convert first character of each word to uppercase and after numbers and special characters
# print(my_string.strip()) # Hello World! remove whitespace from the beginning and end of the string

# print(my_string.lstrip()) # Hello World! remove whitespace from the beginning of the string
# print(my_string.rstrip()) # Hello World! remove whitespace from the end of the string
# print(my_stringg.strip("#@")) # Hello World! remove '#' and '@' from the beginning and end of the string
# print(my_string.replace("Hello", "Hi")) # Hi World! replace a substring with another substring

# print(my_string.split()) # ['Hello', 'World!'] split the string into a list based on whitespace
# print(name.split("_")) # ['mahmoud', 'elsayed', 'mahmoud']  split the string into a list based on '_'
# print(name.split("-",1)) # ['mahmoud_elsayed', 'mahmoud'] split the string into a list based on '-'
# print(name.rsplit("_",1)) # ['mahmoud', 'elsayed-mahmoud'] split the string into a list based on '_' and limit the number of splits to 1

# print(len(my_string)) # 12 length of the string
# print(len(my_stringg)) # 22 length of the string

# c, b, d = 1, 22, 333
# print(str(c).zfill(3)) # 001 fill the string with zeros to the left to make it 3 characters long
# print(str(b).zfill(3)) # 022 fill the string with zeros to the left to make it 3 characters long
# print(str(d).zfill(3)) # 333 fill the string with zeros to the left to make it 3 characters long

# e = "reshe"
# print(e.center(11, "#")) # ###reshe### center the string and fill the rest with '#' to make it 11 characters long

# f = "reshe"
# print(f.count("e")) # 2 count the number of occurrences of 'e' in the string
# print(f.count("e", 0, 4)) # 1 count the number of occurrences of 'e' in the string from index 0 to 4

# g = "RESHA"
# k = "mahmoud"
# print(g.swapcase()) # RESHE swap the case of the string
# print(k.swapcase()) # MAHMOUD swap the case of the string

# i = "Hello World!"
# print(i.startswith("Hello")) # True check if the string starts with 'Hello'
# print(i.startswith("H", 2, 5)) # True check if the string starts with 'Hello' from index 0 to 5

# k = "Hello World!"
# print(k.endswith("World!")) # True check if the string ends with 'World!'
# print(k.endswith("!", 2, 12)) # True check if the string ends with 'World!' from index 2 to 12

# a = "Hello World!"
# print(a.index("o")) # 4 return the index of the first occurrence of 'o' in the string
# print(a.index("o", 5, 12)) # 7 return the index of the first occurrence of 'o' in the string from index 5 to 12
# print(a.index("o", 9, 12)) # ValueError: substring not found return the index of the first occurrence of 'o' in the string from index 9 to 12, if not found raise ValueError

# b = "Hello World!"
# print(b.find("o")) # 4 return the index of the first occurrence of 'o' in the string
# print(b.find("o", 5, 12)) # 7 return the index of the first occurrence of 'o' in the string from index 5 to 12
# print(b.find("o", 9, 12)) # -1 return the index of the first occurrence of 'o' in the string from index 9 to 12, if not found return -1


# ! rjust ljust

# c= "Hello World!"
# print(c.rjust(20, "#")) # ###########Hello World! right justify the string
# print(c.ljust(20, "#")) # Hello World!########### left justify the string


# ! splitlines

# d = "Hello\nWorld!"
# print(d.splitlines()) # ['Hello', 'World!'] split the string into a list based on newlines
# print(type(d.splitlines())) # <class 'list'> return the type of the object

# ! expandtabs
# e = "Hello\tWorld!"
# print(e.expandtabs(4)) # Hello   World! expand the tabs to 4 spaces

# # TASK i want to expand the tabs to 7 spaces and 18 spaces in the same print statement with two different strings and print them in two different lines
# a = "Hello\tWorld!"
# e = "Hello\tWorld!"
# print(a.expandtabs(7)+ "\n" + e.expandtabs(18)) # Hello   World! expand the tabs to 4 spaces and 8 spaces

# ! islower

# five = 'i love python'
# six = 'I Love Python'
# print(five.islower()) # True because it is a lowercase letter
# print(six.islower()) # False because it is not a lowercase letter

# ! identifier

# seven = "osama_elzero"
# eight = "OsamaElzero100"
# nine = "Osama--Elzero100"
# print(seven.isidentifier())# True because it is a valid identifier and contains only alphabetic characters and underscores
# print(eight.isidentifier())# True because it is a valid identifier and contains only alphabetic characters and numbers
# print(nine.isidentifier())# False because it is not a valid identifier because it contains special characters

# ! isalpha

# ten = "Hello"
# print(ten.isalpha())# True `because` it is a valid identifier and contains only alphabetic characters
# eleven = "Hello World2"
# print(eleven.isalpha())# False `because` it contains a space and a number

# ! isalnum

# twelve = "123456"
# print(twelve.isalnum())# True because it is a valid identifier and contains only numeric characters
# thirteen = "123456a"
# print(thirteen.isalnum())# True because it is a valid identifier and contains only numeric and alphabetic characters

# ! isnumeric
# fourteen = "123456"
# print(fourteen.isnumeric())# True because it is a valid identifier and contains only numeric characters
# fifteen = "123456a"
# print(fifteen.isnumeric())# False because it contains a letter and it is not a valid identifier

# ! replace
# a = "Hello World!"
# print(a.replace("l", "Hi")) # Hi World! replace a substring with another substring
# print(a.replace("l", "Hi" , 1)) # Hi World! replace a substring with another substring only the first occurrence of 'l' with 'Hi'

# ! join
# b = ["Hello", "World!"]
# print(" ".join(b)) # Hello World! join the elements of a list with a string # output: Hello World! join the elements of a list with a string
# print(type(" ".join(b))) # <class 'str'> return the type of the object


# ! streng formatting
# name = "Osama"
# age = 36
# rank = 10
# print("My Name is %s and my age is %d and my rank is %.2f"%(name, age, rank)) # My Name is Osama and my age is 36 and my rank is 10.000000
# # %s is string %d is num %f is float( .2 to control how many num add in float ) %.7s used to control how many characters to print from the string

# print("My Name is " + name + " and my age is " + str(age) + " and my rank is " + str(rank)) # My Name is Osama and my age is 36 and my rank is 10

# print("My Name is {} and my age is {:d} and my rank is {:.2f}".format(name, age, rank)) # My Name is Osama and my age is 36 and my rank is 10.00

# print("My Name is {0} and my age is {1} and my rank is {2:.2f}".format(name, age, rank)) # My Name is Osama and my age is 36 and my rank is 10.00
#  #{2:.2f} the first number is the index of the argument in the format method, and the second number is the number of decimal places to display

# print("My Name is {n} and my age is {a} and my rank is {r}".format(n=name, a=age, r=rank)) # My Name is Osama and my age is 36 and my rank is 10

# print(f"My Name is {name} and my age is {age} and my rank is {rank:.2f}") # My Name is Osama and my age is 36 and my rank is 10.00

# my_mony = 108141474414
# print(f"My Name is {name:.2s} and my age is {age} and my rank is {rank} and my money is {my_mony:,d}") # My Name is Osama and my age is 36 and my rank is 10 and my money is 1,081,414,744,147


# ! nunmbers
# x = 10+5j
# print(f"real is {x.real} and imaginary is {x.imag}")

# you convert from int to float by using float() function and from float to int by using int() function

# can not convert complex numbers to int or float

# ! arithmetic operators
# [+,-,*,/,%,**,// ]

# print(float(10+5)) # 15.0
# print(10-5) # 5
# print(10*5) # 50
# print(4+7*10) # 74 since multiplication has higher precedence than addition
# print(type(10/5)) # 2.0 class 'float' because division always returns a float
# print(int(10/5)) # 2 class 'int' because we converted the float to int
# print(10%5) # 0
# print(9%5) # 4 search for the remainder of the division
# print(10**5) # 100000
# print(10//5) # 2 returns the integer part of the division and discards the remainder if not acceptable the result will be rounded down to the nearest integer
# print(9//5) # 1 returns the integer part of the division and discards the remainder if not acceptable the result will be rounded down to the nearest integer


# ! list
# list is a collection of items that are ordered and changeable. Allows duplicate members.
# list is defined by square brackets []
# list are ordered , to use index to access the elements of the list
# list are changeable , we can change, add, and remove items in a list after it has been created
# list allows duplicate members, meaning that we can have items with the same value in a list are not unique
# list can have different data types, meaning that we can have items with different data types in a list

# my_list = [1, 2, 3, 4, 5]
# print(my_list) # [1, 2, 3, 4, 5]

# print(my_list[2]) # 3

# print(my_list[-1]) # 5 (accessing the last element)

# print(my_list[2:4]) # [3, 4] (accessing a range of elements)

# my_list[2] = 10
# print(my_list) # [1, 2, 10, 4, 5] (changing an element)

# my_list[2] = [10, 20, 30]
# print(my_list) # [1, 2, [10, 20, 30]] (adding elements)

# my_list[2:3] = []
# print(my_list) # [1, 2, 4, 5] (removing an element)

# my_list[2:3] = [10, 20]
# print(my_list) # [1, 2, 10, 20, 5] (editing elements)

# ! list methods

# my_list = [1, 2, 3, 4, 5]

# my_list_old = [10, 9, 8, 7, 6]

# my_list.append(6)
# print(my_list) # [1, 2, 3, 4, 5, 6] (adding an element to the end)


# my_list.append(my_list_old)
# print(my_list) # [1, 2, 15, 4, 5, 6, 7, 8, 9, [10, 9, 8, 7, 6]] (adding a list to the end)

# print(my_list[-1]) # [10, 9, 8, 7, 6] (accessing the last element which is a list)

# print(my_list[-1][0]) # 10 (accessing the first element of the last element which is a list)

# print(my_list[-1][1]) # 9 (accessing the second element of the last element which is a list)


# my_list.extend(my_list_old)
# print(my_list) # [1, 2, 15, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6] (adding all elements of a list to the end)
# my_list.extend([7, 8, 9])
# print(my_list) # [1, 2, 15, 4, 5, 6, 7, 8, 9] (adding multiple elements to the end)


# a = [1,2,3,4,5,'resha',6,7,8,9,10]
# a.remove(5)
# print(a) # [1, 2, 3, 4, 'resha', 6, 7, 8, 9, 10] (removing an element by value)
# # in remove if element doble it will remove the first one only


# f = [10, 9, 8, 7, 6]
# f.sort()
# print(f) # [6, 7, 8, 9, 10] (sorting the list in ascending order) not accessible for string and complex numbers
# f.sort(reverse=True)
# print(f) # [10, 9, 8, 7, 6] (sorting the list in descending order)


# z = [10,3,4,1,'resha',6,]
# z.reverse() # accessible for string and complex number
# print(z) # [ 6, 'resha', 1, 4, 3, 10] (reversing the list)


# my_list.insert(2, 15)
# print(my_list) # [1, 2, 15, 4, 5, 6] (adding an element at a specific index) before the index


# a = [1,2,3,4,6,7]
# a.clear() # [] (removing all elements from the list)
# print(a)

# b = [1,2,3,4,6,7]
# b.copy() # [1, 2, 3, 4, 6, 7] (creating a copy of the list)
# c = b.copy()

# print(c+b) # [1, 2, 3, 4, 6, 7, 1, 2, 3, 4, 6, 7] (adding the copy to the original list)
# print(f"{b} {c}") # [1, 2, 3, 4, 6, 7] [1, 2, 3, 4, 6, 7]


# d = [1,2,3,4,6,7]
# d.copy() # [1, 2, 3, 4, 6, 7] (creating a copy of the list)
# g = d.copy() # shallow copied if change of list after copied not save the change
# d.append(0) # change the list after copied not save the change
# print(d)
# print(g)


# d = [1,2,3,4,6,7]
# print(d.count(1))

# d = [1,2,3,4,6,7]
# print(d.index(4))

# ! tuple

# tuple is a collection of items that are ordered and unchangeable. Allows duplicate members.
# tuple is defined by parentheses ()
# tuple are ordered, to use index to access the elements of the tuple
# tuple are unchangeable, we cannot change, add, or remove items in a tuple after it has been created
# tuple allows duplicate members, meaning that we can have items with the same value in a tuple are not unique
# tuple can have different data types, meaning that we can have items with different data types in a tuple

# mytuple = (1, 2, 3, 4, 5)
# mytupletwo = 1, 2, 3, 4, 5 # if tuple contain only one element we must add a comma after the element to define it as a tuple
# print(mytuple) # (1, 2, 3, 4, 5)
# print(type(mytuple)) # (1, 2, 3, 4, 5) class 'tuple'
# print(mytupletwo) # (1, 2, 3, 4, 5)
# print(type(mytupletwo)) # (1, 2, 3, 4, 5) class 'tuple'
# print(mytuple[2]) # 3

#                                                        #tuple methods
# mytuple = (1, 2, 3, 4, 5)
# mytupletwo = 1, 2, 3, 4, 5
# c = mytuple + mytupletwo
# print(c) # (1, 2, 3, 4, 5, 1, 2, 3, 4, 5) (adding two tuples together)

# print (c.count(1)) # 2 (counting the number of occurrences of an element in a tuple)

# print(f"{mytuple}{mytupletwo}") # (1, 2, 3, 4, 5)(1, 2, 3, 4, 5) (adding two tuples together)

# tuple destruction

# a = ("resha", "mahmoud", "elsayed" , "mahmoud")
# b, c, d , _ = a
# print(b) # resha
# print(c) # mahmoud
# print(d) # elsayed

# ! set
# set is a collection of items that are unordered and unindexed. No duplicate members.
# set is defined by curly braces {}
# set are unordered, meaning that the items in a set do not have a defined order and cannot be accessed by index
# set are unindexed, meaning that the items in a set do not have a defined order and cannot be accessed by sclicing
# set do not allow duplicate members, meaning that we cannot have items with the same value in a set are not unique
# set can have different data types, meaning that we can have items with different data types in a set

# setis = {1, 2, 3, 4, 5}
# setistwo = {1, 2, 3, 4, 5, 5, 5, 5, 5, 5} # if set contain duplicate elements it will remove the duplicates and keep only one element
# print(setis) # {1, 2, 3, 4, 5}
# print(setistwo) # {1, 2, 3, 4, 5} (removing duplicates)

# ! set methods

# ! clear ()

# setis = {1, 2, 3, 4, 5}
# setistwo = {1, 2, 3, 4, 5, 5, 5, 5, 5, 5 , 6, 7, 8, 9, 10} # if set contain duplicate elements it will remove the duplicates and keep only one element
# setis.clear()
# print(setis) # set() (clearing the set)

# ! union ()

# print(setis.union(setistwo)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} (combining two sets and removing duplicates)
# print(setistwo | setis) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} (combining two sets and removing duplicates)

# ! add ()

# d = {1, 2, 3, 4, 5}
# d.add(6) # add can only add one element at a time and it will not add duplicates
# print(d) # {1, 2, 3, 4, 5, 6} (adding an element to the set)

# ! remove()

# g = {1, 2, 3, 4}
# g. remove(1)
# # g. remove(7)
# print (g)

# ! discard()

# h = {1, 2, 3, 4}
# h.discard(1) # remove the element from the set
# h.discard(7)
# print(h)

# ! pop()
# i = {1, 2, 3, 4}
# i.pop() # remove a random element from the set and return it
# print(i) # {2, 3, 4} (removing a random element from the set)

# ! update()
# p = {1, 2, 3, 4}
# print(p.update({5, 6, 7})) # add multiple elements to the set


# ! difference()

# a = {1, 2, 3 , 4}
# b = {3, 4, 5, 6}
# print(a.difference(b)) # {1, 2} (returning the elements that are in set a but not in set b) you can do it with the syntax minus sign also a-b
# print(b.difference(a)) # {5, 6} (returning the elements that are in set b but not in set a)

# ! difference_update()

# c = {1, 2, 3 , 4}
# j= {3, 4, 5, 6}
# print(c)
# c.difference_update(j) # {1, 2} (removing the elements that are in set j from set c) and it will update the set c to be the difference of the two sets
# print(c)

# ! intersection()

# q = {1, 2, 3 , 4}
# w = {3, 4, 5, 6}
# print(q)
# print(q.intersection(w)) # {3, 4} (returning the elements that are in both sets) you can do it with the syntax ampersand also q&w
# print(q) # {1, 2, 3, 4} (the set q is not changed because the intersection method does not update the set)

# ! intersection_update()

# print(q) # {1, 2, 3, 4}
# q.intersection_update(w) # {3, 4} (keeping only the elements that are in both sets) and it will update the set q to be the intersection of the two sets
# print(q) # {3, 4} (the set q is changed because the intersection_update method updates the set)

# ! symmetric_difference()

# i = {1, 2, 3, 4, 5, "X"}
# j = {"Osama","Zero", 1, 2, 4}
# print(i)
# print (i.symmetric_difference(j)) # i^j keeping only the elements that are in either set but not in both) and it will return a new set with the symmetric difference of the two sets
# print(i)


# print("X" *40)


# ! symmetric_difference_update())

# a = {1, 2, 3, 4, 5, "X"}
# x = {"Osama","Zero", 1, 2, 4}
# print(a)
# a.symmetric_difference_update(x) # a ^ x (keeping only the elements that are in either set but not in both) and it will update the set a to be the symmetric difference of the two sets
# print(a)

# ! issuperset()

# a = {1, 2, 3, 4, 5}
# b = {1, 2, 3}
# print(a.issuperset(b)) # True (checking if set a contains all elements of set b)


# print("#" *40)

# ! issubset()

# s = {1, 2, 3, 4, 5}
# d = {1, 2, 3}
# print(s.issubset(d)) # False (checking if set s is a subset of set d)


# ! isdisjoint()

# g = {1, 2, 3, 4}
# h = {1, 2, 3}
# i = {10, 11, 12}
# print(g.isdisjoint(h)) # False
# print(g.isdisjoint(i)) # True


# ! dictionary

# dictionary is a collection of items that are unordered, changeable and indexed. No duplicate members
# dictionary is defined by curly braces {}
# dictionary are unordered, meaning that the items in a dictionary do not have a defined order and cannot be accessed by index
# dictionary are changeable, meaning that we can change, add, and remove items in a dictionary after it has been created
# dictionary are indexed, meaning that the items in a dictionary have a defined order and can be accessed by key
# dictionary do not allow duplicate members, meaning that we cannot have items with the same key in a dictionary are not unique
# dictionary can have different data types, meaning that we can have items with different data types in a dictionary
# dictionary are defined by key-value pairs, where each key is unique and maps to a value


# user = {
#       "name": "Osama",
#       "age": 36,
#       "country": "Egypt",
#       "skills": ["HTML", "CSS", "JavaScript", "Python"],
#       "is_married": False
# }
# print(user) # {'name': 'Osama', 'age': 36, 'country': 'Egypt', 'skills': ['HTML', 'CSS', 'JavaScript', 'Python'], 'is_married': False}
# print(user["name"]) # Osama (accessing the value of the key "name")
# print(user.get ( "age")) # 36 (accessing the value of the key "age"
# print(user.keys()) # dict_keys(['name', 'age', 'country', 'skills', 'is_married']) (returning a list of all the keys in the dictionary)
# print(user.values()) # dict_values(['Osama', 36, 'Egypt', ['HTML', 'CSS', 'JavaScript', 'Python'], False]) (returning a list of all the values in the dictionary)

# ! two dimensional dictionary
# languages = {
#     "HTML": {
#         "level": "beginner",
#         "duration": "3 months"
#     },
#     "CSS": {
#         "level": "intermediate",
#         "duration": "4 months"
#     }
# }
# print(languages) # {'HTML': {'level': 'beginner', 'duration': '3 months'}, 'CSS': {'level': 'intermediate', 'duration': '4 months'}}
# print(languages["CSS"] ) # {'HTML': {'level': 'beginner', 'duration': '3 months'}, 'CSS': {'level': 'intermediate', 'duration': '4 months'}}
# print(languages["CSS"]["level"]) # intermediate (accessing the value of the key "level" in the dictionary "CSS")
# print(languages.get("HTML").get("duration")) # 3 months (accessing the value of the key "duration" in the dictionary "HTML")
# print(len(languages)) # 2 (returning the number of items in the dictionary)
# print(len(languages["HTML"])) # 2 (returning the number of items in the dictionary "HTML")


# framework1 = {
#     "name" : "Django",
#       "language" : "Python",
# },
# framework2 = {
#     "name" : "Laravel",
#     "language" : "PHP"
# } ,
# framework3 = {
#     "name" : "React",
#     "language" : "JavaScript"
# }

# allframeworks = {

#     "framework1" : framework1,
#     "framework2" : framework2,
#     "framework3" : framework3
# }
# print(allframeworks) # {'framework1': {'name': 'Django', 'language': 'Python'}, 'framework2': {'name': 'Laravel', 'language': 'PHP'}, 'framework3': {'name': 'React', 'language': 'JavaScript'}}
# print(allframeworks["framework1"]["name"]) # Django (accessing the value of the key "name" in the dictionary "framework1")


# ! dic methods

# ! clear()
# user = {
#       "name": "Osama",
#       }
# print(user) # {'name': 'Osama'}
# user.clear() # None (removing all items from the dictionary)
# print(user) # {} (the dictionary is now empty)

# ! update()

# membar = {
#     "name": "Osama",

# }
# print(membar) # {'name': 'Osama', 'age': 36}
# membar.update( {"age": 36}) # add a new key-value pair to the dictionary
# print(membar) # {'name': 'Osama', 'age': 36} (adding a new key-value pair to the dictionary)


# ! copy ()

# main = {
#     "name": "Osama",
# }
# print(main) # {'name': 'Osama'}
# secondary = main.copy() #  (creating a copy of the dictionary)
# print(secondary) # {'name': 'Osama'} (the copy is identical to the original dictionary)
# main.update({"age": 36}) # add a new key-value pair to the original dictionary
# print(main) # {'name': 'Osama', 'age': 36} (the original dictionary has been updated)
# print(secondary) # {'name': 'Osama'} (the copy remains unchanged)


# ! setdefault()
# user = {
#       "name": "Osama",
#       "age": 36,
#       "country": "Egypt"
# }
# print(user) # {'name': 'Osama', 'age': 36, 'country': 'Egypt'}
# user.setdefault("skills", ["HTML", "CSS", "JavaScript"]) # add a new key-value pair to the dictionary if the key does not exist
# print(user) # {'name': 'Osama', 'age': 36, 'country': 'Egypt', 'skills': ['HTML', 'CSS', 'JavaScript']} (the new key-value pair has been added)
# user.setdefault("age", 40) # does not change the value of the key "age" because it already exists
# print(user) # {'name': 'Osama', 'age': 36, 'country': 'Egypt', 'skills': ['HTML', 'CSS', 'JavaScript']} (the value of the key "age" remains unchanged)

# ! popitem()
# user2 = {
#       "name": "Osama",
#       "age": 36,
#       "country": "Egypt"
# }
# print(user2) # {'name': 'Osama', 'age': 36, 'country': 'Egypt'}
# user2.update({"skills": "c"})
# print(user2.popitem()) # return ('skills', 'c')

# ! ITEMS ()
# view ={
#     "name": "Osama", # key of the dictionary
# }

# allview = view.items()
# print(view)
# view ["age"] = 36
# print(allview)


# ! fromkeys ()
# a = ("key0" , "key1" , "key2") # keys of the new dictionary if not specified the keys will be None by default
# b = "x" # value of the keys in the new dictionary if not specified the value will be None
# print(dict.fromkeys (a,b )) # {'key0': 'x', 'key1': 'x', 'key2': 'x'} (creating a new dictionary with the keys from the tuple and the value from the variable b)

# ! boolean()
# in programming we use boolean to check if a condition is true or false
# boolean is a data type that can be either True or False

# name = "Osama"
# print(bool(name)) # True (because the name is not empty)
# name = "" # empty string
# print(bool(name)) # False (because the name is empty)
# name =[] # empty list
# print(bool(name)) # False (because the name is empty)
# name ={} # empty dictionary
# print(bool(name)) # False (because the name is empty)
# name =() # empty tuple
# print(bool(name)) # False (because the name is empty)
# name =0 # 0
# print(bool(name)) # False (because the name is 0)
# name =1 # 1
# print(bool(name)) # True (because the name is 1)

# ! boolean operators (and, or, not)

# and: returns True if both operands are True
# or: returns True if at least one operand is True
# not: returns the opposite of the operand

# age = 20
# country = "Egypt"
# if age > 18 and country == "Egypt":
#     print("You are an adult in Egypt")
# else:
#     print("You are not an adult in Egypt")

# if age > 21 or country == "Egypt":
#     print("You are an adult in Egypt")
# else:
#     print("You are not an adult in Egypt")

# print(not age > 21) # True (because the age is not greater than 21)
# print(not age > 21 and country == "Egypt") # False (because the age is not greater than 21 and the country is not Egypt)
# print(not age > 21 or country == "Egypt") # True (because the age is not greater than 21 or the country is Egypt)
# print(not age > 21 and country != "Egypt") # True (because the age is not greater than 21 and the country is not Egypt)
# print(not age > 21 or country != "Egypt") # False (because the age is not greater than 21 or the country is not Egypt)

# ! assignment operators (=, +=, -=, *=, /=, %=, **=, //=)
# =: assigns the value of the right operand to the left operand
# +=: adds the value of the right operand to the left operand and assigns the result to the left operand
# -=: subtracts the value of the right operand from the left operand and assigns the result to the left operand
# *=: multiplies the value of the right operand by the left operand and assigns the result to the left operand
# /=: divides the value of the right operand by the left operand and assigns the result to the left operand
# %=: divides the value of the right operand by the left operand and assigns the remainder to the left operand
# **=: raises the value of the left operand to the power of the right operand and assigns the result to the left operand
# //=: divides the value of the right operand by the left operand and assigns the result to the left operand

# x = 10 # value of x is 10
# y = 20 # value of y is 20
# x = x + y # x = x + y is the same as x += y
# x += y # x += y is the same as x = x + y
# print(x) # 30 (the value of x is now 30)
# x -= y # x -= y is the same as x = x - y
# print(x) # 10 (the value of x is now 10)
# x *= y # x *= y is the same as x = x * y
# print(x) # 200 (the value of x is now 200)
# x /= y # x /= y is the same as x = x / y
# print(x) # 10 (the value of x is now 10)
# x %= y # x %= y is the same as x = x % y
# print(x) # 0 (the value of x is now 0)
# x **= y # x **= y is the same as x = x ** y
# print(x) # 1000000 (the value of x is now 1000000)
# x //= y # x //= y is the same as x = x // y
# print(x) # 10 (the value of x is now 10)

# ! comparison operators (==, !=, >, <, >=, <=)

# ==: checks if the value of the left operand is equal to the value of the right operand
# !=: checks if the value of the left operand is not equal to the value of the right operand
# >: checks if the value of the left operand is greater than the value of the right operand
# <: checks if the value of the left operand is less than the value of the right operand
# >=: checks if the value of the left operand is greater than or equal to the value of the right operand
# <=: checks if the value of the left operand is less than or equal to the value of the right operand

# ! type conversion (int(), float(), str(), bool(), list(), tuple(), set(), dict())
# int(): converts the value to an integer
# float(): converts the value to a float
# str(): converts the value to a string
# bool(): converts the value to a boolean
# list(): converts the value to a list
# tuple(): converts the value to a tuple
# set(): converts the value to a set
# dict(): converts the value to a dictionary

# a = 10
# print(type(a)) # <class 'int'> (the type of a is int)
# print(type(str(a))) # <class 'str'> (the type of the value of a is now str)

# b = 10.5
# print(type(b)) # <class 'float'> (the type of b is float)
# print(type(int(b))) # <class 'int'> (the type of the value of b is now int)

# c = "10"
# print(type(c)) # <class 'str'> (the type of c is str)
# print(type(str(c))) # <class 'str'> (the type of the value of c is now str)

# d = True
# print(type(d)) # <class 'bool'> (the type of d is bool)
# print(type(float(d))) # <class 'bool'> (the type of the value of d is now bool)

# e = [1, 2, 3]
# print(type(e)) # <class 'list'> (the type of e is list)
# print(type(tuple(e))) # <class 'tuple'> (the type of the value of e is now tuple)

# f = (1, 2, 3)
# print(type(f)) # <class 'tuple'> (the type of f is tuple)
# print(type(list(f))) # <class 'list'> (the type of the value of f is now list)

# g = {1, 2, 3}
# print(type(g)) # <class 'set'> (the type of g is set)
# print(type(dict(g))) # <class 'dict'> (the type of the value of g is now dict)

# h = {"name": "Osama", "age": 36}
# print(type(h)) # <class 'dict'> (the type of h is dict)
# print(type(list(h))) # <class 'list'> (the type of the value of h is now list)


# input() used to user enter input
# name = input("Enter your name: ")
# # name = name.strip().capitalize()
# print(f"Hello {name.strip().capitalize():.2s}") # Hello Os being used to print the name in a specific format

# ! Email sclice [start:stop:step]
# email = "osama@gmail.com"
# # print(len(email))  # 15
# print(
#     f"{email.capitalize()[0 : email.index('@')]:.2}"
# )  # Os (capitalize the first letter of the email)
# print(
#     f"{email.capitalize()[email.index('@') + 1 :: 2]}"
# )  # gmail (capitalize the first letter of the email)
# print(email[6:11])  # gmail
# print(email[12:18])  # com

# practice your age full details

# age = int(input("Enter your age:").strip()) # strip the white space from the end and beginning of the string
# print(age)
# print(type(age))

# # get age in all time units

# month = age * 12
# week = month * 4
# day = week * 7
# hour = day * 24
# minute = hour * 60
# second = minute * 60
# print(f"{age} years is\n{month} months\n{week:,} weeks\n{day:,} days\n{hour:,} hours\n{minute:,} minutes\n{second:,} seconds")

# ! Control flow if and elif and else
# make a program that asks the user to enter a number and prints whether the number is positive, negative, or zero

# uname = "resha"
# isstudent = input("Are you a student or not: ")
# print(f"You are a student: {isstudent}")
# ucountry = input("Enter your country: ")
# print(f"Your country is {ucountry}")
# cname = "python"
# cprice = 100
# cdiscount = 10

# print(f"Your name is {uname} and course name is \"{cname}\" and your price is {cprice} and your discount is {cdiscount}")
# print(f"course after discount is {cprice - cdiscount}")

# if ucountry == "Egypt" or ucountry == "KSA":

#     print(f"Your name is {uname} and course name is \"{cname}\" " )

#     if isstudent == "yes":

#         print(f"course price after discount is: ${cprice - 90}") # 90 is the discount price of Egypt output the price after discount is 10

#     else:
#      print(f"course price after discount is: ${cprice - 80}") # 80 is the discount price of Egypt output the price after discount is 20

# elif ucountry == "USA":

#      print(f"Your name is {uname} and course name is \"{cname}\" " )

#      if isstudent == "yes":

#          print(f"course price after discount is: ${cprice - 77}") # 77 is the discount price of USA output the price after discount is 23

#      else:

#       print(f"course price after discount is: ${cprice - 70}") # 70 is the discount price of USA output the price after discount is 30

# else:
#      print(f"Your name is {uname} and course name is \"{cname}\" " )

#      if isstudent == "yes":

#         print(f"course price after discount is: ${cprice -74}") # 74 is the discount price of KSA output the price after discount is 26

#      else:

#       print(f"course price after discount is: ${cprice - 10}") # 10 is the discount price of KSA output the price after discount is 90

# elif ucountry == "KSA":
#      print(f"Your name is {uname} and course name is \"{cname}\" " )
#      print(f"course price after discount is {cprice - 80}") # 80 is the discount price of KSA output the price after discount is 20


# ! Ternary conditional operator

# cuontary = input("Enter your country: ")

# if cuontary == "Egypt":
#    print(f"tha weather is sunny in {cuontary}")

# elif cuontary == "USA":
#     print(f"tha weather is rainy in {cuontary}")

# else:
#     print(f"tha weather is cloudy in {cuontary}")


# mobvis_rate = 10
# age = 20
# if age > mobvis_rate:

#     print("You are an adult in Egypt") # print the statement if the age is greater than the mobvis rate

# else:

#     print("You are not an adult in Egypt") # print the statement if the age is less than the mobvis rate


# ! short if

# print("You are an adult in Egypt" if age > mobvis_rate else "You are not an adult in Egypt")


# ! practice your age full details advanced

# print("you can use the following units of time: year, month, week, day, hour, minute, second or y, m, w, d, h, min, s")
# age = int(input("Enter your age:").strip()) # strip the white space from the end and beginning of the string

# # get age in all time units

# unit = input("Enter the unit of time: ").strip().lower() # lower the case of the unit of time of all the letters

# # get age in all time units

# month = int(age * 12)
# week = month * 4
# day = int(age) * 365
# hour = day * 24
# minute = hour * 60
# second = minute * 60

# if unit == "year" or unit == "y":
#     print(f"{age} years")

# elif unit == "month" or unit == "m":
#     print(f"{month} months")

# elif unit == "week" or unit == "w":
#     print(f"{week} weeks")

# elif unit == "day" or unit == "d":
#     print(f"{day:,} days")

# elif unit == "hour" or unit == "hr":
#     print(f"{hour:,} hours")

# elif unit == "minute" or unit == "min":
#     print(f"{minute:,} minutes")

# elif unit == "second" or unit == "s":
#     print(f"{second:,} seconds")

# else:
#     print("Invalid unit of time")


# ! mambership operator used to idetfy if a value is in a list

# name = "Mahmoud Elsayed"
# print("s" in name) # True
# print("a" not in name) # False
# print("a" in name.lower()) # True
# print("a" in name.upper()) # False
# print("a" in name.capitalize()) # True
# print("a" in name.title()) # False
# print("a" in name.strip()) # True


# ! list

# frinds = ["Mahmoud", "Elsayed", "Mahmoud"]
# print("Mahmoud" in frinds) # True
# print("Mahmoud" not in frinds) # False


# !  using in and not in with conditions
# name = "Mahmoud"
# if name in frinds :
#     print("name is in the list")
# else:
#     print("name is not in the list")

# name = "resha"
# if name not in frinds :
#     print("name is not in the list")
# else:
#     print("name is in the list")

# ! membership operator practical example

# list contain admins

# admins = ["Mahmoud", "Elsayed", "Mahmoud"]

# # login
# username = input("Enter your username: ").strip().capitalize()
# password = input("Enter your password: ").strip().lower()

# if username in admins and password == "admin":
#     print(f"Hello {username} Welcome to the admin panel")
#     options = input("delete user, add user or exit: ").strip().lower()
#     print(options)
#     if options == "delete user":
#         print("Enter the username you want to delete: ")
#         username = input().strip().capitalize()
#         if username in admins:
#             admins.remove(username)
#             print(f"User {username} has been deleted")
#             print(f"the new list after deletion is {admins}")
#         else:
#             print("User not found")
#     elif options == "add user":
#         print("Enter the username you want to delete: ")
#         username = input().strip().capitalize
#         if username in admins:
#             print("User already exists")
#         else:
#             admins.append(username)
#             print(f"User {username} has been added")
#             print(f"the new list after addition is {admins}")
#     elif options == "exit":
#         print("Thank you for using the admin panel")
# else:
#     print("Invalid username or password")


# ! while loop

# a = 0
# while a < 5:
#     print(a)
#     a += 1  # a = a + 1
#     while a <= 10:
#         print(a)
#         a += 1  # a = a + 1
# print("a is greater than 10")

# a = 0
# while a < 5:
#     print(a)
#     a += 1  # a = a + 1
#     while True:
#         print("Hello World!")
#         break

# myf = ["a", "b", "c", "d", "e", "f", "g", "h"]

# print(len(myf))

# A = 0
# while A < len(myf):  # num of objects greater than the number of indexes by one
#     print(
#         f"@{str(A + 1).zfill(2)} is {myf[A]}"
#     )  # print the index and the value of the list
#     A += 1
# else:
#     print("all friends print")

# my_favourite_webs = []

# maxweb = 6

# while len(my_favourite_webs) < maxweb:
#     print("Enter the name of the web: ")
#     web = input().strip().capitalize()
#     if web in my_favourite_webs:
#         print("Web already exists")
#     else:
#         my_favourite_webs.append(web)
#         print(f"Web {web} has been added")
#         print(f"the new list after addition is {my_favourite_webs}")  # print the list

# option = input("Add Or No").strip().capitalize()
# print(option)
# if option == "Add":
#     print("Enter the name of the web: ")
#     web = input().strip().capitalize()
#     if web in my_favourite_webs:
#         print("Web already exists")
#     else:
#         my_favourite_webs.append(web)
#         print(f"Web {web} has been added")
#         print(
#             f"the new list after addition is {my_favourite_webs}"
#         )  # print the list


# Tries = 4
# thepass = "resha@123"
# input_pass = input("Enter your pass")
# while input_pass != thepass:
#     Tries -= 1
#     print(f"Wrong pass You have , {'last try' if Tries == 0 else Tries} tries left")
#     input_pass = input("Enter your pass")
#     if Tries == 0:
#         print("You have tried too many times")
#         break
# else:
#     print("You have entered the correct pass") # THE DIFFERENCE bwtween print after while and else print after while will print when con trup or false but
# else print when con is true


# ! for loop
# item is the variable that will be used to access the elements of the list
# item is avirable you create and call it when you want to use it


# mynums = [1, 2, 3, 4, 5]

# for item in mynums:
#     if item % 2 == 0:
#         print(item, "is even")
#     else:
#         print(item, "is odd")
# # for loop with range
# for item in range(1, 6):
#     print(item)

# myname = "Resha"
# for item in myname:
#     print(f" [ {item.upper()} ] ")

# loop for training

# mydic = {
#     "name": "Mahmoud",
#     "age": 36,
#     "country": "Egypt",
#     "skills": ["HTML", "CSS", "JavaScript", "Python"],
#     "is_married": False,
# }
# print(mydic["name"])
# print(mydic.get("age"))
# for info in mydic:
#     print(info)
#     print(f"the value of {info} is {mydic[info]}")

# nasted for loop

# people = ["Mahmoud", "Elsayed", "Mahmoud"]

# skills = ["HTML", "CSS", "JavaScript", "Python"]

# for person in people:
#     print(f"person is {person}")
#     for skill in skills:
#         print(f"person has {skill}")

# peoples = {
#     "Mahmoud": {
#         "HTML": "beginner",
#         "CSS": "intermediate",
#         "JavaScript": "advanced",
#     },
#     "Elsayed": {
#         "HTML": "advanced",
#         "CSS": "intermediate",
#         "JavaScript": "advanced",
#     },
#     "Saad": {
#         "HTML": "beginner",
#         "CSS": "intermediate",
#         "JavaScript": "advanced",
#     },
# }
# print(peoples["Mahmoud"])
# print(peoples["Mahmoud"]["HTML"])
# print(peoples["Saad"]["HTML"])
# print(peoples["Elsayed"]["CSS"])
# for person in peoples:
#     # print(f"person is {person} and his skills are {peoples[person]}")
#     print(f"person is {person}")
#     for skill in peoples[person]:
#         print(f"person has {skill} and his level is {peoples[person][skill]}")


# ! break continue pass

# num = [1, 2, 3, 4, 5, 9, 10, 11, 12, 14, 15]
# for i in num:
#     if i == 12:  # continue stope the curent itiration and continue the next one dont run enything after the continue in the iteration
# continue # continue the next iteration of the loop
# break # break the loop and used to exit the loop
# pass # pass the current iteration of the loop and run enything after the pass in the iteration
# else:
#     print(i)

# ! loop advanced dict

# peoples = {
#     "Mahmoud": {
#         "HTML": "beginner",
#         "CSS": "intermediate",
#         "JavaScript": "advanced",
#     }
# }
# # for person in peoples:
# #     print(f"{person} has {peoples[person]}")

# for key,skill in peoples.items():
#     print(f"{key} has {skill}")


# peoples = {
#     "Mahmoud": {
#         "HTML": "beginner",
#         "CSS": "intermediate",
#         "JavaScript": "advanced",
#     },
#     "Elsayed": {
#         "HTML": "advanced",
#         "CSS": "intermediate",
#         "JavaScript": "advanced",
#     },
# }
# for key, value in peoples.items():
#     print(f"{key}")
#     for child_key, child_value in value.items():
#         print(f"{child_key} has {child_value}")


# ! function and return
# 1 a function is a block of code that performs a specific task
# 2 a function runs only once called it and returns a value
# 3 a function accepts elements as input to perform a specific task called parameters
# 4 a function can do the task without returning a value but it can return a value
# 5 a function create to prevent dry code and make the code more readable  DRY MEEN DONT REPEAT YOURSELF
# 6 a function can be called multiple times with different arguments
# 7 a function can take input arguments and return output
# 8 There is Built-in function in python and user defined function
# 9 a function is for all team and all project

# ! function parameter and argument

# a, c, d = "Mahmoud", "Elsayed", "Mahmoud"

# print(a)
# print(c)
# print(d)


# def say(name):
#     print(f"Hello {name}")


# def is function keyword to define a function
# say is the name of the function
# (name) is the parameter of the function
# say("resha")  # resha is the argument of the function


# say("resha")
# say(a)


# def add(a, b):
#     if type(a) != int or type(b) != int:
#         print("Error: Both arguments must be integers")
#     else:
#         print(f"The sum of {a} and {b} is {a + b}")


# add(10, "Mahmoud")
# add(10, 20)


# def fullname(firstname, middlename, lastname):
#     print(
#         f"Hello {firstname.strip().capitalize()} {middlename.upper().strip():.1s} {lastname.strip().capitalize()}"
#     )
#     # must be strip write in the first place scince the strip will remove the white space and capitalize will capitalize the first letter of the string


# fullname("  mahmoud  ", "  sayed  ", "  mahmoud  ")


# function packing and unpacking * args

# mylist = [1, 2, 3, 4, 5]
# print(mylist)
# print(*mylist) # the idea of unpacking is take the elements of the list and print them one by one out of the list
# print(*mylist, sep="  ")


# def say_hi(a, b, c, d):  # used * args to accept any number of arguments and print them one by one out of the list
#     people = [a, b, c, d]
#     for person in people:
#         print(f"Hello {person}")

# say_hi("Mahmoud", "Elsayed", "Mahmoud", "Elsayed")

# the up and down function is used to print the elements of the list but up the num of parameters is defined by the number of elements in the list
# can not increase the number of arguments because the parameters defined in the function must be the same as the number of elements in the list
# so we use the * to accept any number of arguments

# def say_hi(*people): # pepole here instead of people = [a, b, c, d] we use *people to accept any number of arguments

#     print(type(people))
#     print(people)

#     for person in people:
#         print(f"Hello {person}")


# say_hi("Mahmoud", "Elsayed", "Mahmoud", "Elsayed")


# def Show_Skills(Name, *args):  # def show_details (skilli, skill, skill3):
#      # print(f"Hello Osama Your Skills Is: ")
#     print(
#         f"The Skills Are {args}"
#     )  # print (f"(ski111)") print(f"(skill2}") print (f"{ski113)")

#     for arg in args:  # use arg to access the elements of the list and print them one by one out of the list
#         # print(f"The data is {arg}")
#         print(f"Hello {Name} The Skills Are {arg} and the type is {type(arg)}")


# Show_Skills("Mahmoud", "HTML", "CSS", "JavaScript", "Python")


# ! function default parameter


# def say_hi(
#     name, age=30, country="unknown"
# ):  # default vaule must be put in the end of the parameter
#     print(f"Hello {name} your age is {age} and your country is {country}")


# say_hi("Mahmoud")
# say_hi("Mahmoud", age=36)
# say_hi("Mahmoud", age=36, country="Egypt")

# ! pack and unpack argument for keword argument


# myskills = {
#     "HTML": "beginner",
#     "CSS": "intermediate",
#     "JavaScript": "advanced",
# }


# def show_data(
#     **kwargs,
# ):  # **kwargs must input of the function or must be the argument of the input is dictionary key and value

#     print(
#         f"The data is {kwargs}"
#     )  # parameters of the function and here sorted the key and value of the dictionary
#     for key, value in kwargs.items():# items() method used to access the key and value of the dictionary
#         print(f"{key} is {value}")


# show_data(name="Mahmoud", age=36, country="Egypt")
# show_data(**myskills)

# myskills = {
#     "HTML": "beginner",
#     "CSS": "intermediate",
#     "JavaScript": "advanced",
# }

# mytuple = ("HTML", "CSS", "JavaScript")


# def show_skills(name, *skills, **skillswithprog):

#     print(f"Hello {name} \nyour skills without prog are {skills}")
#     for skill in skills:
#         print(f"Hello {name}  your skills are {skill}")

#     print(f"Hello {name}  your skills with prog are {skillswithprog}")
#     for key, value in skillswithprog.items():
#         print(f"Hello {name}  your skills are {key} and the level is {value}")


# show_skills("Mahmoud", "HTML", "CSS", "JavaScript", Python="beginner")
# show_skills("Mahmoud", *mytuple, Python="beginner")
# show_skills("Mahmoud", *mytuple, **myskills)


# ! function scope


# from concurrent.futures import thread
# from itertools import count
# import json
# import numbers
# import threading
# from tkinter import ALL
# from typing import Counter, Protocol, Type

# import concurrent
# from grpc import Future
# from matplotlib.pylab import f


from multiprocessing import process
from pyclbr import Class
import random

from matplotlib.pylab import f


x = 1  # x is a global scope


# def one():
#     global x  # x is a global scope
#     x = 2
#     print(x, " x one is a local scope")


# def two():
#     x = 4
#     print(x, " x two is a local scope")


# print(x, " x is a global scope")
# one()
# two()
# print(x, " x is a global scope after calling the function one ")

# if i set the x to global scope in the function one the value of x will be changed in the function two
# if function one is called before function two the value of x will be changed if function two is no have x


# ! function recursion

# x = "wwwoooorld"
# print(x[1:])


# def clean(word):
#     if len(word) == 1:
#         return word
#     print(f"print start function {word}")
#     if word[0] == word[1]:
#         print(f"before return condition {word}")
#         return clean(word[1:])
#     print(f"before return return {word}")
#     return word[0] + clean(word[1:])
#     # stash [world] in a variable and return the first letter of the stashed variable


# print(clean("wwwooorrllddd"))


# ! function lambda

# it funcation no has name
# you can it call it inline without defining it
# you can use it in return data from another function
# lambda used for simple function and def handles more complex functions
# lambda is a function that is defined without a name
# lambda is one single line of code not a block of code
# lambda type is a function


# def say_hi(name, age):
#     return f"Hello {name} your age is {age}"


# hello = lambda name, age: f"Hello {name} your age is {age}"

# print(say_hi("Mahmoud", 36))
# print(hello("Mahmoud", age=37))
# print(hello.__name__)
# print(say_hi.__name__)
# print(type(hello))

# ! file handling
# "a" Append Open File For Appending, Values, Create File If Not Exists
# "r" Read [Default Value] Open File For Read and Give Error If File is Not Exists
# "w" Write Open File For Writing, Create File If Not Exists
# "x" Create Create File, Give Error If File Exists


# import os

# print("Current directory:", os.getcwd())

# print("File exists:", os.path.exists(r"C:\Users\Mahmoud Elsayed\Downloads\resah.txt"))

# print("Files in Downloads:")
# print(os.listdir(r"C:\Users\Mahmoud Elsayed\Downloads"))


# import os

# print(os.getcwd())  # current working directory

# print(os.path.dirname(os.path.abspath(__file__)))  # get the directory of the file

# print(os.path.abspath(__file__))  # get the absolute path of the file

# os.chdir("c:/Users/Mahmoud Elsayed/Downloads/")  # change the current working directory


# myfile = open(r"C:\Users\Mahmoud Elsayed\Downloads\resah.txt", "r")

# print(myfile.read())  # read all the file
# print(myfile.read(7))  # read all the file with a length of 7

# print(myfile.readline())  # read one line
# print(myfile.readline(7))  # read one line with a length of 7
# print(myfile.readline())  # read one line

# print(myfile.readlines())  # read all the lines output a list
# print(myfile.readlines(40))  # read all the lines with a length of 40
# print(type(myfile.readlines(7)))  # read all the lines with a length of 7

# for line in myfile:
#     print(line)
#     if line.startswith("07"):
#         break
# myfile.close()


# ! file handling part three write and append in file

# file = open(r"C:\Users\Mahmoud Elsayed\Downloads\mastering python\resha.txt", "w")
# file.write("01 Hello World!\n")
# file.write("02 Hello World! \n")
# file.close()

# file = open(r"C:\Users\Mahmoud Elsayed\Downloads\mastering python\fun.txt", "w")
# file.write("Elzero\n" * 10)
# file.close()

# mylist = [
#     "Elzero\n",
#     "Elzero",
#     "Elzero",
#     "Elzero",
#     "Elzero",
#     "Elzero",
#     "Elzero",
#     "Elzero",
#     "Elzero",
#     "Elzero",
# ]

# file = open(r"C:\Users\Mahmoud Elsayed\Downloads\mastering python\resha.txt", "w")
# file.writelines(mylist)

# ! THE DIFFERENCE bwtween w and a is that w will create a new file
# ! if the file does not exist and a will append the data to the file if the file exists
# ! a will not create a new file if the file does not exist

# file = open(r"C:\Users\Mahmoud Elsayed\Downloads\mastering python\resha.txt", "a")
# # file.write("\n01 Hello World!\n")
# # file.write("02 Hello World! \n")
# file.write("03 here is a new line\n")
# file.close()

# ! file handling part four inportant info

# file = open(r"C:\Users\Mahmoud Elsayed\Downloads\mastering python\resha.txt", "a")
# file.truncate(6) # truncate the file to the length of 6 I mean the file will be truncated to 6 characters and the rest of the characters will be deleted

# file = open(r"C:\Users\Mahmoud Elsayed\Downloads\mastering python\resha.txt", "a")
# print(file.tell()) # tell the current position of the cursor


# file = open(r"C:\Users\Mahmoud Elsayed\Downloads\mastering python\resha.txt", "r")
# file.seek(0) # move the cursor to the beginning of the file here or to the position is define
# file.read() # read all the file

# import os

# os.remove(r"C:\Users\Mahmoud Elsayed\Downloads\mastering python\resha.txt") # delete the file


# ! built-in function
# all ()
# any ()
# bin ()
# id ()

# x = [1, 2, 3, 4, 5, []]
# x = [1, 2, 3, 4, 5, 6]
# if all(x): # all() return True if all element of the list is true
#     print("all elements are true")
# else:
#     print("at least one element is false")

# x = [1, 2, 3, 4, 5, []]
# x = [0, 0, []]
# if any(x): # any() return True if any element of the list is true
#     print("at least one element is true")
# else:
#     print("all elements are false")


# print(bin(10)) # return the binary representation of the number


# a = 10
# b = 20

# print(id(a))  # return the memory address of the variable
# print(id(b))  # return the memory address of the variable

# ! built-in function part two

# sum() (itarable , start) itarable is the list or tuple and start is the index of the first element of the list
# round() (number, ndigits) number is the number to be rounded and ndigits is the number of decimal places
# range() (start, stop, step) start is the index of the first element of the list, stop is the index of the last element of the list and step is the step of the list
# print()

# a = [1, 2, 3, 4, 5]

# print(sum(a))  # return the sum of the elements of the list = 15
# print(
#     sum(a, start=1)
# )  # return the sum of the elements of the list starting meen add one to the list = 16

# print(
#     sum(a, 2)
# )  # return the sum of the elements of the list starting meen add two to the list = 17

# print(round(10.51))  # return the number rounded to the nearest integer = 11

# print(
#     round(140.566, 2)
# )  # return the number rounded to the nearest integer with two decimal places = 140.57

# print(
#     round(140.566, 3)
# )  # return the number rounded to the nearest integer with three decimal places = 140.566


# print(list(range(0)))  # return the list of the numbers from 0 to 0 = 0

# print(
#     list(range(10))  # start and step by default is 0 and the end must be specified
# )  # return the list of the numbers from 0 to 9 = 0 1 2 3 4 5 6 7 8 9

# print(
#     list(
#         range(0, 20, 2)
#     )  # return the list of the numbers from 0 to 19 with a step of 2
# )  # return the list of the numbers from 0 to 19 with a step of 2 = 0 2 4 6 8 10 12 14 16 18


# print("Hello World!")  # default seperator is space in print
# print("Hello", "World!", sep=" | ")  # seperator is |

# print("first line", end="\n")  # end is the new line character default is \n
# print("second line", end="\t")  # end now is the tab character
# print("third line", end=" its me ")  # end now is the string its me
# print("fourth line")  # end now is the new line character

# ! built-in function part three

# abs() (number) return the absolute value of the number the distance from zero
# pow() (number, power, modulo) return the number raised to the power of the number and the modulo
# min() (iterable) return the smallest element of the iterable
# max() (iterable) return the largest element of the iterable
# slice() (iterable, start, stop, step) return the elements of the iterable starting meen the index of the first element of the list,
# stop is the index of the last element of the list and step is the step of the list you wont to skip


# print(abs(-10))  # return the absolute value of the number the distance from zero = -10
# print(abs(10))  # return the absolute value of the number the distance from zero = 10
# print(
#     abs(108.19)
# )  # return the absolute value of the number the distance from zero = 108.5
# print(
#     abs(-108.19)
# )  # return the absolute value of the number the distance from zero = 108.5


# print(pow(2, 3))  # return the number raised to the power of the number = 8 2*2*2

# print(
#     pow(2, 0.5)
# )  # return the number raised to the power of the number = 1.4142135623730951

# print(pow(2, 10))  # return the number raised to the power of the number = 1024

# print(
#     pow(2, 10, 3)
# )  # return the number raised to the power of the number = 3 2*2*2*2*2*2*2*2*2*2 mod = 3

# Mynums = [1, 2, 3, 4, 5]

# print(min(1, 40, 3, -30))  # return the smallest element of the iterable = 1
# print(min("A", "B", "C", "D"))  # return the smallest element of the iterable = A

# print(min(Mynums))  # return the smallest element of the iterable = 1
# print(min(Mynums, key=abs))  # return the smallest element of the iterable = 1 abs meen absolute value of the element in the list
# print(min(Mynums, key=len))  # return the smallest element of the iterable = 1 len meen length of the element in the list


# print(max(1, 40, 3, -30))  # return the largest element of the iterable = 40
# print(max("A", "B", "C", "D"))  # return the largest element of the iterable = D

# Mynums = [1, 2, 3, 4, 5]

# print(max(Mynums))  # return the largest element of the iterable = 5

# sclist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(
#     sclist[0:2]
# )  # return the elements of the list from the index 0 to the index 2 = [1, 2]
# print(
#     sclist[2:-1:2]
# )  # return the elements of the list from the index 2 to the index 4 with a step of 2 = [3, 5]

# print(sclist[slice(2, 4)])
# # return the elements of the list from the index 2 to the index 4 = [3, 4] here end must be specified


# ! built-in function part four Map
# [1] Map take a function and iterate
# [2] Map called Map because it Map the function on every element of the list
# [3] Map return a list of the result of the function
# [4] The function can be pre_defined or lambda function
# [5] map(function, iterable)


# ! use map with pre_defined function
# def format(name):
#     return f" - {name.strip().upper()} - "


# Mynames = ["Mahmoud", "Elsayed", "Mahmoud"]

# Myformattednames = map(format, Mynames)

# print(Myformattednames) # Map return adress of object in memory

# for n in Myformattednames:
#     print(n)

# for n in list(map(format, Mynames)):  # if you dont wont variable to store the map
#     print(n)

# ! use map with lambda function

# Mynames = ["Mahmoud", "Elsayed", "Mahmoud"]

# for n in list(map((lambda x: f" - {x.strip().upper()} - "), Mynames)):
#     print(n)


# ! built-in function part five filter
# [1] Filter take a function and iterate
# [2] Filter called Filter because it Filter the function on every element of the list
# [3] Filter return a list of the result of the function
# [4] The function can be pre_defined or lambda function
# [5] filter(function, iterable)
# [6] the function must return True or False if True the element will be in the list if False the element will not be in the list


# def number(num):
#     # if num % 2 == 0:
#     return num % 2 == 0


# Mynums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20]
# Myresult = filter(number, Mynums)
# print(Myresult)  # return the adress of the object in memory
# for n in Myresult:
#     print(n)


# def checkname(name):
#     # if name[0] == "o":
#     return name[0] == "o" # or name.startswith("o")


# Mystrands = ["Mahmoud", "Elsayed", "Mahmoud", "osama"]
# Myresult = filter(checkname, Mystrands)
# for n in Myresult:
#     print(n)


# Mystrands = ["Mahmoud", "Elsayed", "Mahmoud", "osama"]
# for nm in filter(lambda x: x.startswith("o"), Mystrands):
#     print(nm)


# ! built-in function part six Reduce
# [1] Reduce Take A Function + Iterator and the Iterator Can Be List or Tuple
# [2] Reduce Run A Function On First And Second Element And Give Result
# [3] Then Run Function On Result And Third Element
# [4] Then Run Function On Result And Fourth Element And So On
# [5] Till One Element is Left and This is The Result of The Reduce
# [6] The Function Can Be Pre-Defined Function or Lambda Function
# [7] Reduce(function, iterable)


# def sum_all(num1, num2):
#     return num1 + num2


# Mynums = [
#     1,
#     2,
#     3,
#     4,
#     5,
# ]
# result = reduce(sum_all, Mynums)
# print(result)

# ((((1+2)+3)+4)+5) = 15

# Mynums = [
#     1,
#     2,
#     3,
#     4,
#     5,
# ]
# result = reduce(lambda x, y: x + y, Mynums)
# print(result)  # 15

# ! built-in function part seven
# [1] enumerate() take an iterable and return a list of tuples add counter to the itarable when do loop over the list (itrable, start=0)
# [2] help() take a function and return the help of the function
# [3] reversed() take an iterable and return a reversed iterable


# Myskills = ["HTML", "CSS", "JavaScript", "Python"]

# for i in enumerate(Myskills, start=1):
#     print(i)

# Myskills_with_counter = enumerate(Myskills, start=1)

# for count, skill in Myskills_with_counter: # enumerate add new variable which is the counter
#     print(f"{count} : {skill}")

# ! help("keywords")

# print(help(enumerate))

# ! reserved () (itrable)
# mystring = "Elzero"

# print(reversed(mystring))

# print(list(reversed(mystring)))

# for L in reversed(mystring):
#     print(L)

# ! Modules part one Intro ans built-in Modules

# [1] Modules is a set of files containing functions
# [2]you can import a module to use the functions in the module
# [3]you can import multiple modules to use the functions in the module
# [4]you can create your own module

# import random

# print(random)
# print(random.random()) # return a random number between 0 and 1
# print(random.randint(0, 10)) # return a random number between 0 and 10
# print(random.randint(0, 10, 2)) # return a random number between 0 and 10 with a step of 2

# import random

# print(f"print random float {random.random()}") # return a random float number between 0 and 1
# print(f"print random int {random.randint(0, 10)}") # return a random int number between 0 and 10
# print(f"print random int {random.randint(0, 10, 2)}") # return a random int number between 0 and 10 with a step of 2
# print(dir(random)) # show all the functions in the module random

# from random import (
#     randint,  # import the function randint from the module random to impprt more functions use (,)
#     random,
# )  # if ypu wont all the functions in the module random you can use (*)

# print(f"print random float {random()}")

# print(
#     f"print random int {randint(0, 10)}"
# )  # return a random int number between 0 and 10
# # here dont use random.randint because i import the function randint from the module random

# ! Modules part two create your own module
# [1] create a file with the name of the module
# [2] write the functions in the file
# [3] import the module
# [4] use the functions in the module

# import sys

# print(sys.path) # show all the path in the sys.path list and the current working directory is the first path in the list

# sys.path.append(
#     r"C:\Users\Mahmoud Elsayed\Downloads"
# )  # add the folder path that contains od.py

# import od

# od.say("Mahmoud")
# od.is_How("Mahmoud")

# import od as d

# d.say("Mahmoud")
# d.is_How("Mahmoud")

# from od import is_How as h
# from od import say as s

# s("Mahmoud")
# h("Mahmoud")

# ! Modules part three install external package

# [1] Module vs Package
# [2] External Packages Downloaded From The Internet
# [3] You Can Install Packages With Python Package Manager PIP
# [4] PIP Install the Package and Its Dependencies
# [5] Modules List "https://docs.python.org/3/py-modindex.htmI"
# [6] Packages and Modules Directory "https://pypi.org/"
# [7] PIP Manual "https://pip.pypa.io/en/stable/reference/pip_instal1/"


# pip --version check the version of pip
# pip list check the list of installed packages
# pip install package_name install the package
# pip install package_name==version install the package with the specific version
# pip install package_name --upgrade upgrade the package
# pip install package_name --user install the package for the current user
# pip install package_name --target install the package in the target directory
# pip install package_name --no-deps install the package without its dependencies
# pip install package_name --no-binary install the package without its binary dependencies
# pip install package_name --no-compile install the package without its compiled dependencies
# pip install package_name --no-clean-scripts install the package without its clean scripts
# pip install package_name --force-reinstall install the package even if it is already installed
# pip install package_name --ignore-installed ignore the installed package
# pip install package_name --no-warn-script-location install the package without its warning
# pip install package_name --prefix install the package in the prefix directory
# pip install package_name --compile compile the package
# pip install pyfiglet used to print the text in the figlet format

# import pyfiglet
# import termcolor

# # print(pyfiglet.figlet_format("Mahmoud Elsayed", font="slant")) # print the text in the figlet format
# # print(termcolor.colored("Mahmoud Elsayed", "red")) # print the text in the red color format
# # print(dir(pyfiglet))
# print(
#     termcolor.colored(
#         pyfiglet.figlet_format("Mahmoud Elsayed", font="slant"), color="red"
#     )
# )  # print the text in the red color format and the text in the figlet format
# print(

#     termcolor.colored("Mahmoud Elsayed", "red", attrs=["bold"])
# )  # print the text in the red color format and bold

# ! Data and Time

# import datetime as dt

# print(dir(dt))
# print(dir(dt.datetime))

# print(dt.datetime.now())  # return the current date and time

# print(dt.datetime.now().year)  # return the year of the current year

# print(dt.datetime.now().month)  # return the month of the current month

# print(dt.datetime.now().day)  # return the day of the current day

# print(dt.datetime.max)  # return the maximum date

# print(dt.datetime.min)  # return the minimum date

# print(dt.datetime.now().time())  # return the time of the current time

# print(dt.datetime.now().date())  # return the date of the current date

# print(dt.datetime.now().time().hour)  # return the hour of the current hour

# print(dt.datetime.now().time().minute)  # return the minute of the current minute

# print(dt.datetime.now().time().second)  # return the second of the current second

# print(
#     dt.datetime(2021, 1, 1)
# )  # return the date of the year 2021 and the month of January and the day of 1

# print(
#     dt.datetime(2021, 1, 1, 12, 30, 45)
# )  # return the date of the year 2021 and the month of January and the day of 1 and the time of 12:30:45

# ----------------------------------------------------------------------------------------

# mybirthday = dt.datetime(1990, 1, 1)
# datanow = dt.datetime.now()

# print(f"my birthday is {mybirthday - datanow} days old")  # my birthday is 365 days old

# print(
#     f"my birthday is {(mybirthday - datanow).days} days old"
# )  # my birthday is 365 days old


# ! date and time part two format date

# import datetime as dt

# mybirthday = dt.datetime(1990, 1, 1)
# print(mybirthday)
# print(
#     mybirthday.strftime("%a")
# )  # return the weekday of the date in the format of %a  Fri
# print(
#     mybirthday.strftime("%A")
# )  # return the weekday of the date in the format of %A  Friday
# print(
#     mybirthday.strftime("%b")
# )  # return the month of the date in the format of %b  Jan
# print(
#     mybirthday.strftime("%B")
# )  # return the month of the date in the format of %B  January
# print(
#     mybirthday.strftime("%c")
# )  # return the date and time of the date in the format of %c  Fri Jan  1 00:00:00 1990

# print(
#     mybirthday.strftime("%d %B %Y")
# )  # return the date of the date in the format of %d %B %Y  1 January 1990

# ! Itrable vs Iterator

# Iterable
# [1] Object Contains Data That Can Be Iterated Upon
# [2] Examples (String, List, Set, Tuple, Dictionary)
# ********************************************************************************
# Iterator
# [1] Object Used To Iterate Over Iterable Using next) Method Return 1 Element At A Time
# [2] You Can Generate Iterator From Iterable When Using iter() Method
# [3] For Loop Already Calls iter() Method on The Iterable Behind The Scene
# [4] Gives "StopIteration" If Theres No Next Element

# mystring = "Elzero"
# for letter in mystring:
#     print(letter, end=" ")

# mystring = "Elzero"
# myitrable = iter(mystring)
# print(next(iter(myitrable)), end=" ")  # return the first element of the string
# print(next(iter(myitrable)), end=" ")  # return the second element of the string
# print(next(iter(myitrable)), end=" ")  # return the third element of the string
# print(next(iter(myitrable)), end=" ")  # return the fourth element of the string
# print(next(iter(myitrable)), end=" ")  # return the fifth element of the string
# print(next(iter(myitrable)), end=" ")  # return the sixth element of the string

# ! Generators
# [1] Generator is a Function With "yield" Keyword Instead of "return"
# [2] It Support Iteration and Return Generator Iterator By Calling "yield"
# [3] Generator Function Can Have one or More "yield"
# [4] By Using next () It Resume From Where It Called "yield" Not From Begining
# [5]When Called, Its Not Start Automatically, Its Only Give You The Control


# def mygenerator():
#     yield "Elzero"
#     yield "Mahmoud"
#     yield "Elsayed"
#     yield "Mahmoud"


# myitrable = mygenerator()
# print(next(myitrable))  # return the first element of the generator
# print("Hi")  # return hi and then it will return the second element of the generator

# print(next(myitrable))  # return the second element of the generator
# print("Hi")  # return hi and then it will return the third element of the generator

# print(next(myitrable))  # return the third element of the generator
# print("Hi")  # return hi and then it will return the fourth element of the generator

# print(next(myitrable))  # return the fourth element of the generator

# for i in mygenerator(): # or for i in myitrable:
#     print(i)

# ! Decorators

# [1] Sometime Called Meta Programming
# [2] Everything in Python is Object Even Functions
# [3] Decorator Take A Function and Add Some Functionality and Return It
# [4] Decorator Wrap Other Function and Enhance Their Behaviour
# [5] Decorator is Higher Order Function (Function Accept Function As Parameter)
# [7] Decorator is a Function That Takes Another Function As Input And Return A New Function


# def mydecorator(func):  # mydecorator is the decorator
#     def nested(): # nested is the new function
#         print("before") # before is the function that will be called before the function func
#         func() # func is the function that will be called after the function before
#         print("after") # after is the function that will be called after the function func

#     return nested # return the function nested


# @mydecorator # used to call the decorator
# def say():
#     print("Hi")


# say() # call the function say and the decorator mydecorator will be called output before hi after

# after_decorator = mydecorator(say) # used to learn
# after_decorator()

# ! Decorator with Parameters part two


# ! ex 1
# def mydecorator(func):  # mydecorator is the decorator
#     def nested(s1, s2):
#         # nested is the new function
#         if s1 < 0 or s2 < 0:
#             print("Error: Both arguments must be positive")
#             # else:
#             # print(f"The sum of {s1} and {s2} is {s1 + s2}")
#         func(s1, s2)
#         # func is the function that will be called after the function before

#     return nested  # return the function nested


# @mydecorator
# def calc(a1, a2):

#     print(a1 + a2)  # print the sum of the two arguments


# calc(10, 20)

# ! ex 2
# def my_decorator(func):

#     def nested(*args):

#         # Check all arguments
#         if any(x < 0 for x in args):
#             print("Error: All arguments must be positive")
#         else:
#             print(f"The sum is {sum(args)}")

#     return nested


# @my_decorator
# def function_one(a, b):
#     return a + b


# @my_decorator
# def function_two(a, b, c, d):
#     return a + b + c + d


# function_one(-10, 20)
# function_two(10, 20, 30, 40)


# ! ex 3

# def my_decorator(func):

#     def nested(*args):

#         if any(x < 0 for x in args):
#             print("Error: All arguments must be positive")
#         else:
#             func(*args)

#     return nested


# @my_decorator
# def function_there(a, b):
#     print(f"The sum of {a} and {b} is {a + b}")


# @my_decorator
# def function_four(a, b, c, d):
#     print(f"The sum of {a}, {b}, {c}, and {d} is {a + b + c + d}")


# function_there(10, 20)
# function_four(10, 20, 30, 40)

# ! ex 4

# from time import time


# def speedtest(func):
#     def wrapper():
#         start = time()  # use to store the time of begining run before run the funcation
#         func()
#         end = time()   # use to store the time of finsh run after run the funcation
#         print(f"Function Running Time is :{end - start} ")

#     return wrapper


# @speedtest #
# def big_loop():
#     for n in range(1, 20000):
#         print(n)


# big_loop()


# ! parctical loop on many iterators with zip
# [1] zip() take many iterators and return a list of tuples
# [2] zip() return the iterators in the same order as the zipped list

# mylist = [1, 2, 3, 4, 5]
# mylisttwo = ["a", "b", "c"]
# tuple = ("man", "woman", "child")
# dict = {"name": "Mahmoud", "age": 36, "country": "Egypt"}

# for i1, i2, i3, i4 in zip(mylist, mylisttwo, tuple, dict):
#     print(
#         f"List one is {i1} and list two is {i2} and tuple is {i3} and dict is {i4}",
#         "value is",
#         dict[i4],
#     )


# mylist = [1, 2, 3, 4, 5]
# mylisttwo = ["a", "b", "c"]
# zipped = zip(mylist, mylisttwo)

# for i in zipped:
#     print(
#         i
#     )  # THE lowest length of the iterators is used to determine the length of the zipped list


# mylist = [1, 2, 3, 4, 5]
# mylisttwo = [10, 20, 30, 40, 50]
# for i, j in zip(mylist, mylisttwo) :
#     print(f"{i} + {j} = {i + j}")

# ! Parctical image manipulation with Pillow
# https://pillow.readthedocs.io/en/stable/handbook/tutorial.html # to more info
# from PIL import Image

# myimage = Image.open(r"C:\Users\Mahmoud Elsayed\Downloads\resha.jpg")  # open the image
# myimage.show()  # show the image
# # print(myimage.size)  # return the size of the image
# myBox = (100, 100, 200, 200)  # first number is the x coordinate, second number is the y coordinate,
# # third number is the width and fourth number is the height
# newimage = myimage.crop(myBox)  # crop the image
# myconverted = myimage.convert("RGB")  # convert the image to RGB
# myconverted.show()  # show the image

# ! Doc String & Commenting vs Documenting --

# [1] Documentation String For Class, Module or Function
# [2] Can Be Accessed From The Help and Doc Attributes$
# [3]Made For Understanding The Functionality of The Complex Code
# [4] Theres One Line and Multiple Line Doc Strings


# def say():
#     """This is a function that says hello
#     print("Hello")  # This is the function
#     """  # This is documentation string for the function
#     print("Hello")


# say()
# print(say.__doc__)  # print the documentation string
# help(say)  # print the documentation string

# ! Installing and use pylint for better code quality

# [1] Install pylint
# [2] Create a pylintrc file
# [3] Run pylint
# [4] Fix the errors

# """
# This is My Module To Create Function
# To Say Hello
# elzero py - Visual Studio Code

# """


# def say_hello(name):
#     """This Function Only Say Hello To Someone"""
#     msg = "Hello"

#     return f"{msg} {name}"


# say_hello("Ahmed")

# ! Error And Exception Raising

# [1]Exceptions Is A Runtime Error Reporting Mechanism
# [2]Exception Gives You The Message To Understand The Problem
# [3] Traceback Gives You The Line To Look For The Code in This Line
# [4] Exceptions Have Types (SyntaxError, IndexError, KeyError, Etc...)
# [5]Exceptions List https://docs.python.org/3/library/exceptions.html
# [6]raise Keyword Used To Raise Your Own Exceptions (You Can Raise Your Own Exceptions)
# [7]try Keyword Used To Catch Exceptions

# X = -10

# if X < 0:
#     raise ValueError("X must be greater than 0")
# else:
#     print(X)

# y = "Elzero"

# if type(y) != str:
#     raise TypeError("y must be a string") # raise TypeError("y must be a string") raise used to raise your own exception
# else:
#     print(y)

# ! Exception Handling Try Except Else Finally

# num = int(
#     input("Enter your age:").strip()
# )  # strip the white space from the end and beginning of the string

# print(num)
# print(type(num))

# try:
#     num = int(input("Enter your age:"))
# except ValueError:
#     print("Invalid input")
# else:
#     print(num)

# finally:
#     print(
#         "This will always be printed"
#     )  # finally block is used to execute code no matter what happens in the try block

# try:
#     # print(1/0)
#     # print(x)
#     print(int("Variable x is not Defined")) # Erorr Happens since erorr i,m not defind
# except ZeroDivisionError:
#     print("You can't divide by zero")
# except NameError:
#     print("Variable x is not Defined")
# except:
#     print("Erorr Happens ")


# user_password = "admin@123"
# x = 0

# while x <= 4:
#     try:
#         pass1 = input("Enter your password: ").strip().lower()

#         if pass1 == user_password:
#             print("You are an admin")
#             break

#         raise ValueError("Invalid password")

#     except ValueError as error:
#         print(error)
#         x += 1
# else:
#     print("Too many attempts")

# The_File = None
# The_tries = 4

# while The_tries > 0:
#     try:
#         print("Enter The File Name With The Absolute Path")
#         print(f"{The_tries} tries left")
#         print(
#             r"Example: C:\Users\Mahmoud Elsayed\Downloads\mastering python\mastering.py"
#         )
#         The_File_Name = input("Enter the file name: ").strip()
#         The_File = open(The_File_Name, "r")
#         print(The_File.read())
#         break
#     except FileNotFoundError:
#         print("File Not Found")
#         The_tries -= 1
#     except:
#         print("Error")
#     finally:
#         if The_File is not None:
#             print("File Closed")
#             The_File.close()

# else:
#     print("Too many attempts")


# ! Debugging Code

# mylist = [1, 2, 3, 4, 5]
# mydict = {"name": "Mahmoud", "age": 36, "country": "Egypt"}

# for i in mylist:
#     print(i)

# for key, value in mydict.items():
#     print(f"{key} is : {value}")


# ! Type Hinting
# [1] Type hinting is a way to specify the type of a variable


# def say(name: str):
#     print(f"Hello {name}")


# say("Mahmoud")


# def say(name: str, age: int):  # age is an integer and name is a string type hint
#     print(f"Hello {name} your age is {age}")


# say("Mahmoud", 36)

# ! Regular Expressions Part one
# [1] Sequence of Characters That Define A Search Pattern
# [2] Regular Expression is Not In Python Its General Concept
# [3] Used In [Credit Card Validation, IP Address Validation, Email Validation]
# [4] Test RegEx "https://pythex.org/?regex=%5Cw&test_string=rwsjhxsctx+147+1+47&mode=finditer
# [5] Characters Sheet"https://imgv2-2-f.scribdassets.com/img/document/463520737/original/77394f8614/1683427837?v=1"
# [6] Regular Expressions are a way to match a pattern in a string

# ! Regular Expressions Part two Quantifiers
# [1] Quantifiers Are Used To Specify How Many Times A Pattern Must Match
# * 0 Means Zero Or More Times
# + 1 Means One Or More Times
# ? 0 Or 1 Means Zero Or One Times
# {n} n Means Exactly n Times
# {2} 2 Means Two Times
# {2,} 2 Or More Times
# {,6} up to 6 Times
# {2,6} 2 To 6 Times

# ! Regular Exprressions Part three Characters Classes Training
# [0-9] 0 To 9 Characters
# [^0-9] Anything Except 0 To 9 Characters
# [A-Z] A To Z Characters
# [^A-Z] Anything Except A To Z Characters
# [a-z] a To z Characters
# [^a-z] Anything Except a To z Characters
# [a-zA-Z] a To z Or A To Z Characters
# [^a-zA-Z] Anything Except a To z Or A To Z Characters

# ! Regular Exprressions Part four Assertions And Email Pattern
# [^@] Anything Except @
# [.] Anything Except .
# [\w] Anything Except a To z Or A To Z Characters Or 0 To 9 Characters
# [\d] Anything Except 0 To 9 Characters
# ^ Start Of The String
# $ End Of The String

# ^[A-z0-9\.]+@[A-z0-9]+(\.[A-z0-9]+)+$ # Email Pattern
# ^[A-z0-9\.]+@[A-z0-9]+(\.(com|net|org|edu|gov])+$ # Email Pattern

# ! Regular Exprressions Part five Logical Or And Escaping
# | Logical Or
# \ Escaped special character
# () Grouping

# (\d-|\d\)|\d\>) (\w+)
# (\d{3}) (\d{4}) (\d{3}|\(\d{3}\))
# ^(https?:\\)(www\.)?([\w+)\.(com|net|org)$ Email Pattern

# ! Regular Exprressions Part six Re Module Search And FindAll
# search() Search A String For A Match And Return A First Match Only
# findall() Search A String For A Match And Return All Matches and empty list if not found

# !
# import re

# mystring = re.search(
#     r"[A-Z]{2}", "EElzero Web SchooL"
# )  # use search() to search a string for a match and return a first match only

# print(mystring)  # re.Match object; span=(0, 1), match='E'> print the match object

# print(mystring.span())  # return the span of the match

# print(
#     f"The Letter of the match is {mystring.group()}"
# )  # return the letter of the match
# print(
#     f"The Regex of the match is {mystring.re.pattern}"
# )  # return the regex of the match
# print(f"The Index of the match is {mystring.start()}")  # return the index of the match

# print(
#     f"The Letter of the match is {mystring.group()}"
# )  # return the letter of the match

# !

# isvalidemail = re.search(
#     r"^[A-Za-z0-9\.]+@[A-Za-z0-9]+(\.[A-Za-z0-9]+)+$", "osama@gmail.com"
# )  # use search() to search a string for a match and return a first match only
# if isvalidemail:
#     print("Valid Email") # return the letter of the match
#     print(isvalidemail.span())  # return the span of the match
#     # print(isvalidemail.string())  # return the string of the match
#     print(isvalidemail.group())  # return the letter of the match
# else:
#     print("Not Valid Email")

# # print(isvalidemail)  # re.Match object; span=(0, 1), match='E'> print the match object


# ! findall() (pattern, string) pattern is the regex pattern and string is the string to search

# email = input(
#     "Enter your email: "
# ).strip()  # strip removes the whitespace from the end and beginning of the string
# search = re.findall(
#     r"^[A-Za-z0-9\.]+@[A-Za-z0-9]+(\.[A-Za-z0-9]+)+$", email
# )  # findall() search a string for a match and return all matches and empty list if not found
# mylist = []  # mylist is a list that will contain the email if it is valid
# if search:  # if search is not empty
#     mylist.append(email)  # add the email to the list
#     print(f"Your Email is {mylist}")  # print the list
# else:
#     print("Invalid Email")  # print the message if the email is invalid


# ! Regular Expressions Part seven Re Module Split And Sub
# [1] Split (string, pattern, maxsplit) => Return A List Of Elements Splitted On Each Match
# [2] Sub (Pattern, Replacement, string) => Replace A Pattern With A Replacement In A String
# [3] Sub (Pattern, Replacement, string, count) => Replace A Pattern With A Replacement In A String And Return The Number Of Replacements

# !

# import re

# streing_one = "Hello World! i love python"
# search = re.split(r"\s", streing_one, maxsplit=1)
# print(search)

# !

# streing_two = "How-to_Write_A_Very-Good-Article"
# search_two = re.split(r"[-|_]", streing_two)
# print(search_two)

# for c, i in enumerate(search_two, start=1):
#     if len(i) == 1:
#         continue
#     print(f"Word Number is : {c} and the word is {i.lower()}")


# # ! sub()
# print(re.sub(r"\s", "_", "Hello World! i love python"))
# print(re.sub(r"\s", "_", "Hello World! i love python", count=1))


# ! Regular Expressions Part eight Groups Trim And Flags


# ! oop part one
# WHAT IS OOP?
# Python Support Object Oriented Programming
# OOP Is A Paradigm Or Coding Style
# Paradigm =>
# Means Structuring Program So The Methods[Functions] and Attributes [Data] "
# Are Bundled Into Objects
# Methods => Act As Function That Use The Information Of The Object
# Python Is Multi-Paradigm Programming Language [Procedural, OOP, Functional]
# Procedural => Structure App Like Recipe, Sets Of Steps To Make The Task
# Functional=> Built On the Concept of Mathematical Functions

# ! oop part two
# [01] Class is The Blueprint Or Construtor Of The Object
# [02] Class Instantiate Means Create Instance of A Class
# [03] Instance => Object Created From Class And Have Their Methods and Attributes
# [04] Class Defined With Keyword class
# [05] Class Name Written With PascalCase [UpperCamelCase] Style
# [06] Class May Contains Methods and Attributes
# [07] When Creating object Python Look For The Built In init Method
# [08] _init_ Method Called Every Time You Create Object (Instance) Of The Class) From Class
# [09] _init_ Method Is Initialize The Data For The object
# [10] Any Method With Two Underscore in The Start and End Called Dunder or Magic Method
# [11] self Refer To The Current Instance Created From The Class (And Must Be First Param)
# [12] self Can Be Named Anything But By Convention We Use self
# [13] In Python Do Not Need To Call Nwe () Keyword To Create Object From Class

# !  syntax of class
# class ClassName:
#     constructor=> Do Initialization [Create Instance] Of The Object
#     Each Instance Of The Class Separated Object

#     def __init__(self, param1, param2):
#         Body of Function

#     method=> Do Actions With The Object
#     attribute=> Store Data With The Object


# class person:
#     def __init__(
#         self, name, age
#     ):  # _init_ method is called every time you create object from class and must be contain argument self
#         print(f"Hello {name} your age is {age}")


# person_one = person("Mahmoud", 36)
# person_two = person("Elsayed", 36)

# # person()  # create object from class Person and call the _init_ method
# # person("Mahmoud", 36)  # create object from class Person and call the _init_ method
# print(person_one)
# print(person_two)  # print the object person_two
# print(person_one.__class__)  # print the class of the object person_one

# ! OOP Part Three Inheritance Attributes And Methods part one
# Self: Point To Instance Created From Class
# Instance Attributes: Instance Attributes Defined Inside The  (Constructor == class)
# ---------------------------------------------------------------------
# Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself


# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# person_one = person("Mahmoud", 36) # create object person_one from class person
# person_two = person("Elsayed", 36)

# print(f"Hello {person_one.name} your age is {person_one.age}")
# print(f"Hello {person_two.name} your age is {person_two.age}")


# ! OOP Part Four Inheritance Attributes And Methods part two


# class person:
#     def __init__(self, firstname, midename, lastname, gender):
#         self.firstname = firstname  # instance attributes  (firstname is the attribute of the object person_one and person_two)
#         self.midename = midename
#         self.lastname = lastname
#         self.gender = gender

#     def FullName(self):
#         return f"Hello {self.firstname} {self.midename} {self.lastname}"

#     def SayMaster(self):
#         if self.gender == "male":
#             return f"Hello Master {self.firstname}"
#         elif self.gender == "female":
#             return f"Hello Miss {self.firstname}"
#         else:
#             return f"Hello {self.firstname}"

#     def GetAllInfo(self):
#         return f"{self.SayMaster()} , your full name is {self.FullName()}"


# person_one = person(
#     "Mahmoud", "Elsayed", "Mahmoud", "male"
# )  # (person_one is the object of the class person and firstname, midename, lastname are the attributes of the object person_one)
# person_two = person("Mona", "Elsayed", "Mahmoud", "female")

# print(
#     f"Hello {person_one.firstname[0].lower()}{'.' + person_one.midename.lower()}{'.' + person_one.lastname[0].lower()}"
# )
# print(f"Hello {person_two.firstname} {person_two.midename} {person_two.lastname}")
# print(person_one.FullName())


# print(person_two.SayMaster())

# print(person_one.GetAllInfo())


# ! OOP Part Five class Attributes
# import random

# class person:
#     UserId = random.randint(10000, 99999)  # class attributes (UserId is the attribute of the class person)
#     not_allowed_names = [
#         "Hall",
#         "Shit",
#         "Fuck",
#         "Bitch",
#     ]  # class attributes (not_allowed_names is the attribute of the class person)

#     users_count = (
#         0  # class attributes (users_count is the attribute of the class person)
#     )

#     def __init__(self, firstname, midename, lastname, gender, ):
#         self.firstname = firstname  # instance attributes  (firstname is the attribute of the object person_one and person_two)
#         self.midename = midename
#         self.lastname = lastname
#         self.gender = gender
#         person.users_count += 1
#         person.UserId


#     def FullName(self):
#         if self.firstname in person.not_allowed_names:
#             raise ValueError("Firstname is not allowed")
#         else:
#             return f"Hello {self.firstname} {self.midename} {self.lastname}, His UserId is {person.UserId}"

#     def SayMaster(self):
#         if self.gender == "male":
#             return f"Hello Master {self.firstname}"
#         elif self.gender == "female":
#             return f"Hello Miss {self.firstname}"
#         else:
#             return f"Hello {self.firstname}"

#     def GetAllInfo(self):
#         return f"{self.SayMaster()} , your full name is {self.FullName()}"

#     def DeleteUser(self):
#         if person.users_count == 0:
#             raise ValueError("No Users")
#         else:
#             print(f"User {self.FullName()} has been deleted")
#             person.users_count -= 1


# print(person.users_count)  # print the class attribute users_count = 0

# person_one = person("Mahmoud", "Elsayed", "Mahmoud", "male")
# person_two = person("Mona", "Elsayed", "Mahmoud", "female")

# print(person_one.FullName())

# print(person.users_count)  # print the class attribute users_count = 2

# person_one.DeleteUser()

# print(person.users_count)  # print the class attribute users_count = 2


# print(person_one.get_all_info())
# print(person("Hall", "Elsayed", "Mahmoud", "male").get_all_info())


# ! OOP Part Six class Methods And Static Methods

# Class Method
# -Marked With @classmethod Decorator To Flag It As Class Method
# -It-Take Cls Parameter Not Self To Point To The Class not The Instance
# -It Doesn't Require Creation of a Class Instance
# -Used When You Want To Do Something With The Class Itself
# -Static Methods:
# -It Takes No Parameters
# -Its Bound To The Class Not Instance
# -Used When Doing Something # ! Doesnt Have Access To Object Or•Class But Related To Class


# class person:
#     Users = []  # Keeps references to every person instance that is created
#     NotAllowedNames = [
#         "Hall",
#         "Shit",
#         "Fuck",
#         "Bitch",
#     ]  # class attributes (not_allowed_names is the attribute of the class person)

#     @classmethod  # class method is a method that is bound to the class and not the instance of the class
#     def ShowAllUsersInfo(
#         cls,
#     ):  # cls is a parameter that is used to refer to the class itself and not the instance of the class
#         print(
#             f"We Have {cls.UsersCount} Users In Our System"
#         )  # In Class Method we can access class attribute and class method using cls keyword.But we can't access instance attribute And instance methods using cls keyword Or self keyword.
#         for user in person.Users:
#             print(user.FullName())

#     @staticmethod  # static method is a method that is bound to the class and not the instance of the class
#     def SayHi():  # may be not take any parameter
#         # static method can't access class attribute and class method using cls keyword.
#         # But we can access instance attribute And instance methods using self keyword.
#         print("Hello from static method")

#     UsersCount = (
#         0  # class attributes (users_count is the attribute of the class person)
#     )

#     def __init__(self, firstname, midename, lastname, gender):
#         self.firstname = firstname  # instance attributes  (firstname is the attribute of the object person_one and person_two)
#         self.midename = midename
#         self.lastname = lastname
#         self.gender = gender
#         person.UsersCount += 1
#         person.Users.append(self)

#     def FullName(self):
#         if self.firstname in person.NotAllowedNames:
#             raise ValueError("Firstname is not allowed")
#         else:
#             return f"Firts Name is {self.firstname} Middle Name is {self.midename} Last Name is {self.lastname}"

#     def SayMaster(self):
#         if self.gender == "male":
#             return f"Hello Master {self.firstname}"
#         elif self.gender == "female":
#             return f"Hello Miss {self.firstname}"
#         else:
#             return f"Hello {self.firstname}"

#     def GetAllInfo(self):
#         return f"{self.SayMaster()} , your full name is {self.FullName()}"

#     def DeleteUser(self):
#         if self not in person.Users:
#             raise ValueError("User does not exist")

#         print(f"User {self.firstname} has been deleted")
#         person.Users.remove(self)
#         person.UsersCount -= 1


# print(person.UsersCount)  # print the class attribute users_count = 0

# person_one = person("Mohamed", "Elsayed", "Mahmoud", "male")
# person_two = person("Mona", "Elsayed", "Mahmoud", "female")


# # person_one.DeleteUser()
# print(person.UsersCount)  # print the class attribute users_count = 2

# person.ShowAllUsersInfo()  # call the class method show_users to print the total users
# # print(person_one.get_all_info())
# # print(person("Hall", "Elsayed", "Mahmoud", "male").get_all_info())
# person.SayHi()  # call the static method hi to print hello from static method


# ! OOP Part Seven Magic Methods
# Everything in Python is An Object
# __init__ Called Automatically When Instantiating Class
# self._class The class to which a class instance belongs
# __str__  Gives a Human-Readable Output of the Object
# __len__ Returns the Length of the Container
#  Called When  We Use the Built-in•len() Function on the object


# class skill:
#     def __init__(
#         self,
#     ):  # refers to the instance of the class and is used to access the attributes and methods of the class
#         self.skill_name = ["HTML", "CSS", "JavaScript", "Python"]

#     def __str__(
#         self,
#     ):  # refers to the instance of the class and is used to access the attributes and methods of the class
#         return f"My Skills Are : {self.skill_name}"

#     def __len__(self):

#         return len(
#             self.skill_name
#         )  # refers to the instance of the class and is used to access the attributes and methods of the class


# profile = skill()
# profile.skill_name.append("Django")  # append the skill Django to the list of skills


# print(profile)  # print the object profile
# print(len(profile))
# print(profile.skill_name)
# print(profile.__class__)  # print the class of the object profile
# print(profile.__str__())  # print the human-readable output of the object profile
# print(str(profile))

# my_string = "Elzero"  # my_string is an object of the class str and is used to access the attributes and methods of the class str
# print(type(my_string))  # print the type of the object my_string
# print(my_string.__class__)  # print the class of the object my_string
# print(dir(str))  # print the attributes and methods of the object str
# print(str.upper(my_string))  # print the human-readable output of the object my_string


# ! OOP Part Eight Inheritance


# class food:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def Eat(self):
#         print("Eat Method from base class")


# class putani(food):
#     def __init__(self, name, price, count):
#         super().__init__(name, price)  # calling the constructor of the base class
#         self.count = count
#         print(
#             f"{self.name} Is created from derived class and price is : {self.price} and count is : {self.count}"
#         )  # print the name and price of the object

#     def Catch(self):
#         print(
#             "Catch method from derived class"
#         )  # print the method of the derived class


# # food_one = food("Pizza")
# food_two = putani("Burger", 15, 1)
# food_two.Eat()  # calling the Eat method of the base class
# food_two.Catch()

# ! OOP Part Nine Multiple Inheritance And Overriding_Mathods

# class Manu:
#     def ShowMenu(self):
#         print("Available items: Pizza, Burger, Salad")


# class Order:
#     def ShowOrder(self):
#         print(f"Order: {self.item} x {self.quantity}")


# class DateOfOrder:
#     def ShowDate(self):
#         print(f"Order date: {self.date}")


# class Payment:
#     def ShowPayment(self):
#         print(f"Payment method: {self.payment_method}")


# class CustomerOrder(Manu, Order, DateOfOrder, Payment):
#     def __init__(self, item, quantity, date, payment_method, price):
#         self.item = item
#         self.quantity = quantity
#         self.date = date
#         self.payment_method = payment_method
#         self.price = price

#     # This overrides ShowOrder from the Order class.
#     def ShowOrder(self):
#         total = self.price * self.quantity
#         print(f"Order: {self.item} x {self.quantity} = ${total:.2f}")

#     def ShowSummary(self):
#         self.ShowMenu()
#         self.ShowOrder()
#         self.ShowDate()
#         self.ShowPayment()


# customer_order = CustomerOrder("Pizza", 2, "2026-10-24", "Credit card", 12.50)
# customer_order.ShowSummary()

# ! OOP Part Ten Polymorphism
# fun have the same name but have more than one and do onther thing different about onther class

# f1 = 10
# f2 = 20
# print(f1 + f2)  # print the sum of f1 and f2
# s1 = "Hello"
# s2 = "World"
# print(s1 + "  " + s2)  # print the concatenation of s1 and s2
# print(len([1, 2, 3]))  # print the length of the list
# print(len("Hello"))  # print the length of the string "Hello"
# print(len({"key":1, "key2":2}))  # print the length of the dictionary


# class A:
#     def say(self):
#         print("Hello from class A")
#         raise NotImplementedError("This method should be overridden in a subclass")


# class B(A):
#     def say(self):
#         print("Hello from class B")


# class C(A):
#     def say(self):
#         print("Hello from class C")


# my_instance = B()
# my_instance.say()  # call the function say of the class B
# # my_instance2 = A()
# # my_instance2.say()  # call the function say of the class A

# ! OOP Part Eleven Encapsulation
# • Encapsulation
# - Restrict Access To The Data Stored in Attirbutes and Methods
# Public
# - Every Attribute and Method That We Used So Far Is Public
# - Attributes and Methods # ! Can Be Modified-and-Run From-Everywhere
# - Inside Our Outside The Class
# Protected
# - Attributes and Methods # ! Can Be Accessed From Within The Class And Sub Classes
# - Attributes and Methods Prefixed With One Underscore -
# Private
# - Attributes and Methods Can # ! Be Accessed - From Within The Class Or Object Only
# - Attributes Cannot Be Modified From Outside The Class
# - Attributes and Methods Prefixed With Two Underscores -
# - Attributes = Variables = Properties


# class Mamber:
#     def __init__(self, name):
#         self.name = name  # public attribute

# one = Mamber("Mahmoud")
# print(one.name)
# one.name = "Mahmoud Elsayed"
# print(one.name)


# class Mamber:
#     def __init__(self, name):
#         self._name = name  # protected attribute

# one = Mamber("Mahmoud")
# print(one._name)
# one._name = "Mahmoud Elsayed"
# print(one._name)


# class Member:
#     def __init__(self, name):
#         self.__name = name  # private attribute

#     def say(self):
#         return f"Hello {self.__name}"


# one = Member("Mahmoud")
# print(one.__name) # AttributeError: 'Member' object has no attribute '__name' since it is private
# print(one.say())
# print(one._Member__name)  # name mangling to access private attribute and it is not recommended to use it

# ! OOP Part Twelve Property Getter And Setter


# class Mamber:
#     def __init__(self, name):
#         self.__name = name  # private attribute

#     def Say(self):
#         return f"Hello {self.__name}"

#     def GetName(self):  # Getter method to access private attribute
#         return self.__name

#     def SetName(self, NewName):  # Setter method to access private attribute
#         self.__name = NewName


# one = Mamber("Mahmoud")
# # one._Mamber__name = "Mahmoud Elsayed"  # name mangling to access private attribute and it is not recommended to use it
# # print(
# #     one._Mamber__name
# # )  # name mangling to access private attribute and it is not recommended to use it

# print(one.GetName())  # Using the getter method to access the private attribute
# one.SetName(
#     "Mahmoud Elsayed"
# )  # Using the setter method to access the private attribute
# print(one.GetName())  # Using the getter method to access the private attribute

# print(one.Say())  # Using the say method to access the private attribute

# ! OOP Part Thirteen Property Decorators


# class Mamber:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def say(self):
#         return f"Hello {self.name}"

#     @property
#     def AgeInDays(self):
#         return f"Your Age Is : {self.age} Years And Age In Days Is : {self.age * 365} "


# one = Mamber("Mahmoud", 21)

# print(one.name)
# print(one.age)
# print(one.AgeInDays)  # property decorator is used to create a new attribute
# # print(one.AgeInDays()) # cant run since AgeInDays is a property decorator and not a method so we not use () to call it
# print(one.say())

# ! OOP Part Fourten ABS,s Abstract Base Class

# - Class Called Abstract Class If it Has One or More Abstract Methods
# - abc module in Python Provides Infrastructure for Defining Custom Abstract Base Classes.
# - By -Adding @absttractmethod Decorator on The Methods
# - ABCMeta Class Is a Metaclass Used For Defining Abstract Base Class


# from abc import ABCMeta, abstractmethod


# class program(metaclass=ABCMeta):
#     @abstractmethod
#     def HasOpp(self):
#         pass  # abstract method

#     def GetName(self):
#         pass

# class Student(program):
#     # pass  #  ! TypeError: Can't instantiate abstract class Student without an implementation for abstract method 'HasOpp'
#     def HasOpp(self):
#         return "No"


# class Teacher(program):
#     def HasOpp(self):
#         return "Yes"

# # one = program()
# # print(one.HasOpp()) # TypeError: Can't instantiate abstract class program with abstract method has_opp
# two = Student()
# print(two.HasOpp())

# three = Teacher()
# print(three.HasOpp())


# ! DataBase Part One

# Database Is A Place Where We Can Store Data
# - Database Organized Into Tables (Users, Categories)
# - Tables Has Columns (ID, Username,  Password)
# - There's Many Types Of Databases (MongoDB, MysQL, SQLite)
# - SQL Stand  For Structured Query Language
# - SQLite => Can- Run in Memory or in A Single File
# - You Can Browse File With https://sqlitebrowser.org/
# - Data Inside Database Has Types  (Text,  Integer, Date)

# ! DataBase Create DataBase And Connect
# - connect() => Create Database If Not Exist And Connect To It
# - execute() => Execute SQL Statement
# - close() => Close The Connection To The Database

# import sqlite3

# import sqlite3

# db = sqlite3.connect(
#     "mydatabase.db"
# )  # create a database file if not exist and connect to it

# db.execute(
#     "CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER )"
# )  # create a table and columns in the database if not exist

# db.close()  # close the connection to the database

# ! DataBase Insert Data Into Table
# - Cursor() => All The Operations That We Do On The Database Will Be Done Through Cursor Not Connection
# - commit() => Commit The Changes To The Database

# import sqlite3

# db = sqlite3.connect(
#     "mydatabase.db"
# )  # create a database file if not exist and connect to it

# cr = db.cursor()  # create a cursor to perform operations on the database

# cr.execute(
#     "CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER )"
# )  # create a table and columns in the database if not exist

# cr.execute(
#     "CREATE TABLE IF NOT EXISTS users (user_id INTEGER, name TEXT)"
# )  # create a table and columns in the database if not exist

# my_list = [
#     ["HTML", 100, 1],
#     ["CSS", 90, 1],
#     ["JavaScript", 80, 1],
#     ["Python", 70, 1],
#     ["Django", 60, 1],
#     ["Flask", 50, 1],
#     ["React", 40, 1],
#     ["Angular", 30, 1],
#     ["NodeJS", 20, 1],
#     ["Express", 10, 1],
# ]
# for name, prores, user in my_list:
#     cr.execute(
#         f"INSERT INTO skills (name, progress, user_id) VALUES ('{name}', {prores} , {user})",
#     )  # insert data into the table skills

# # cr.execute(
# #     "INSERT INTO skills (name, progress, user_id) VALUES ('HTML', 100, 1)"
# # )  # insert data into the table skills

# # cr.execute(
# #     "INSERT INTO users (user_id, name) VALUES (1, 'Mahmoud')"
# # )  # insert data into the table users

# # cr.execute(
# #     "INSERT INTO users (user_id, name) VALUES (2, 'Elsayed')"
# # )  # insert data into the table users


# db.commit()  # commit the changes to the database save the changes

# db.close()  # close the connection to the database


# my_list = [
#     ["HTML", 100, 1],
#     ["CSS", 90, 1],
#     ["JavaScript", 80, 1],
#     ["Python", 70, 1],
#     ["Django", 60, 1],
#     ["Flask", 50, 1],
#     ["React", 40, 1],
#     ["Angular", 30, 1],
#     ["NodeJS", 20, 1],
#     ["Express", 10, 1],
# ]
# for i, j, k in my_list:
#     print(i, j, k)

# ! DataBase Sqlite3 Retrieve Data From Database
# - fetchone() => Return One Row From The Cursor
# - fetchall() => Return All Rows From The Cursor Return A List Of Tuples
# - fetchmany(size) => Return Many Rows From The Cursor

# import sqlite3

# db = sqlite3.connect(
#     "mydatabase.db"
# )  # create a database file if not exist and connect to it

# cr = db.cursor()  # create a cursor to perform operations on the database

# cr.execute(
#     "CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER )"
# )  # create a table and columns in the database if not exist

# cr.execute(
#     "CREATE TABLE IF NOT EXISTS users (user_id INTEGER, name TEXT)"
# )  # create a table and columns in the database if not exist

# cr.execute(
#     "INSERT INTO users (user_id, name) VALUES (1, 'Mahmoud')"
# )  # insert data into the table users

# cr.execute(
#     "INSERT INTO users (user_id, name) VALUES (2, 'Elsayed')"
# )  # insert data into the table users

# cr.execute(
#     "INSERT INTO users (user_id, name) VALUES (3, 'Mahmoud Elsayed')"
# )  # insert data into the table users

# cr.execute("select name from users")  # select data from the table users
# for name in cr.fetchall():  # fetchall() return all rows from the cursor
#     print(name)  # print the data from the table users

# print(cr.fetchone())  # print the data from the table users
# print(cr.fetchall())  # print the data from the table users
# print(cr.fetchmany(2))  # print the data from the table users

# db.commit()  # commit the changes to the database save the changes
# db.close()  # close the connection to the database


# # ! DataBase Training On Everything


# def get_all_data():

#     try:
#         db = sqlite3.connect(
#             "mydatabase.db"
#         )  # create a database file if not exist and connect to it

#         print("Database Connected")  # print the message if the database is connected

#         cr = db.cursor()  # create a cursor to perform operations on the database

#         cr.execute("SELECT * FROM users")  # select all data from the table users
#         data = (
#             cr.fetchall()
#         )  # Assign the data from the table users to the variable data

#         print(
#             "Database Has Number Of Rows Is : ", len(data)
#         )  # print the number of rows in the table users

#         print("Showing All Data From The Table Users")

#         for row in data:  # fetchall() return all rows from the cursor
#             print("User Id :", row[0], end=" ")
#             print("User Name :", row[1])

#     except sqlite3.Error as er:  # catch the exception if the database is not connected e is ilis name of the exception
#         print(f"Failed to Connect to Database{er}")

#     finally:
#         if db:
#             db.commit()  # commit the changes to the database save the changes
#             db.close()  # close the connection to the database
#             print("Database Closed")  # print the message if the database is closed


# get_all_data()

# try used to handle exceptions and errors that may occur during the execution of the code.
# In this case, it is used to catch any errors that may occur while connecting to the database or fetching data from the table.
# If an error occurs, the code inside the except block will be executed, and a message will be printed indicating that the connection to the database failed.

# ! DataBase Update And Delete Data From Database
# - update() => Update The Data In The Table
# - delete() => Delete The Data From The Table

# import sqlite3

# db = sqlite3.connect(
#     "mydatabase.db"
# )  # create a database file if not exist and connect to it

# cr = db.cursor()  # create a cursor to perform operations on the database

# cr.execute("UPDATE users SET name = 'Ahmed Mahmoud ' WHERE user_id = 1")

# cr.execute("DELETE FROM users WHERE user_id = 2")

# cr.execute("select * from users ")

# print(cr.fetchall())

# db.commit()

# ! DataBase Create APP SKILLS PART ONE

# import sqlite3

# db = sqlite3.connect("mydatabase.db")
# cr = db.cursor()
# cr.execute("SELECT * FROM users")
# users = cr.fetchall()
# db.close()

# user = input("Enter your username: ")
# if user in [i[1] for i in users]:
#     print("You are allowed to access this app")
#     print(f"Welcome {user} to the app")
#     try:
#         print("Opthion => 1: Show All Skills")
#         print("Opthion => 2: Add a new skill")
#         print("Opthion => 3: Delete a skill")
#         print("Opthion => 4: Exit")
#         option = input("Enter your option: ").strip().capitalize()

#         if option == "1":
#             print("Showing All Skills")
#             db = sqlite3.connect("mydatabase.db")
#             cr = db.cursor()
#             cr.execute("SELECT * FROM skills")
#             data = cr.fetchall()
#             print(data)
#             db.close()

#         elif option == "2":
#             print("Enter the skill name: ")
#             skill = input().strip().capitalize()
#             cr.execute("SELECT * FROM skills")
#             data = cr.fetchall()
#             if skill in [i[0] for i in data]:
#                 print("Skill already exist")
#                 db.close()
#             else:
#                 print("Enter the progress: ")
#                 progress = int(input().strip())
#                 print("Enter the user id: ")
#                 user_id = int(input().strip())
#                 db = sqlite3.connect("mydatabase.db")
#                 cr = db.cursor()
#                 cr.execute(
#                     f"INSERT INTO skills (name, progress, user_id) VALUES ('{skill}', {progress} , {user_id})"
#                 )
#                 db.commit()
#                 print(f"Skill {skill} has been added successfully")
#                 db.close()

#         elif option == "3":
#             print("Enter the skill name to delete: ")
#             skill = input().strip().capitalize()
#             db = sqlite3.connect("mydatabase.db")
#             cr = db.cursor()
#             cr.execute("SELECT * FROM skills")
#             data = cr.fetchall()
#             if skill not in [i[0] for i in data]:
#                 print(f"Skill {skill} does not exist")
#                 db.close()
#             else:
#                 cr.execute(f"DELETE FROM skills WHERE name = '{skill}' AND user_id = 1")
#                 db.commit()
#                 print(f"Skill {skill} has been deleted successfully")
#                 db.close()

#         elif option == "4":
#             print("Thank you for using the app")

#         else:
#             raise ValueError("Invalid option")

#     finally:
#         if db:
#             db.close()
#             print("Database Closed")

# else:
#     print("You are not allowed to access this app")

# ! DataBase Create APP SKILLS Ex 2

# import sqlite3

# db = sqlite3.connect("mydatabase.db")
# cr = db.cursor()

# user_id = 2

# input_masseage = """
# Choose an option:
# "show" => Show All Skills
# "add" => Add a new skill
# "delete" => Delete a skill
# "update" => Update a skill
# "exit" => Exit the app
# Enter your option:
# """
# user_input = input(input_masseage).strip().lower()

# commands_list = ["show", "add", "delete", "update", "exit"]


# def commit_and_close() -> None:
#     db.commit()
#     db.close()
#     print("Connection To Database Closed")


# def show_skills():
#     print("Showing All Skills")
#     cr.execute(f"SELECT * FROM skills WHERE user_id = {user_id}")
#     skills = cr.fetchall()
#     if len(skills) > 0:
#         print(f"You Have {len(skills)} Skills")
#         for row in skills:
#             print(f"Skill Name: {row[0]} , Progress: {row[1]}% , User Id: {row[2]}")
#     else:
#         print("Do Not Have Any Skills")
#     commit_and_close()


# def add_skill():
#     print("Enter the skill name: ")
#     skill = input().strip().capitalize()
#     cr.execute(
#         f"SELECT name FROM skills WHERE name = '{skill}' AND user_id = {user_id}"
#     )
#     skills = cr.fetchall()
#     for i in skills:
#         if i[0] == skill:
#             print("Skill already exist")
#             print("You Wont To Update It")
#             if input("Enter your option Y/N: ").strip().lower() == "y":
#                 print("Enter the progress: ")
#                 progress = int(input().strip())
#                 cr.execute(
#                     f"UPDATE skills SET progress = {progress} WHERE name = '{skill}' AND user_id = {user_id}"
#                 )
#                 print(
#                     f"Skill {skill} has been updated successfully And Progress Now Is {progress}"
#                 )
#             else:
#                 print("Your Choice Was No Meening That You Dont Want To Update It")
#         else:
#             print(f"Skill {skill} does not exist You Can Add It")
#             print("Enter the progress: ")
#             progress = int(input().strip())
#             cr.execute(
#                 f"INSERT INTO skills (name, progress, user_id) VALUES ('{skill}', {progress} , {user_id})"
#             )
#             print(f"Skill {skill} has been added successfully")
#             break

#     commit_and_close()


# def delete_skill():
#     print("Enter the skill name to delete: ")
#     cr.execute(f"SELECT name FROM skills WHERE user_id = {user_id}")
#     skills = cr.fetchall()
#     skill = input().strip().capitalize()
#     if skill in [i[0] for i in skills]:
#         cr.execute(f"DELETE FROM skills WHERE name = '{skill}' AND user_id = {user_id}")
#     else:
#         print(f"Skill {skill} does not exist")

#     commit_and_close()


# def update_skill():
#     print("Enter the skill name to update: ")
#     cr.execute(f"SELECT name FROM skills WHERE user_id = {user_id}")
#     skills = cr.fetchall()
#     skill = input().strip().capitalize()
#     if skill not in [i[0] for i in skills]:
#         print(f"Skill {skill} does not exist")
#     else:
#         print("Enter the progress: ")
#         progress = int(input().strip())
#         cr.execute(
#             f"UPDATE skills SET progress = {progress} WHERE name = '{skill}' AND user_id = {user_id}"
#         )
#         print(
#             f"Skill {skill} has been updated successfully And Progress Now Is {progress}"
#         )

#     commit_and_close()


# def exit_app():

#     commit_and_close()


# if user_input in commands_list:
#     print("Command Found")
#     if user_input == "show":
#         show_skills()

#     elif user_input == "add":
#         add_skill()

#     elif user_input == "delete":
#         delete_skill()

#     elif user_input == "update":
#         update_skill()

#     else:
#         print("App Exited")
#         commit_and_close()
# else:
#     print("Command Not Found")

# ! Advanced Lesson Name And Main Function

# if __name__ == "__main__":
# - __name__ is Built-in Variable That Return The Name Of The Module
# - "__main__" => Value Of The __name__ Variable
# Execution Mathods
# -Directly => Execute The Python File Useing Command Line
# -From Import => Import The Code From File To Another File
# --------------------------------------------------------------------------------
# In Some Cases You Wont To Know If You Are Using A Module Mathod As import
# Or Are Use The Orginal Python File Mathod
# --------------------------------------------------------------------------------
# In Directly Mode Python Assign A Value To The Variable __name__ Which Is The Name Of The Module
# To Built-in Variable __name__ in the graound of the file


# ! Advanced Lesson Timing Your Code With Timeit

# Advanced_Lessons=> Timing Your Code With Timeit --
# - timeit: - Get Execution Time Of Code By Running 1M. Time And Give You Minimal Time
# - timeit: - It Used For Performance By Testing All Functionality
# - timeit (stmt, setup, timer, •number)
# - timeit(pass, pass, default, 1.000.000) • Default.Values
# ---------------------------------------------------------------
# - stmt: Code You Want  To Measure The  Execution-Time
# - setup: Setup-Done  Before  The Code-Execution (Import Module Or Anything)
# - timer: The Timer Value
# - number: How-Many Execution That Will Run
# ---------------------------------------------------------------

# import random
# import timeit

# print(timeit.timeit("'Hello World!'*1080")) # timeit.timeit is used to measure the execution time of a statement

# name = "Mahmoud"
# print(name*1080)
# print(timeit.timeit("name = 'Mahmoud' ; name * 1080")) # explain line of code is

# print(random.randint(0, 100))
# print(timeit.timeit(stmt="random.randint(0, 100)", setup="import random"))

# print(timeit.repeat(stmt="random.randint(0, 100)", setup="import random", repeat=10))

# ! - Advanced_Lessons=> Add Logging To Your Code --
# --------------------------------------------------------------------------------
# - Print Out  To Console Or File
# - Print Logs Of What Happens
# --------------------------------------------------------------------------------
# - DEBUG
# - INFO
# - WARNING
# - ERROR
# - CRITICAL
# --------------------------------------------------------------------------------
# name=> Logging Module Give It To The Default Logger.
# --------------------------------------------------------------------------------
#  Basic Config
# - level=> Level of Severity
# - filename=> File Name And Extension
# - filemode=> Mode Of File (a => Append, w => Write, x => Create)
# - format=> Format Of The Log Message (name, levelname, message, asctime)
# - datefmt=> Date Format Of The Log Message (asctime) Use To Format The Date
# --------------------------------------------------------------------------------
# - getLogger(name)=> Get The Logger By Name (name)


# import logging

# # print(dir(logging))

# logging.basicConfig(
#     filename="app.log",
#     filemode="a",
#     format="Logger_name: (%(asctime)s) => | %(name)s | %(levelname)s => '%(message)s'",
#     datefmt="%d  %B  %Y , %H:%M:%S",
# )  # create a file called app.log and write the logs to it

# My_Logger = logging.getLogger("My_Logger")  # get the logger
# My_Logger.warning("This is a warning message")  # write a warning message to the file
# # logging.critical("This is a critical message")  # write a critical message to the file
# # logging.error("This is a error message")
# # logging.warning("This is a warning message")
# # logging.info("This is an info message")
# # logging.debug("This is a debug message")

# ! Advanced_Lessons => Unit Testing With Unittest --
# Test Runner
# - The Module That Run The Unit Testing (unittest, pytest)
# --------------------------------------------------------------------------------
# Test Case
# -Smallest Unit Of Testing
# -It Use Asserts Methods To Check For Actions And Responses
# --------------------------------------------------------------------------------
# Test Suite
# -Collection Of Multiple Tests Or Test Cases
# --------------------------------------------------------------------------------
# Test Report
# - A-Full Report Contains The Failure Or Succeed
# --------------------------------------------------------------------------------
# unittest
# - Add Tests Into Classes As Methods
# - Use a Series of Special Assertion Methods
# https://docs.python.org/3/library/unittest.html

# --------------------------------------------------------------------------------


# assert 3 + 5 == 8, "Should Be 8" # assert is used to check if the condition is true or false
# not return anything but raise an error if the condition is false
# Return Nothing Since 3 + 5 == 8 And No Error Raised

# assert 3 + 5 == 9, "Should Be 8" # Return Error Since 3 + 5 != 8 And Error Raised Is AssertionError: Should Be 8


# def test_add_one():
#     assert 3 * 5 == 15, "Should Be 15"


# def test_add_two():
#     assert 3 * 5 == 16, "Should Be 15"


# if __name__ == "__main__":
#     test_add_one() # Return Nothing Since Passed The Test Case
#     test_add_two() # Return AssertionError: Should Be 15 Since Not Passed The Test Case
#     print("All Tests Passed")

# import unittest


# class TestAdd(unittest.TestCase):
#     def test_add_one(
#         self,
#     ):  # self is the instance of the class TestAdd and it is used to access the attributes and methods of the class
#         self.assertTrue(
#             3 < 5, "Should Be True"
#         )  # Explain line of code is self.assertTrue(3 < 5, "Should Be True") Return True Since Is The Condition True And No Error Raised
#         # Here Compare 3 < 5 And True

#     def test_add_two(self):
#         self.assertEqual(
#             3 + 5, 8, "Should Be 8"
#         )  # Explain line of code is self.assertEqual(3 + 5, 8, "Should Be 8") Return True Since 3 + 5 == 8 And No Error Raised
#         # Here Compare 3 + 5 == 8 And True

#     def test_add_three(self):
#         self.assertGreater(
#             5, 3, "Should Be True"
#         )  # self.assertGreater(5 ,3 , "Should Be True") is the same as assert 5 > 3, "Should Be True"
#         # Explain line of code is self.assertGreater(5 ,3 , "Should Be True") Return True Since 5 > 3 And No Error Raised
#         # Here Compare 5 > 3 And True


# # ! so the test case is passed and the test report is Ran 3 tests in 0.001s OK

# if __name__ == "__main__":
#     unittest.main()  # unittest.main() run all the test cases


# ! Advanced_Lessons => Generate Random Serial Numbers --
# --------------------------------------------------------------------------------

# import random
# import string

# print(string.digits) # Return '0123456789'
# print(string.ascii_letters) # Return 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# print(string.ascii_lowercase) # Return 'abcdefghijklmnopqrstuvwxyz'
# print(string.ascii_uppercase) # Return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# def Generate_Serial_Number(length):
#     All_Characters = string.ascii_letters + string.digits
#     # print(
#     #     All_Characters
#     # )  # Return All_Characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#     Chars_Count = len(All_Characters)
#     # print(Chars_Count)  # Return Chars_Count = 62
#     Serial_List = []
#     while len(Serial_List) < length:
#         random_number = random.randint(
#             0, Chars_Count - 1
#         )  #  Chars_Count - 1 is the maximum number of characters in the string
#         random_char = All_Characters[random_number]
#         Serial_List.append(random_char)
#     print("".join(Serial_List))  # Return '0a1b2c3d4e5f6g7h8i9j0a1b2c3d4e5f6g7h8i9j0'


# Generate_Serial_Number(10)

# ! Flask Intro And Your First Page

# --------------------------------------------------------------------------------
# Flask Is A Macro Framework Built In Python
# --------------------------------------------------------------------------------
# - HTML => HyperText Markup Language
# - CSS => Cascading Style Sheets
# - JavaScript => A Programming Language
# - Python => A High-Level Programming Language
# --------------------------------------------------------------------------------

# from flask import Flask  # from flask import Flask is used to import the Flask class

# skills_app = Flask(
#     __name__
# )  # Flask(__name__) is used to create an instance of the Flask class


# @skills_app.route(
#     "/"
# )  # @skills_app.route("/") is used to create a route for the Flask app
# def HomePage():
#     return "Hello From Flask Framework"


# @skills_app.route(
#     "/Info"
# )  # @skills_app.route("/Info") is used to create a route for the Flask app and the route is Info
# def InfoPage():
#     return "Info Page From Flask Framework"


# if __name__ == "__main__":
#     skills_app.run(
#         debug=True,
#         port=9000,
#     )  # skills_app.run(debug=True) is used to run the Flask app and debug is True Acctivate Debug Mode

# ! Flask Create HTML Files
# --------------------------------------------------------------------------------

# from flask import (  # from flask import Flask is used to import the Flask class
#     Flask,
#     render_template,
# )  # and render_template is used to render the HTML file

# my_skills = [("HTML", 96, 1), ("CSS", 90, 1), ("JS", 80, 1)]

# skills_app = Flask(
#     __name__
# )  # Flask(__name__) is used to create an instance of the Flask class


# @skills_app.route(
#     "/"
# )  # @skills_app.route("/") is used to create a route for the Flask app
# def HomePage():
#     return render_template(
#         "HomePage.html",
#         pagetitle="Home Page",
#         test="Test From Home Page File Html",
#         custom_css="HomePage",
#     )  # render_template("HomePage.html") is used to render the HTML file


# @skills_app.route(
#     "/Add"
# )  # @skills_app.route("/Add") is used to create a route for the Flask app and the route is Add
# def AddPage():
#     return render_template(
#         "AddPage.html",
#         pagetitle="Add Page",
#         test="Test From Add Page File Html",
#         custom_css="AddPage",
#     )  # render_template("AddPage.html") is used to render the HTML file


# @skills_app.route("/Skills")
# def SkillsPage():
#     return render_template(
#         "SkillsPage.html",
#         pagetitle="Skills Page",
#         page_head="My Skills",
#         custom_css="SkillsPage",
#         description="This is my skills",
#         data=my_skills,
#     )


# @skills_app.route("/Info")
# def InfoPage():
#     return render_template(
#         "InfoPage.html",
#         pagetitle="Info Page",
#         test="Test From Info Page File Html",
#     )


# if __name__ == "__main__":
#     skills_app.run(
#         debug=True,
#         port=9000,
#     )  # skills_app.run(debug=True) is used to run the Flask app and debug is True Acctivate Debug Mode

# --------------------------------------------------------------------------------
# ! -- Numpy => Intro--
# --------------------------------------------------------------------------------
# - NumPy Is A-Python Third-Party Module To Deal With Arrays & Matrices
# - NumPy Stand- For Numerical Python
# - NumPy Is Open Source
# - NumPy-Support Dealing With Large Multidimensional Arrays & Matrices
# - NumPy Has Many Mathematical Functions To Deal With This Elements
# --------------------------------------------------------------------------------
# - Why We Use NumPy Array
# - Consume Less Memory
# - Very Fast Compared To Python List
# - Easy To Use
# - Support Element Wise Operation
# - Elements Are Stored Contiguous
# --------------------------------------------------------------------------------
# - Python Lists
# - Homogeneous => Can Contains The Same Type of Objects
# - Heterogeneous => Can Contains Different Types of Objects
# --------------------------------------------------------------------------------
# print(np.__version__)  # print the version of NumPy
# ! Numpy Create Array

# import numpy as np

# my_list = [1, 2, 3, 4, 5]
# my_array = np.array(my_list)

# print(my_list)
# print(my_array)

# print("#" * 40)

# print(type(my_list))  # <class 'list'> number of dimensions list
# print(type(my_array))  # <class 'numpy.ndarray'> number of dimensions array

# print("#" * 40)

# print(my_list[0])  # 1 (accessing the first element of the list)
# print(my_array[0])  # 1 (accessing the first element of the array)

# print("#" * 40)

# a = np.array(10)  # create a zero dimensions araay
# b = np.array([20, 10])  # create a one dimensions araay
# c = np.array([[30, 20], [40, 30]])  # create a two dimensions araay
# d = np.array(
#     [[[70, 9], [80, 6]], [[90, 3], [100, 1]]]
# )  # create a three dimensions araay

# print(
#     d[1][1][0]
# )  # 3 (accessing the first element of the third list of the three dimensions araay)
# # d[1][1][0] is the same as d[1, 1, 0]

# print("#" * 40)

# print(a.ndim)  # 0 (number of dimensions of the araay)
# print(b.ndim)  # 1 (number of dimensions of the araay)
# print(c.ndim)  # 2 (number of dimensions of the araay)
# print(d.ndim)  # 3 (number of dimensions of the araay)

# print("#" * 40)

# my_custom_array = np.array(
#     [70, 9], ndmin=2
# )  # create a two dimensions araay with a minimum number of dimensions 2 call custom dimension
# print(my_custom_array)
# print(my_custom_array.ndim)  # 2 (number of dimensions of the araay)

# print("#" * 40)

# print(my_custom_array[0])  # [70, 9] (accessing the first element of the araay)
# print(my_custom_array[0, 1])  # 9 (accessing the first element of the araay)
# print(my_custom_array[0, 0])  # 70 (accessing the second element of the araay)

# --------------------------------------------------------------------------------
# ! -- Numpy => Compare Data locations And Types--
# --------------------------------------------------------------------------------

# import numpy as np

# my_list = [1, 2, 3, 4, 5]
# my_array = np.array([1, 2, 3, 4, 5])

# print(my_list[0])
# print(my_list[1])

# print(my_array[0])
# print(my_array[1])

# print("#" * 40)

# print(id(my_list[0]))  # return the memory address of the object
# print(id(my_list[1]))

# print(id(my_array[0]))  # return the memory address of the object
# print(id(my_array[1]))

# print("#" * 40)

# my_list_of_data = [1, 2, "A", "B", True, 10.5]
# my_array_of_data = np.array([1, 2, "A", "B", True, 10.5])

# print(my_list_of_data)
# print(my_array_of_data)

# print("#" * 40)

# print(my_list_of_data[0])
# print(my_array_of_data[0])

# print(type(my_list_of_data[0]))  # <class 'int'>
# print(type(my_array_of_data[0]))  # <class 'numpy.str_'>

# print("#" * 40)

# my_list_of_data = [1, 2, "A", "B", True, 10.5]
# my_array_of_data = np.array([1, 2])

# print(type(my_list_of_data[0]))  # <class 'int'>
# print(type(my_array_of_data[0]))  # <class 'numpy.int64'>

# ! -- Numpy => compare performance and memory usage --

# import time

# import sys  # sys is a module that provides access to some variables used

# or maintained by the Python interpreter and to functions that interact strongly with the interpreter
# import numpy as np

# elements = 10000000

# my_list1 = range(elements)  # Create a list of numbers from 0 to elements-1 (10000000)

# my_list2 = range(elements)

# list_start = time.time()  # Start the timer for the list operation time.time() record the time when the operation starts
# list_result = [
#     (l1 + l2) for l1, l2 in zip(my_list1, my_list2)
# ]  # do loop operation and return the result in a list and sort the list

# print(
#     f"List Time: {time.time() - list_start}"
# )  # print the time of the list operation to musure performance

# my_array1 = np.arange(
#     elements
# )  # Create a numpy array of numbers from 0 to elements-1 (10000000)

# my_array2 = np.arange(elements)

# array_start = time.time()

# array_result = my_array1 + my_array2  # srort the two arrays

# print(
#     f"Array Time: {time.time() - array_start}"
# )  # print the time of the array operation to musure performance

# # print(list_result)
# # print(array_result)

# # for l1, l2 in zip(my_list1, my_list2):
# #     print(l1 + l2)

# my_array = np.arange(100)
# print(my_array)
# print(my_array.itemsize)  # return the size of the data type of the array in bytes
# print(my_array.size)  # return the number of elements in the array
# print(
#     f"All Bytes Of Array : {my_array.itemsize * my_array.size}"
# )  # return the total number of bytes in the array
# print(my_array.nbytes)  # return the total number of bytes in the array

# print(my_array.nbytes)  # return the total number of bytes in the array
# print(my_array.shape)  # return the shape of the array
# print(my_array.ndim)  # return the number of dimensions of the array
# print(my_array.dtype)  # return the data type of the array
# print(my_array.flags)  # return the flags of the array
# print(my_array.flat)  # return a 1-D iterator over the array
# print(my_array.flatten())  # return a copy of the array flattened to one dimension
# print(my_array.T)  # return a copy of the array with the same data type, but with the rows and columns reversed
# print(my_array.transpose())  # return a copy of the array with the same data type, but with the rows and columns reversed

# my_array = np.arange(100).reshape((10, 10))  # create a two dimensional array

# print("#" * 40)

# My_list = range(100)
# # for i in My_list:
# #     print(i)

# print(len(My_list))  # return the number of elements in the list

# print(
#     f" Bytes OF One Element: {sys.getsizeof(My_list[0])}"
# )  # return the total number of bytes in the list

# print(
#     f"All Bytes OF List : {sys.getsizeof(My_list) * len(My_list)}"
# )  # return the total number of bytes in the list

# ! Numpy => Array Sclicing
# import numpy as np

# my_array = np.array(["A", "C", "D", "E", "F", "G", "H", "I", "J"])


# print(my_array[1])  # return the element of the array from the index 1
# print(my_array.ndim)  # return the number of dimensions of the array
# print(my_array[1:4])  # return the elements of the array from the index 1 to the index 4
# print(
#     my_array[1:4:2]
# )  # return the elements of the array from the index 1 to the index 4 with a step of 2
# print(
#     my_array[1::2]
# )  # return the elements of the array from the index 1 to the last index with a step of 2
# print(
#     my_array[::2]
# )  # return the elements of the array from the first index to the last index with a step of 2

# print("#" * 40)

# my_array2 = np.array(
#     [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"], ["J", "K", "L"]]
# )  # create a Two Dimensional Array
# print(my_array2.ndim)  # return the number of dimensions of the array

# print(
#     my_array2[1]
# )  # return the element of the array from the index 1 Who is a list ["D", "E", "F"]

# print("#" * 40)

# print(
#     my_array2[:3, 0:2]
#     # return the elements of the array from the first index to the index 3 which is [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
#     # and return the elements of the array from the first index to the index 2 which is [["A", "B",], ["D", "E"]]
# )

# print("#" * 40)

# print(
#     my_array2[1::, 0:2]
# )  # return the list of the list from the index 1 to the last index with a step of 2 which is [["D", "E", "F"], ["G", "H", "I"], ["J", "K", "L"]]
# # and return the elements of the array from the first index to the index 2 which is [['D' 'E']['G' 'H']['J' 'K']]


# print("#" * 40)


# print(
#     my_array2[1][1:3]
# )  # return the element of the List Of List From the index 1 Who is a list ["D", "E", "F"]
# # and return the elements of the list from the index 1 to the index 3 which is ["E", "F"]

# ! --Numpy => Data Type And COntrol Array --
# -------------------------------------------------------------------------------------
# https://numpy.org/devdocs/user/basics.types.html
# https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html#specifying-and-construc
# -------------------------------------------------------------------------------------
# '?' boolean
# 'b'- (signed) byte
# 'B' unsigned byte
# 'i'- (signed) integer
# 'u'- unsigned integer
# 'f' floating-point
# 'c'-complex-floating point
# 'm" timedelta
# 'M' -datetime
# -o'. (Python) objects
# 'S', 'a'-zero-terminated bytes• (not recommended)
# 'U' Unicode string
# 'V raw data (void)
# -------------------------------------------------------------------------------------

# import numpy as np

# # show array data type

# my_array1 = np.array([1, 2, 3])
# my_array2 = np.array([1.5, 2.5, 3.5])
# my_array3 = np.array(["Ah", "B", "Doaa"])

# print(my_array1.dtype)  # return the data type of the array which is int6
# print(my_array2.dtype)  # return the data type of the array which is float64
# print(
#     my_array3.dtype
# )  # return the data type of the array which is <U4 (unicode) 4 bytes> Of The Groth string In The Array Which Is Doaa

# print("#" * 40)

# # Create A Array With Specific Data Type

# my_array4 = np.array(
#     [1, 2, 3], dtype=int
# )  # create a array with the data type of int Or 'i' Or 'int'
# my_array5 = np.array(
#     [1.5, 2.5, 3.5], dtype=float
# )  # create a array with the data type of float Or 'f' Or 'float'
# my_array6 = np.array(
#     ["Ah", "B", "Doaa"], dtype=str
# )  # create a array with the data type of str (string)

# print(my_array4.dtype)
# print(my_array5.dtype)
# print(my_array6.dtype)

# # Change The Data Type Of An Array

# print("#" * 40)

# my_array7 = np.array([0, 1, 2, 3, 0, 4])

# print(my_array7.dtype)  # return the data type of the array which is int64
# print(my_array7)

# print("#" * 40)

# my_array7 = my_array7.astype(float)  # change the data type of the array to float

# print(my_array7.dtype)  # return the data type of the array which is float64
# print(my_array7)

# print("#" * 40)

# my_array7 = my_array7.astype(bool)  # change the data type of the array to bool

# print(my_array7.dtype)  # return the data type of the array which is bool (boolean)
# print(my_array7)

# print("#" * 40)

# # Test Capacity Of An Array

# my_array8 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=float)

# print(my_array8.dtype)  # return the data type of the array which is float64
# print(my_array8[0].itemsize)  # return the size of the data type of the array in bytes = 8

# print("#" * 40)

# my_array8 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype='f')

# print(my_array8.dtype)  # return the data type of the array which is float32
# print(my_array8[0].itemsize)  # return the size of the data type of the array in bytes = 4

# -------------------------------------------------------------------------------------
# ! --Numpy => Arithmetic And Usful Operations --
# -------------------------------------------------------------------------------------

# - Addition
# - Subtraction
# - Multiplication
# - Division
# ------------------------------------------------
# - Min
# - Max
# - Sum
# - Revel => Return Flattened Array 1 Dimension With Same Type Of Data
# ------------------------------------------------

# import numpy as np

# # Arithmetic Operations With One Dimension Array
# my_array1 = np.array([1, 2, 3, 4, 5])
# my_array2 = np.array([10, 20, 30, 40, 50])
# print(
#     my_array1 + my_array2
# )  # return the sum of the two arrays in the same order as the arrays [11, 22, 33, 44, 55]
# print(
#     my_array1 - my_array2
# )  # return the difference of the two arrays in the same order as the arrays [-9, -18, -27, -36, -45]
# print(
#     my_array1 * my_array2
# )  # return the product of the two arrays in the same order as the arrays [10, 40, 90, 160, 250]
# print(
#     my_array1 / my_array2
# )  # return the quotient of the two arrays in the same order as the arrays [0.1, 0.2, 0.3, 0.4, 0.5]

# print("#" * 40)

# # Arithmetic Operations With Two Dimension Array

# my_array3 = np.array(
#     [[1, 2, 3, 4, 5], [16, 17, 18, 19, 20]]
# )  # create a two dimensions araay

# my_array4 = np.array(
#     [[10, 20, 30, 40, 50], [1, 2, 3, 4, 5]]
# )  # create a two dimensions araay

# print(
#     my_array3 + my_array4
# )  # return the sum of the two arrays in the same order as the arrays [[11, 22, 33, 44, 55], [17, 19, 21, 23, 25]]
# print(
#     my_array3 - my_array4
# )  # return the difference of the two arrays in the same order as the arrays [[-9, -18, -27, -36, -45], [ 15  15  15  15  15]]
# print(
#     my_array3 * my_array4
# )  # return the product of the two arrays in the same order as the arrays [[ 10  40  90 160 250]] [ 16  34  54  76 100]]
# print(
#     my_array3 / my_array4
# )  # return the quotient of the two arrays in the same order as the arrays [[0.1, 0.1, 0.1, 0.1, 0.1], [16., 8.5, 6., 4.75 ,4.]]

# print("#" * 40)

# Min, Max, Sum, Revel => Return Flattened Array 1 Dimension With Same Type Of Data

# my_array5 = np.array([1, 2, 3, 4, 5])

# print(my_array5.min())  # return the minimum value of the array which is 1
# print(my_array5.max())  # return the maximum value of the array which is 5
# print(my_array5.sum())  # return the sum of the array which is 15
# print(
#     my_array5.ravel()
# )  # return the flattened array which is [1, 2, 3, 4, 5] Reval => Return Flattened Array 1 Dimension With Same Type Of Data

# print("#" * 40)

# my_array6 = np.array(
#     [[1, 2, 3, 4, 5], [16, 17, 18, 19, 20]]
# )  # create a two dimensions araay

# print(my_array6.min())  # return the minimum value of the array which is 1
# print(my_array6.max())  # return the maximum value of the array which is 20
# print(my_array6.sum())  # return the sum of the array which is 101
# print(
#     my_array6.ravel()
# )  # return the flattened array which is [1, 2, 3, 4, 5, 16, 17, 18, 19, 20] Reval => Return Flattened Array 1 Dimension With Same Type Of Data

# print("#" * 40)

# print(my_array6.ndim)  # return the number of dimensions of the array which is 2

# print("#" * 40)

# x = my_array6.ravel()  # convert the array to one dimension

# print(x.ndim)  # return the number of dimensions of the array which is 1

# -------------------------------------------------------------------------------------
# ! --Numpy => Shape And Reshape --
# -------------------------------------------------------------------------------------

# import numpy as np

# my_array1 = np.array([1, 2, 3, 4, 5])

# print(my_array1.ndim)  # return the number of dimensions of the array which is 1
# print(my_array1.shape)  # return the shape of the array which is (5,)

# print("#" * 40)

# my_array2 = np.array(
#     [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# )  # create a two dimensions araay

# print(my_array2.ndim)  # return the number of dimensions of the array which is 2
# print(my_array2.shape)  # return the shape of the array which is (3, 4)
# # which is (number of rows, number of columns) 3 num of araay and 4 num of elements in each araay

# print("#" * 40)

# my_array3 = np.array(
#     [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
# )  # create a three dimensions araay

# print(my_array3.ndim)  # return the number of dimensions of the array which is 3
# print(my_array3.shape)  # return the shape of the array which is (2, 2, 3)
# # which is (number of rows, number of columns, number of elements in each araay)
# # 2 num of araay and 2 num of array in each araay and 3 num of elements in each araay

# print("#" * 40)

# # Reshape

# my_array4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# print(my_array4.ndim)  # return the number of dimensions of the array which is 1
# print(my_array4.shape)  # return the shape of the array which is (12,)
# print(
#     my_array4.reshape(3, 4)
# )  # return the reshaped array which is [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# x = my_array4.reshape(3, 4)
# print(x.shape)  # return the shape of the array which is (3, 4)

# print("#" * 40)

# my_array5 = np.array(
#     [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
# )  # create a two dimensions araay

# print(my_array5.ndim)  # return the number of dimensions of the array which is 2
# print(my_array5.shape)  # return the shape of the array which is (2, 10)

# print("#" * 40)

# # print(my_array5.reshape(-1))
# # y = my_array5.reshape(-1)
# # print(my_array5.reshape(5, 4))
# # y = my_array5.reshape(5, 4)
# print(my_array5.reshape(2, 5, 2))
# y = my_array5.reshape(2, 5, 2)
# print(y.ndim)  # return the number of dimensions of the array which is 1
# print(y.shape)  # return the shape of the array which is (20,)

# print("#" * 40)

# -------------------------------------------------------------------------------------
# ! Virsual Environment Part One
# -------------------------------------------------------------------------------------

# import pyfiglet
# import termcolor

# print(termcolor.colored(pyfiglet.figlet_format("Finalnaly", font="slant"), color="red"))


# ======================================================================================
# New Part
# ======================================================================================

# A, B, C = [1, 2, 3]

# print(f"A = {A} , B = {B} , C = {C}")

# ! Extending Itrerable Unpacking With *args

# a, b, *c = [
#     1,
#     2,
#     3,
#     4,
#     5,
# ]  # * c create a list from the list c and return the list in the same order as the list c

# print(f"a = {a} , b = {b} , c = {c}")  # a = 1 , b = 2 , c = [3, 4, 5]

# # ! Ignoring Values

# a, _, c = [1, 2, 3]  # a = 1 , c = 3
# _, _, c = [1, 2, 3]  # c = 3

# print(f"a = {a} , c = {c}")  # a = 1 , c = 3

# ! Unpacking In Functions Arguments


# data = ("Alice", (25, "New York"))
# nama, (age, location) = data  # nama = Alice , age = 25 , location = New York


# def print_name_and_location(*names):
#     for name in names:
#         print(f"Name: {name} , Location: {location}")


# print_name_and_location("Mahmoud", "Elsayed", "Mahmoud")

# ! Combining List with Unpacking
# list1 = [1, 2, 3, 4, 5]
# list2 = [10, 20, 30, 40, 50]

# print(
#     f"Combined List: {*list1, *list2}"
# )  # Combined List: (1 2 3 4 5 10 20 30 40 50) in the same order as the list
# # do unpacking and return the elements of the list in the same order as the list

# ! unpacking dictionary with **
# dict1 = {"name": "Mahmoud", "age": 36, "country": "Egypt"}
# dict2 = {"name": "Elsayed", "age": 36, "country": "Egypt"}

# combined_dict = {**dict1, **dict2}

# print(
#     f"Combined Dict: {combined_dict}\n"
# )  # Combined Dict: this will return the combined dictionary in the same order as the dictionary dict1 and dict2

# ! swaping two variables

# x = 10
# y = 20
# print(f"Before Swapping x = {x} , y = {y}")
# x, y = y, x
# print(f"After Swapping x = {x} , y = {y}")


# ! demonstrating_exec used to execute the code in the string exce builtin function


# def demonstrating_exec():
#     code = """def great(name):
#     return f"Hello {name}!\""""
#     # instead of do this def great(name): return f"Hello {name}!\n" we can do this with exec function now such as string
#     # Execute The Code
#     local_scope = {}  # local_scope is a dictionary that will be used to store the variables and functions great and return
#     exec(
#         code, {}, local_scope
#     )  # exec(code, {}, local_scope) execute the code that is in the string code and store the variables and functions in the dictionary local_scope
#     # {} is the global scope (dictionary) that will be used to store the need code to be executed
#     print(local_scope["great"]("Mahmoud"))  # Hello Mahmoud


# demonstrating_exec()

# user_coed = input("Enter your code: ").strip()

# exec(user_coed)

# print(user_coed)


# def demonstrate_eval():
#     # evaluate the expression
#     expression = input("Enter your expression: ")

#     result = eval(expression) # eval(expression) evaluate the expression and return the result like as 3*5 = 15
#     #
#     print(f"The result of eval the expression is: {result}")

# demonstrate_eval()

# -------------------------------------------------------------------------------------------------------
# ! Safe Eval be safe yuo can use it to evaluate the expression and return the result so be careful
# -------------------------------------------------------------------------------------------------------
# Enter your expression: demonstrating_exec()
# Hello Mahmoud!
# The result of eval the expression is: None
# -------------------------------------------------------------------------------------------------------


# def demonstrate_safe_eval():
#     # evaluate the expression
#     expression = input("Enter your expression that use a , b and c: ")

#     # define the variables for the expression
#     variables = {"a": 1, "b": 2, "c": 3}

#     result = eval(
#         expression, {}, variables
#     )  # eval(expression, {} , variables) evaluate the expression and return the result

#     print(f"The result of safe eval the expression is: {result}")


# demonstrate_safe_eval()

# Function Annotations


# def greet(name: str, age: int) -> str:
#     """
#     Greet a person with their name and age.
#     Args:
#         name (str): The name of the person expected to be a string
#         age (int): The age of the person expected to be an integer
#     """
#     return f"Hello {name} your age is {age}"


# print(greet("Mahmoud", 36))

# ! Description Protocol


# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         """
#         __repr__ is meant to provide an unambiguous string representation of an object.
#         It,s often used for debugging purposes and should return a string that can be used to reconstruct the object.
#         """
#         return f"Person(name={self.name!r}, age={self.age!r})"

#     def __str__(self):
#         """
#         __str__ is used to provide a human-readable string representation of an object.
#         It is often used for printing or displaying the object or converting it to a string.
#         """
#         return f"Person(name={self.name}, age={self.age}) your age "


# person_one = person("Mahmoud", 36)
# repr(
#     person_one
# )  # return the string representation of the object person_one which is Person(name='Mahmoud', age=36) for debugging purposes and devlopers
# str(
#     person_one
# )  # return the string representation of the object person_one which is Person(name=Mahmoud, age=36) for printing or displaying the object or converting it to a string

# age = int(input("Enter your age:").strip())
# text = str(age)
# print(text)
# print(type(text))


# context manager
# class FileManager:
#     def __init__(
#         self, file_name, file_mode
#     ):  # file_name is the name of the file and file_mode is the mode of the file
#         self.file_name = file_name  # file_name is the name of the file is attribute of the class FileManager
#         self.file_mode = file_mode  # file_mode is the mode of the file is attribute of the class FileManager
#         self.file = (
#             None  # file is the file object is attribute of the class FileManager
#         )

#     def __enter__(
#         self,
#     ):  # __enter__ is used to enter the context of the class FileManager
#         self.file = open(
#             self.file_name, self.file_mode
#         )  # open the file and assign the file object to the attribute file of the class FileManager
#         print(
#             f"File {self.file_name} has been opened"
#         )  # print the message if the file has been opened
#         return self.file  # return the file object

#     def __exit__(
#         self, exc_type, exc_value, traceback
#     ):  # __exit__ is used to exit the context of the class FileManager
#         self.file.close()  # close the file
#         print(
#             f"File {self.file_name} has been closed"
#         )  # print the message if the file has been closed
#         if exc_type:  # if exc_type is not None
#             print(
#                 f"An error has occurred: {exc_value}"
#             )  # print the message if an error has occurred
#         return True  # return True


# Fileone = FileManager(
#     "file.txt", "w"
# )  # create a file manager object and assign the file name and mode to the attributes file_name and file_mode of the class FileManager
# Filetwo = FileManager(
#     "file.txt", "r"
# )  # create a file manager object and assign the file name and mode to the attributes file_name and file_mode of the class FileManager

# if __name__ == "__main__":
#     with (
#         Fileone as fileone
#     ):  # use the file manager object Fileone to open the file file.txt in write mode
#         fileone.write(
#             "Hello World!"
#         )  # write the content "Hello World!" to the file file.txt
#         print("file created successfully")
#     with (
#         Filetwo as filetwo
#     ):  # use the file manager object Filetwo to open the file file.txt in read mode
#         content = filetwo.read()
#         print("file read successfully and content is", content)
#         # read the file file.txt and print the content of the file

# import sys
# import time


# class range:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#         # self.step = step

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.start < self.stop:
#             self.start += (
#                 1  # increment the start value by 1 when the stop condition is not met
#             )
#             return (
#                 self.start
#             )  # return the next value of the range when the stop condition is not met
#         else:
#             raise StopIteration  # raise the StopIteration exception when the stop condition is met


# if __name__ == "__main__":
#     my_range = range(
#         1, 10000
#     )  # create a instance of the range class and pass the start, stop and step as arguments

#     start_time = time.time()

#     for i in (
#         my_range
#     ):  # use the range object to iterate over the range using the __iter__ method
#         My_list = [i]
#         print(i)

#     print(f"All Bytes OF List : {sys.getsizeof(My_list) * len(My_list)}")

#     print(f"Time Return Taken: {time.time() - start_time}")

# print("#" * 40)


# ! Generators
# import time


# def count_up_to(max_num):
#     """
#     A generator function that yields the numbers from 1 to max_num
#     why we use yield instead of return?
#     yield is used to return a value from a generator function
#     and not to store the value in a variable ex max_num = 10808080808
#     return is used to store the value in a variable ex max_num = 10808080808
#     but yield is used to return the value from a generator function without storing it in a variable
#     so we use yield instead of return to save memory
#     """
#     start_time = time.time()
#     current_num = 1
#     while current_num <= max_num:
#         yield current_num
#         current_num += 1
#     print(f"Time Taken: {time.time() - start_time}")


# if __name__ == "__main__":
#     my_generator = count_up_to(10000)
#     for i in my_generator:
#         print(i)

# ! iteratools
# import itertools  # itertools is a module in Python that provides functions for working with iterable objects

# counter = itertools.count(start=1, step=1)
# print(next(counter))  # 1
# print(next(counter))  # 2

# cyler = itertools.cycle(["A", "B", "C"])
# print(next(cyler))  # A
# print(next(cyler))  # B
# print(next(cyler))  # C
# print(next(cyler))  # A (the cycle starts again)

# zipper = itertools.zip_longest(
#     [
#         "a",
#         "b",
#     ],
#     [1, 2, 3],
#     fillvalue="x",
# )
# print(list(zipper))  # [('a', 1), ('b', 2), ('x', 3)]


# combinations = itertools.combinations(["a", "b", "c"], 2)
# print(list(combinations))  # [('a', 'b'), ('a', 'c'), ('b', 'c')]

# ! asyncio module
# # asyncio is a module in Python that provides support for asynchronous programming using coroutines and tasks
# # asyncio is a built-in module in Python 3.4 and later versions


# import asyncio


# async def fetch_data():  # fetch_data is an asynchronous function that runs concurrently with the main function
#     print("Fetching data...")
#     await asyncio.sleep(
#         2
#     )  # simulate a delay of 2 seconds (asyncio.sleep is a coroutine that suspends the execution of the current coroutine for the specified number of seconds)
#     print("Data fetched!")
#     return {"data": 42}  # return a dictionary with the key "data" and the value 42


# async def process_data(): # process_data is an asynchronous function that runs concurrently with the main function
#     print("Processing data...")
#     data = await fetch_data()  # await fetch_data() to wait for the result of the fetch_data() coroutine
#     print(f"process_data: {data['data']}")


# async def main():  # main is an asynchronous function that runs the coroutines in the order they are defined
#     print("Starting main...")
#     await process_data()  # await process_data() to wait for the result of the process_data() coroutine
#     print("Main finished!")


# if __name__ == "__main__":
#     asyncio.run(main())

# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------

# ! Namespaces And Scopes
# Namespaces are a way to organize and group related variables, functions, and classes in Python.
# Scopes are the context in which a variable or function is accessible.
# Scopes can be global, local, Build-in, Encapsulated, or LEGB Rules .

# ! global scope
# global variables are accessible from anywhere in the program
# global variables are declared outside of any function or class

# global_variable = 10  # global_variable is a global variable that can be accessed from anywhere in the program


# def global_function1():
#     # global global_variable  # global_variable is a global variable
#     global_variable = 20  # global_variable is a encapsulated variable
#     print(global_variable)

#     def global_function2():
#         nonlocal global_variable  # nonlocal global_variable is a nonlocal variable
#         global_variable = (
#             30  # Local variable is not accessible from outside the function
#         )
#         print(global_variable)

#     global_function2()
#     print(global_variable)  # print the encapsulated variable which is 30 since do nonlocal global_variable


# # print(global_variable)  # print the global variable which is 10
# global_function1()
# # print(global_variable)  # print the global variable which is 20

# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------

# ! Closures

# Closures are a way to create functions that have access to variables from the scope in which they were defined.
# Closures are created when a function is defined inside another function and the inner function references variables from the outer function.


# def outer_function():
#     saying = "Hey there!"  # saying is a free variable that can be accessed from inner_function
#     # not remove from the scope of outer_function since the inner used it

#     def inner_function():
#         return f"We Are The Knights Who Say {saying}"

#     return inner_function  # return the inner function (Closure)


# func1 = outer_function()  # call the outer function and assign the inner function to the variable func1 (Closure)
# print(
#     func1()
# )  # print the result of the inner function (Closure) which is "We Are The Knights Who Say Hey there!"
# print(
#     type(func1)
# )  # print the type of the inner function (Closure) which is <class 'function'>


# def counter(start):
#     def inc(step=1):
#         nonlocal start  # nonlocal start used to access the start variable from the outer function counter
#         start += step
#         print(start)

#     return inc


# func2 = counter(1)
# func2()  # print the start variable which is 1 and the step which is 1 so the start variable is now 1 + 1 = 2
# func2()  # print the start variable which is 1 and the step which is 1 so the start variable is now 1 + 2 = 3
# func2(10)  # 10 is the step of the function inc


# def counter2(start):
#     def inc(step=1):
#         nonlocal start  # nonlocal start used to access the start variable from the outer function counter
#         start += step
#         print(start)

#     inc()


# # the difference between the two functions is that the first function is a closure and the second function is not a closure
# # and closure saves the start variable in the outer function counter even if the counter function is finished executing
# counter2(1) # print the start variable which is 1 and the step which is 1 so the start variable is now 1 + 1 = 2
# counter2(1) # print the start variable which is 1 and the step which is 1 so the start variable is now 1 + 1 = 2

# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------
# ! Mutable and Immutable
# Mutable: Objects that can be changed after they are created and saved in the same memory location (e.g., a list, a dictionary, a set, etc.)
# Immutable: Objects that can be changed after they are created but not saved in the same memory location (e.g., a tuple, a string, a number, etc.)
# -------------------------------------------------------------------------------------------------------

# ! Mutable

# a = [1, 2, 3]  # a is a mutable list
# b = a  # b is a reference to the same list object in memory
# print(
#     f" id(a) = {id(a)} and id(b) = {id(b)}"
# )  # id(a) = 2887569728448 and id(b) = 2887569728448

# print(f"a = {a}")  # a = [1, 2, 3]
# print(f"b = {b}")  # b = [1, 2, 3]

# print("=" * 60)

# a.append(4)  # append an element to the list

# print(
#     f" id(a) = {id(a)} and id(b) = {id(b)}"
# )  # id(a) = 2887569728448 and id(b) = 2887569728448

# print(f"a = {a}")  # a = [1, 2, 3, 4]
# print(f"b = {b}")  # b = [1, 2, 3, 4]

# print("=" * 60)

# # ! Immutable

# c = (1, 2, 3)  # c is an immutable tuple
# d = c  # d is a reference to the same tuple object in memory
# print(
#     f" id(c) = {id(c)} and id(d) = {id(d)}"
# )  # id(c) = 2887569728448 and id(d) = 2887569728448

# print(f"c = {c}")  # c = (1, 2, 3)
# print(f"d = {d}")  # d = (1, 2, 3)

# print("=" * 60)

# c[0] = 4  # change the value of the first element of the tuple does not support item assignment

# print(f" id(c) = {id(c)} and id(d) = {id(d)}")

# -------------------------------------------------------------------------------------------------------

# ! Copy And Deep Copy And Shallow Copy

#  Shallow Copy => Copy the list and the elements of the list and change do in first level of the list but not in the second level of the list
#  Deep Copy => Copy the list and the elements of the list and change not in first level of the list and not in the second level of the list

# x = [1, 2, 3, 10, [20, 30]]
# z = x  # z is a reference to the same list object in memory
# print((id(x), id(z)))  # (2887569728448, 2887569728448)

# ! Shallow Copy Of The List Constructor

# zz = list(x)  # zz is a Shallow copy of the list x

# print(
#     f" id(x) = {id(x)} and id(zz) = {id(zz)}"
# )  # (2401480310848, 2401480673984) the id of the list x is different from the id of zz

# zz.remove(10)  # remove the element 10 from the list zz since the list zz is a shallow copy of the list x

# print(f"x = {x}")  # x = [1, 2, 3, 10, [20, 30]]
# print(f"zz = {zz}")  # zz = [1, 2, 3, [20, 30]]

# -------------------------------------------------------------------------------------------------------

# ! Shallow Copy Of The Import Copy Module

# import copy

# y = copy.copy(x)  # y is a copy of the list x
# print(f" id(x) = {id(x)} and id(y) = {id(y)}")

# print(f"x = {x}")  # x = [1, 2, 3, 10, [20, 30]]
# print(f"y = {y}")  # y = [1, 2, 3, 10, [20, 30]]

# y[4][0] = 100  # change the value of the first element of the list y

# print(f" x = {(x)} and y = {(y)}")  # x = [1, 2, 3, 10, [100, 30]] and y = [1, 2, 3, 10, [100 , 30]] x  changed

# print("=" * 60)

# -------------------------------------------------------------------------------------------------------

# ! Deep Copy

# l = copy.deepcopy(x)  # y is a deep copy of the list x
# print(f" id(x) = {id(x)} and id(l) = {id(l)}")

# print(f"x = {x}")  # x = [1, 2, 3, 10, [20, 30]]
# print(f"l = {l}")  # y = [1, 2, 3, 10, [20, 30]]

# l[4][0] = 100  # change the value of the first element of the list y

# print(f" x = {(x)} and l = {(l)}")  # x = [1, 2, 3, 10, [20, 30]] and l = [1, 2, 3, 10, [100, 30]] x not changed

# print("=" * 60)


# create fun to deep copy list

# ! Descriptors Real Python
# TAKING CONTROL OF WHAT HAPPEN WHEN ATTRIBUE ARE BEING USED
# The descriptor purpose is to create your own magic.
# (Magic) You decide what happens when class attributes are accessed using the dot notation(.)
# ------------------------------------------------
# Descriptor
#     ↓
# أنت تحدد الـBehavior
#     ↓
# Python تنفذه عند التعامل مع Attribute
# -------------------------------------------------

# -------------------------------------------------
# Descriptor
# ↓
# يتحكم في سلوك dot notation
# ↓
# ------------------------------------------------
# https://realpython.com/python-descriptors/
# https://docs.python.org/3/howto/des

# ------------------------------------------------
# Descriptors Protocol Meyhods (Dunder Methods)
# ------------------------------------------------

# __get__ (self, obj, objtype=None)
# __set__ (self, obj, value)
# __delete__ (self, obj)
# __set_name__ (self, owner, name)

# class MyObject:
#     def hello(self):
#         print("Hello")

# obj = MyObject()  # obj (obj is an instance of MyObject.)is a reference to the class MyObject and he is (object)

# obj.hello() # obj.hello() is a method call on the object obj and it is (method)

# class myclass():
#     attribute = obj # attribute is a reference to the object obj and it

# obj2 = myclass()

# obj2.attribute.hello() # obj2.attribute.hello() is a method call on the object obj2.attribute and it is (


# # ! Descriptor Class
# class MyDescriptor:
#     def __get__(self, obj, objtype=None):
#         pass

# class MyClass:
#     class_attribute = MyDescriptor()


# class Song:
#     def __init__(self, title, artist):
#         self.validate_string(title)
#         self.validate_string(artist)

#         self.title = title
#         self.artist = artist

#     def __str__(self):
#         return f"This is {self.title} by {self.artist}"
#     # this is not the best way to validate string because it is not reusable
#     def validate_string(self, value):
#         if not isinstance(value, str):
#             raise ValueError("Value must be a string")


# song = Song("Bohemian", "Rush")
# s = Song("1234", "John")

# print(str(song))  # Bohemian by Rush
# print(str(s))


# class StringValidation:
#     def __get__(
#         self, obj, objtype=None
#     ):  # obj يمثل الـ object الذي الـ Descriptor متصل به. (song instance)
#         print("__get__(): Accessing '_title'")
#         return obj._title

#     def __set__(self, obj, value):
#         if isinstance(value, str):
#             if len(value) > 2:
#                 print(f"__set__(): Updating '_title' to '{value}'")
#                 obj._title = value
#             else:
#                 raise ValueError(
#                     f"{value}Title must be a string with more than 2 characters"
#                 )
#         else:
#             raise ValueError(
#                 f"{value}Title must be a string with more than 2 characters"
#             )


# class Song:
#     title = StringValidation()
#     # artist = StringValidation()

#     def __init__(self, title, artist):
#         self.title = title
#         self.artist = artist

#     def __str__(self):
#         return f"This is {self.title} by {self.artist}"

#             self.value
# → stored in the Descriptor
# → shared by instances
# → usually problematic for instance-specific data

# obj._title
# → stored in the actual object
# → each object gets its own value
# → avoids sharing the value between instances


# s1 = Song("Bohemian", "Rush")
# print(str(s1))  # This is Bohemian by Rush
# print(s1.title)  # Bohemian
# print(s1.artist)  # Rush

# #                 Song
#                  │
#                  │
#           title = StringValidator()
#                  │
#         ┌────────┴────────┐
#         │                 │
#      SET               GET
#         │                 │
#    __set__()          __get__()

# -------------------------------------

#      StringValidator
#            │
#            │
#           self
#            │
#            ▼
#   ┌─────────────────┐
#   │   Descriptor    │
#   └─────────────────┘
#            │
#            │ attached to
#            ▼
#         Song
#            │
#            ▼
#           obj
#            │
#            ▼
#           s1

# -------------------------------------------

# SET

#         s1.title = ""Bohemian" , s1.artist = "Rush"
#     │
#     ▼
# __set__()
#     │
#     ├── self  → StringValidator()
#     ├── obj   → s1
#     └── value → "Bohemian" , "Rush"

# ------------------------------------------

# GET

#             s1.title
#    │
#    ▼
# __get__()
#    │
#    ├── self     → StringValidator()
#    ├── obj      → s1
#    └── objtype  → Song

# class ValidatatorString :

#     def __set__(self,obj, value):
#         if isinstance(value,str):
#             if len(value) > 2:
#                 print(f"__set__(): Updating '_title' to '{value}'")
#                 print(f"'{self.private_name}' to '{value}'")
#                 setattr(obj,self.private_name,value)
#             else:
#                 raise ValueError(f"{value}Title must be a string with more than 2 characters")
#         else:
#             raise ValueError(f"{value}Title must be a string with more than 2 characters")

#     def __get__(self,obj,objtype=None):
#         print("__get__(): Accessing '_title'")
#         return getattr(obj,self.private_name)

#     def __set_name__(self,owner,name):
#         self.private_name = f"_{name}"
# class Song:
#     title = ValidatatorString()
#     artist = ValidatatorString()
#     def __init__(self,title,artist):
#         self.title = title
#         self.artist = artist
#     def __str__(self):
#         return f"This is {self.title} by {self.artist}"

# s1 = Song("Bohemian", "Rush")
# print(str(s1))  # This is Bohemian by Rush
# print(s1.title)  # Bohemian
# print(s1.artist)  # Rush
# ------------------------------------------------------------
# ! Protocol
# The protocol defines a set of methods that an object should provide.
# Name three static type checkers mentioned. mypy Pyright Pyre
# Concept                    	Meaning
# Biological classification	الكائن بينتمي لأي مجموعة بيولوجية؟
# Behavior	الكائن يقدر يعمل إيه؟

# الـ inheritance ممتاز في تمثيل التصنيف والعلاقات، لكنه مش دايمًا أفضل وسيلة لتنظيم السلوكيات اللي بتتكرر عبر فئات مختلفة.

# ودي نقطة الدكتور الأساسية في الجزء ده.
# The behaviors do not need to be tied directly to the class hierarchy.

# بالعربي:

# بدل ما نربط كل قدرة حركية بفئة بيولوجية محددة، نقدر نوصف القدرات دي بصورة مستقلة.

# يعني بدل ما نسأل:

# Is this object a bird or a fish?

# نسأل:

# Can this object fly? Can it swim? Can it dive?

# Biological hierarchy:

# Animal
# ├── Mammal
# ├── Fish
# └── Bird


# Behaviors:

# Walker
# Swimmer
# Diver
# Flyer
# ! Objects can share behaviors without sharing the same parent class.
# إحنا مش عايزين نربط كل سلوك بـ class معينة.
# ------------------------------------------------------------
# عملنا ثلاث classes مستقلة.

# لاحظ إننا لم نستخدم inheritance بينهم.

# ومع ذلك، كل واحدة عندها method اسمها fly().

# نقدر نعمل objects ونستدعي نفس الـ method:
# class Bird:
#     def fly(self):
#         print("Bird is flying")


# class Airplane:
#     def fly(self):
#         print("Airplane is flying")


# class FlyingFish:
#     def fly(self):
#         print("Flying fish is gliding")

# bird = Bird()
# plane = Airplane()
# fish = FlyingFish()

# bird.fly()
# plane.fly()
# fish.fly()

# Walker للسلوكيات المتعلقة بالمشي والجري.
# Swimmer للسلوكيات المتعلقة بالسباحة والغوص.
# Flyer للسلوكيات المتعلقة بالطيران.

# English — The core idea

# A protocol defines the methods that an object is expected to provide.

# الشرح بالعربي:

# الـ Protocol بيحدد الـ methods اللي الـ object المفروض يوفرها عشان يكون متوافقًا مع النوع ده.

# خلي بالك من كلمة expected.

# إحنا بنوصف السلوك المطلوب، مش بنكتب بالضرورة الكود المسؤول عن تنفيذ السلوك نفسه.

# وده الفرق اللي هنفهمه من الكود الجاي.

# from typing import Protocol

# class Walker(Protocol):
#     def walk(self, destination: str) -> None:
#         ...
#     def run(self, destination: str) -> None:
#         ...
# class Swimmer(Protocol):
#     def swim(self, destination: str) -> None:
#         ...
#     def dive(self, depth: float) -> None:
#         ...

# Concept	المعنى
# Protocol	أداة لتعريف مجموعة من السلوكيات المطلوبة.
# Method signature	وصف اسم الـ method والـ parameters والـ return type.
# ...	بيمثل عدم كتابة تنفيذ للـ method في تعريف الـ Protocol.
# Structural Subtyping	توافق الـ object مع الـ Protocol بناءً على بنيته وسلوكياته المطلوبة، مش على الوراثة منه بالضرورة.
# ! The key idea: An object must provide all the required protocol members with compatible types.

# from typing import Protocol


# class Flyer(Protocol):
#     def fly(self, destination: str) -> None: ...
#     def take_off(self) -> None: ...
#     def land(self,destination: str) -> None: ...


# class Airplane:
#     def fly(self, destination: str) -> None:
#         print(f"Flying to {destination}")

#     def take_off(self) -> None:
#         print("Airplane taking off")

#     def land(self, destination: str) -> None:
#         print(f"Airplane landing at {destination}")


# def send_flying(obj: Flyer) -> None:
#     obj.take_off()
#     obj.fly("Cairo")
#     obj.land("New York")


# class Drone:
#     def fly(self, destination: str) -> None:
#         print(f"Flying to {destination}")

#     def take_off(self) -> None:
#         print("Taking off")

#     def land(self, destination: str) -> None:
#         print(f"Drone landing On {destination}")


# # plane = Airplane()
# send_flying(Airplane())
# send_flying(
#     Drone()
# )  # Not all methods are implemented in Drone class, so it will raise an error if we try to call send_flying with a Drone instance.

# ! PROTOCOLS IN PYTHON

# PROBLEM:
# Inheritance is not always enough to describe object behaviors.
# Example:
# - A whale is a mammal, but cannot walk like a dog.
# - A penguin is a bird, but cannot fly.
# - An airplane can fly, although it is not a bird.
# Putting every behavior inside a class can be incorrect because
# objects in the same category may have different abilities.
# Different classes can also share the same behavior.
# SOLUTION:
# A Protocol describes the methods an object is expected to provide.
# It focuses on WHAT AN OBJECT CAN DO, not which class it inherits from.
# Example:
# from typing import Protocol
# class Flyer(Protocol):
# def fly(self) -> None:
# ...
# class Bird:
# def fly(self) -> None:
# print("Bird is flying")
# class Airplane:
# def fly(self) -> None:
# print("Airplane is flying")

# Bird and Airplane can both satisfy Flyer because both provide
# a compatible fly() method. Explicit inheritance is not required.
# The Protocol describes the required interface; each class
# implements its own behavior.
# KEY DIFFERENCE:
# Inheritance -> Relationships between classes.
# Protocol    -> Expected behavior of objects.
# STRUCTURAL SUBTYPING:
# Compatibility depends on the methods and attributes an object
# provides, rather than requiring explicit inheritance.
# REMEMBER:
# Inheritance describes what a class IS related to.
# Protocols describe what an object CAN DO.
# ------------------------------------------------------------------------------
# from typing import Protocol


# class Notifier(Protocol):
#     def notify(self, message: str) -> None: ...


# class EmailNotifier:
#     def notify(self, message: str) -> None:
#         print(f"Sending email notification: {message}")


# class SMSNotifier:
#     def notify(self, message: str) -> None:
#         print(f"Sending SMS notification: {message}")


# class PushNotifier:
#     def notify(self, message: str) -> None:
#         print(f"Sending push notification: {message}")


# class WhatsAppNotifier:
#     def notify(self, message: str) -> None:
#         print(f"Sending WhatsApp message: {message}")


# def send_notification(obj: Notifier, message: str) -> None:
#     obj.notify(message)


# class BrokenNotifier:
#     def send(self, message: str) -> None:
#         print(message)


# send_notification(EmailNotifier(), "Hello via Email!")
# send_notification(SMSNotifier(), "Hello via SMS!")
# send_notification(PushNotifier(), "Hello via Push Notification!")
# send_notification(WhatsAppNotifier(), "Hello via WhatsApp!")
# send_notification(
#     BrokenNotifier(), "Hello via Broken Notifier!"
# )  # This will raise an error because BrokenNotifier does not implement the notify method.


# from typing import Protocol, TypeVar

# T = TypeVar(
#     "T"
# )  # T: بيمثل نوعًا هيتحدد حسب الاستخدام؛ ممكن يكون int أو str أو نوعًا آخر.


# class Reader(Protocol[T]):
#     def read(self) -> T:  # -> T: القيمة المرجعة لازم يتوافق نوعها مع T.
#         ...


# class NumberReader:
#     def read(self) -> int:
#         return 100


# class TextReader:
#     def read(self) -> str:
#         return "Hello Python"


# def process_reader(
#     reader: Reader[T],
# ) -> T:  # reader: Reader[T]: بنحدد إن الكائن لازم يكون متوافقًا مع Reader، وإن نوع القيمة مرتبط بـ T.
#     return reader.read()


# number_reader = NumberReader()
# text_reader = TextReader()

# number = process_reader(number_reader)
# text = process_reader(text_reader)

# print(number)
# print(type(number))

# print(text)
# print(type(text))


# ===============================================================
# ! Pure Function
# ===============================================================
# def Remove_My_List(MyList: list) -> list:
#     """
#     Remove the last elements of the list and return list.
#     Args:
#         MyList (list): The list to be removed
#     Returns:
#         list: A new list with the last element removed
#     """
#     MyList.pop(-1)  # remove the last element of the list


# number_list = [1, 2, 3, 4, 5]
# print(number_list)  # [1, 2, 3, 4, 5]
# for i in range(len(number_list)):
#     Remove_My_List(number_list)
#     print(number_list)  # [1, 2, 3, 4], [1, 2, 3], [1, 2], [1], []

# def butlast (MyList: list) -> list:
#     """
#     Return a new list with the last element removed.
#     Args:
#         MyList (list): The list to be removed
#     Returns:
#         list: A new list with the last element removed
#     """
#     return MyList[:-1]  # return a new list with the last element removed
# Num_List = [1, 2, 3, 4, 5]
# print(Num_List)  # [1, 2, 3, 4, 5]
# butlast_list = butlast(Num_List)
# print(butlast_list)  # [1, 2, 3, 4]
# print(Num_List)  # [1, 2, 3, 4, 5] (original list remains unchanged)

# =============================================================================
# ! Lambda Function
# Lambda functions are small anonymous functions that can have any number of arguments but can only have one expression.
# =============================================================================

# Duplicate = lambda x: x * 2  # Duplicate is a lambda function that takes one argument x and returns x * 2
# print(Duplicate(5))  # 10
# Add = lambda x, y: x + y  # Add is a lambda function that takes two arguments x and y and returns x + y
# print(Add(5, 10))  # 15

# =============================================================================
# ! Map Function
# Map function applies a given function to all items in an iterable (e.g., list, tuple) and returns a map object (which is an iterator).
# =============================================================================

# Num = [1, 2, 3, 4, 5]
# duplicate = []
# for i in Num:
#     duplicate.append(
#         i * 2
#     )  # duplicate is a list that contains the duplicate of the numbers in the list Num
# print(Num)  # [1, 2, 3, 4, 5]
# print(duplicate)  # [2, 4, 6, 8, 10]

# duplicate_num = list(
#     map(lambda x: x * 2, Num)
# )  # duplicate_num is a list that contains the duplicate of the numbers in the list Num
# print(Num)  # [1, 2, 3, 4, 5] (original list remains unchanged)
# print(duplicate_num)  # [2, 4, 6, 8, 10]

# Names = [("Ali" , "Mahmoud"), ("Ahmed" , "Mohamed"), ("Omar" , "Youssef")]
# update_names = list(
#     map(lambda x: f"{x[1]}, {x[0]}", Names)
# )  # update_names is a list that contains the second element of each tuple in the list list_of_tuples
# print(update_names)  # ['Mahmoud, Ali', 'Mohamed, Ahmed', 'Youssef, Omar']

# ==============================================================================
# ! Filter Function
# Filter function constructs an iterator from elements of an iterable for which a function returns true.
# ==============================================================================
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = []
# for i in numbers:
#     if i % 2 == 0:
#         even_numbers.append(i)
# print(even_numbers)  # [2, 4, 6, 8, 10]
# #===============================================
# even_numbers_filter = list(
#     filter(lambda x: x % 2 == 0, numbers)
# )  # even_numbers_filter is a list that contains the even numbers in the list numbers
# print(numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] (original list remains unchanged)
# print(even_numbers_filter)  # [2, 4, 6, 8, 10] (original list remains unchanged)
# ============================================================================================
# ! Sorted Function
# The sorted() function returns a new sorted list from the elements of any iterable (e.g., list, tuple, dictionary, etc.).
# =============================================================================
# Num = [5, 2, 9, 1, 5, 6]
# sorted_num = sorted(Num)  # sorted_num is a new list that contains the sorted
# sorted_num2= sorted(Num, reverse=True)  # sorted_num is a new list that contains the sorted
# sorted_num3= sorted(Num, key=lambda x: x%2)  # sorted_num is a new list that contains the sorted
# print(Num)  # [5, 2, 9, 1, 5, 6] (original list remains unchanged)
# print(sorted_num)  # [1, 2, 5, 5, 6, 9] (new sorted list)
# print(sorted_num2)  # [9, 6, 5, 5, 2, 1] (new sorted list in reverse order)
# print(sorted_num3)  # [2, 6, 5, 9, 5, 1] (new sorted list by even numbers first then odd numbers)
# #=============================================================================
# Names = ["Ali", "Ahmed", "Omar", "Youssef"]
# sorted_names = tuple(sorted(Names))  # sorted_names is a new tuple that contains the sorted names
# print(Names)  # ['Ali', 'Ahmed', 'Omar', 'Youssef']
# print(sorted_names)  # ('Ahmed', 'Ali', 'Omar', 'Youssef') (new sorted tuple)
# #=============================================================================
# Marks = {"Ali": 90, "Ahmed": 80, "Omar": 70, "Youssef": 60}
# sorted_marks = dict(sorted(Marks.items(), key=lambda x: x[1], reverse=True))  # sorted_marks is a new dictionary that contains the marks sorted in descending order
# print(Marks)  # {'Ali': 90, 'Ahmed': 80, 'Omar': 70, 'Youssef': 60} (original dictionary remains unchanged)
# print(sorted_marks)  # {'Ali': 90, 'Ahmed': 80, 'Omar': 70, 'Youssef': 60} (new sorted dictionary)
# ==============================================================================
# ! All Function
# The all() function returns True if all elements of the iterable are true (or if the
# ==============================================================================
# values = [True, True, 5==5]
# print(all(values)) # True (all elements are true)

# def Check_All_Greter (Num, Goal):
#     for n in Num:
#         if n <= Goal:
#             return False
#     return True
# List = [10, 20, 30, 40, 50]
# # print(Check_All_Greter(List, 5)) # True (all elements are greater than 5)
# def check (nums, goal):
#     return all(map(lambda x: x < goal, nums)) # all() function returns True if all elements of the iterable are true (or if the iterable is empty)
# print(check(List, 5)) # True (all elements are greater than 5)
# =================================================================
# ! JSON
# =================================================================
# import json
# Data = {
#     "President": {
#         "Name": "John Doe",
#         "Age": 55,
#         "Term": 2,
#         "Leave": "New York"
#     }
# }

# with open("data.json", "w") as write_file:
#     json.dump(Data, write_file, indent=4)  # write the data to the file in JSON format with an indentation of 4 spaces

# with open("data.json", "r") as read_file:
#     data = json.load(read_file)  # read the data from the file in JSON format
#     print(data)  # print the data read from the file
#     print(type(data))  # print the type of the data read from the file

# json_val = json.load(open("data.json"))
# print('JSON Value - ', json_val)  # print the data read from the file
# ==================================================================================
# ! Multithreading
# Multithreading is a technique that allows a program to run multiple threads concurrently.
# Multithreading is useful for performing multiple tasks at the same time, such as reading from and writing to a file, or making network requests.
# conqrunce is a technique that allows a program to run multiple threads concurrently.
# in multithresding the core of cpu is shared between threads and each thread has its own stack
# in multithresding the core of cpu is responsible for running one opperation at a time and if this take time transform to onther opperation
# Multithreading is useful for performing multiple tasks at the same time, such as reading from and writing to a file, or making network requests.
# Multithreading is not useful for CPU-bound tasks, such as mathematical calculations, because the core of the CPU is shared between threads and each thread has
# ! using threads when contain io app like reading file or making network request for getharing data from web
# ==================================================================================
# import time as t

# !
# def Sleep():
#     """
#     This function is used to sleep for 1 second.
#     This function is used to simulate a task that takes time to complete.
#     And show the difference of time taken by  normal and multithreading
#     Workflow is :
#     1. Start the timer
#     2. Call the Sleep function
#     3. sleep for one second
#     4. Print "Sleeping"
#     5. End the timer
#     6. Print the time taken
#     param None:
#     return: None
#     """
#     t.sleep(1)  # sleep is a function in the time module that pauses the execution of the program for a specified number of seconds.
#     print("Sleeping")


#     t.sleep(
#         1
#     )  # sleep is a function in the time module that pauses the execution of the program for a specified number of seconds.
#     print("Sleeping")


# strat = t.perf_counter()  # perf_counter is a function in the time module that returns the current time in seconds
# Sleep()  # call fun Sleep this deffrent of sleep
# Sleep()
# end = t.perf_counter()
# print(
#     "Time taken of fun Sleep is : ", end - strat
# )  # Time taken:  2.000000000000001 (time taken to execute the Sleep function)


# import time as t
# from threading import Thread, Lock, current_thread

# !
# def Sleep(seconds=0):
#     """
#     This function is used to sleep for a specified number of seconds.
#     This function is used to simulate a task that takes time to complete.
#     And show the difference of time taken by  normal and multithreading
#     This used Multithreading to run two threads at the same time.
#     Workflow is:
#     1. Start the timer
#     2. Call the Sleep function
#     3. sleep for specified number of seconds
#     4. Print "Sleeping"
#     5. End the timer
#     6. Print the time taken
#     param seconds: int
#     return: None
#     """

#     t.sleep(seconds)
#     print(" sleeping for ", seconds, " seconds by ", current_thread().name)


# start = t.perf_counter()

# thread1 = Thread(
#     target=Sleep, kwargs={"seconds": 2}, name = "T1"
# )  # target is a parameter in the threading module that specifies the function to be executed by the thread. args is a parameter in the threading module that specifies the arguments to be passed to the function. name is a parameter in the threading module that specifies the name of the thread.
# thread2 = Thread(
#     target=Sleep, kwargs={"seconds": 2}, name = "T2"
# )  # asising thread manual *args is posthional argumetns must be included in tuple since kwargs must be in dictionary {"seconds:2"}

# thread1.start()  # start is a method in the threading module that starts a thread.
# thread2.start()

# thread1.join()  # join is a method in the threading module that waits for a thread to complete before continuing with the rest of the program.
# thread2.join()

# end = t.perf_counter()

# print("Time taken of fun Sleep with multithreading is : ", end - start)
# # Time taken:  1.000000000000001 (time taken to execute the Sleep function with multithreading)

# !
# import time as t
# from threading import Thread, Lock, current_thread


# counter = 0
# lock = Lock()


# def Sleep(lock):

#     global counter
#     with lock:
#         # lock.acquire()
#         local_counter = counter
#         local_counter += 1
#         t.sleep(0.5)
#         counter = local_counter
#         # lock.release()


# start = t.perf_counter()
# threads = []
# for _ in range(2):
#     thread = Thread(target=Sleep, args=(lock,))
#     threads.append(thread)

# for thread in threads:
#     thread.start()

# for thread in threads:
#     thread.join()

# end = t.perf_counter()

# print("Time taken of fun Sleep with multithreading is : ", end - start)
# print(f"The num of counter is : {counter}")
# # Time taken:  1.000000000000001 (time taken to execute the Sleep function with multithreading)
# # The num of counter is : 2

# !
# from concurrent.futures import ThreadPoolExecutor
# import time as t


# def Sleep(seconds=0):
#     t.sleep(seconds)
#     return f"Done sleeping for {seconds} seconds"


# start = t.perf_counter()
# thread = []
# with ThreadPoolExecutor() as exe:
#     f1 = exe.submit(Sleep, 1)
#     f2 = exe.submit(Sleep, 1)
#     print(
#         f2.result()
#     )  # this will print the result of the function f2 which is the result of the function Sleep(1) which is "Done sleeping for 1 seconds"
#     print(f1.result())
# end = t.perf_counter()

# print("Time taken of fun Sleep with multithreading is : ", end - start)

# from concurrent.futures import ThreadPoolExecutor, as_completed
# import time as t


# def Sleep(seconds=0):
#     t.sleep(seconds)
#     return f"Done sleeping for {seconds} seconds"


# !

# start = t.perf_counter()
# thread = []
# with ThreadPoolExecutor() as exe:
#     seconds = [5, 6, 1, 2]
#     futures = [exe.submit(Sleep, seconds) for seconds in seconds]
#     for future in as_completed(
#         futures
#     ):  # as_completed return the first element is done first so on
#         print(future.result())

#  Done sleeping for 2 seconds
#  Done sleeping for 5 seconds
#  Done sleeping for 6 seconds

# start = t.perf_counter()
# thread = []
# with ThreadPoolExecutor() as exe:
#     seconds = [5, 6, 1, 2]
#     futures = exe.map(Sleep, seconds)
#     for future in futures:  # the deffrence between map and as_completed is that map return the result in the order of the input since as_completed return the first element is done first so on
#         print(future)


# !

# thread = []
# with ThreadPoolExecutor() as exe:
# with ThreadPoolExecutor() as exe:
#     futures = [exe.submit(Sleep, 1)for _ in range(10)]
#     for future in as_completed(futures):
#         print(future.result())

# end = t.perf_counter()

# print("Time taken of fun Sleep with multithreading is : ", end - start)

# ! crypto_doenloader.py

# import requests
# import json
# import pandas as pd
# import time as t
# import os
# from concurrent.futures import ThreadPoolExecutor

# symbols = [
#     "BTCUSDT",
#     "ETHUSDT",
#     "BNBUSDT",
#     "ADAUSDT",
#     "XRPUSDT",
#     "DOTUSDT",
#     "LINKUSDT",
#     "UNIUSDT",
#     "LTCUSDT",
#     "XLMUSDT",
# ]
# start = t.perf_counter()


# # for symbol in symbols :
# def doenload_crypto_data(symbol):

#     BASE_URL = "https://api.binance.com"
#     ENDPOINT = "/api/v3/klines"
#     url = BASE_URL + ENDPOINT
#     os.makedirs("crypto", exist_ok=True)

#     params = {"symbol": symbol, "interval": "1d", "limit": 1000}
#     response = requests.get(url, params=params)
#     data = json.loads(response.content)
#     df = pd.DataFrame(data)
#     df.to_csv(f"crypto/{symbol}.csv")
#     return f"Download data for {symbol}"
#     # print(f"Download data for {symbol}")


# with ThreadPoolExecutor() as exe:
#     futures = exe.map(doenload_crypto_data, symbols)
#     for future in futures:
#         print(future)

# end = t.perf_counter()
# print(f"Time taken for {round(end - start, 2)}")

# ============================================================
# ! Multiprocessing
# ============================================================
# import os
# import time as t
# from multiprocessing import Process, cpu_count


# def some_process():
#     print(os.getpid())
#     for _ in range(200000000):
#         pass


# # start = t.perf_counter()
# # some_process()
# # end = t.perf_counter()
# # print(f"some_process time  : {round(end - start,2)}")


# if __name__ == "__main__":
#     start = t.perf_counter()
#     procs = [Process(target=some_process) for f in range(cpu_count())]
#     for p in procs:
#         p.start()
#     for p in procs:
#         p.join()
#     end = t.perf_counter()
#     print(f"multiprocessing time : {round(end - start, 2)}")
#     print(f"cpu_count : {cpu_count()}")
#     print(f"number of process : {len(procs)}")

# !
# import time as t
# from multiprocessing import Process, cpu_count, current_process


# def Sleep(seconds):
#     t.sleep(seconds)
#     print(f"{current_process().name} Done sleeping for {seconds} seconds")


# if __name__ == "__main__":  # this is the entry point of the program
#     start = t.perf_counter()

#     p0 = Process(
#         target=Sleep, args=(1,), name="p0"
#     )  # if used seconds=0 this must be used kwargs {"seconds":2}
#     p1 = Process(target=Sleep, args=(2,), name="p1")

#     p0.start()
#     p1.start()
#     p0.join()
#     p1.join()

#     end = t.perf_counter()
#     print(f"Time taken : {round(end - start, 2)}")
#     print(f"cpu_count : {cpu_count()}")

# !
# import time as t
# from multiprocessing import Process, cpu_count, current_process


# def Sleep(seconds=0):
#     t.sleep(seconds)
#     print(f"{current_process().name} Done sleeping for {seconds} seconds")


# if __name__ == "__main__":  # this is the entry point of the program
#     start = t.perf_counter()

#     processes = []
#     # processes = [Process(target=Sleep,args=(1,))for _ in range(10)]
#     # for p in processes:
#     #     processes.append(p)
#     #     p.start()
#     # for p in processes:
#     #     p.join()

#     for i in range(10):
#         p = Process(target=Sleep, kwargs={"seconds": 2}, name=f"p{i}")
#         processes.append(p)
#         p.start()
#     for p in processes:
#         p.join()

#     end = t.perf_counter()
#     print(f"Time taken : {round(end - start, 2)}")
#     print(f"cpu_count : {cpu_count()}")

# !
# import time as t
# from multiprocessing import Process, cpu_count, current_process, Value, Lock


# def Add(num, lock):
#     with lock:
#         num.value += 100


# if __name__ == "__main__":
#     start = t.perf_counter()

#     processes = []
#     num = Value("i", 0)
#     lock = Lock()

#     for _ in range(100):
#         p = Process(target=Add, args=(num, lock))
#         processes.append(p)
#         p.start()

#     for p in processes:
#         p.join()

#     end = t.perf_counter()

#     print(f"Time taken : {round(end - start, 2)}")
#     print(f"cpu_count : {cpu_count()}")
#     print(f"num : {num.value}")

# from concurrent.futures import  ProcessPoolExecutor , as_completed
# from multiprocessing import current_process
# import time as t

# def Sleep(seconds=0):
#     t.sleep(seconds)
#     return (f"{current_process().name} Done sleeping for {seconds} seconds")

# if __name__ == "__main__":  # this is the entry point of the program

#     start = t.perf_counter()

#     with ProcessPoolExecutor() as exe:
#         futures = [exe.submit(Sleep,seconds= 2) for _ in range(10)] # this is way to craete loop name is  list comprehension
#         for future in as_completed(futures):
#             print(future.result())

#     end = t.perf_counter()
#     print(f"Time taken : {round(end - start, 2)}")


# ! Asyncio
# Asyncio is a library for writing single-threaded concurrent code using coroutines,
# multiplexing I/O access over sockets and other resources, running network clients and servers, and other related primitives.
# Blocking is a process where a thread or process is waiting for an event to occur before it can continue execution.(sync)
# Non-blocking is a process where a thread or process
# can continue execution without waiting for an event to occur.(async) Co-rotine (start, end, pause, resu)
# --------------------------------------------------------------------------------------------------

# ! sync (blocking)

# import time as t


# def waiter(customer_request, duration):
#     print(f"start {customer_request} request...")
#     t.sleep(duration)
#     print(f"Finshed for {customer_request} request")


# start = t.perf_counter()


# def main():

#     waiter("coffee", 3)
#     waiter("tea", 2)
#     waiter("water", 1)


# if __name__ == "__main__":
#     main()
#     end = t.perf_counter()
#     print(f"Time Taken for finshed request  for all is {round(end - start, 2)}")

# ! ex for multithreading

# import time as t
# from concurrent.futures import ThreadPoolExecutor, as_completed


# def waiter(customer_request, duration):
#     print(f"start {customer_request} request...")
#     t.sleep(duration)
#     print(f"Finshed for {customer_request} request")


# def main():
#     with ThreadPoolExecutor(max_workers=3) as executor:
#         future_to_request = {
#             executor.submit(waiter, "coffee", 3): "coffee",
#             executor.submit(waiter, "tea", 2): "tea",
#             executor.submit(waiter, "water", 1): "water",
#         }

#         for future in as_completed(future_to_request):
#             request = future_to_request[future]
#             try:
#                 data = future.result()
#             except Exception as exc:
#                 print(f"{request} generated an exception: {exc}")
#             else:
#                 print(f"{request} has been processed")


# if __name__ == "__main__":
#     start = t.time()
#     main()
#     end = t.time()
#     print(f"Total time taken: {round(end - start, 2)} seconds")


# ! asyncio version of the above code

# import asyncio
# import time


# async def waiter(item, delay):
#     print(f"start {item} request...")
#     await asyncio.sleep(delay)
#     return f"Finshed for {item} request"


# async def main():
#     tasks = [
#         waiter("coffee", 3),
#         waiter("tea", 2),
#         waiter("water", 1),
#     ]
#     results = await asyncio.gather(*tasks)
#     for result in results:
#         print(result)


# if __name__ == "__main__":
#     start = time.time()
#     asyncio.run(main())
#     end = time.time()
#     print(f"Total time taken: {round(end - start, 2)} seconds")

# ! SOLID Princpiles

# ! Single Responsibility Principle (SRP)
# A class should have only one reason to change, meaning it should have only one job.
# ! Open/Closed Principle (OCP)
# Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.
# ! Liskov Substitution Principle (LSP)
# Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program.
# ! Interface Segregation Principle (ISP)
# No client should be forced to depend on methods it does not use.
# ! Dependency Inversion Principle (DIP)
# High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.

# from abc import ABCMeta, abstractmethod, ABC


# class Order(metaclass=ABCMeta):
#     items = []
#     quantitues = []
#     prices = []
#     status = "oppen"

#     def AddItems(self, name, quantity, price):
#         self.items.append(name)
#         self.quantitues.append(quantity)
#         self.prices.append(price)

#     def TotalPrice(self):
#         total = 0
#         for i in range(len(self.prices)):
#             total += self.prices[i] * self.quantitues[i]
#         return f"Total Price: {total}"


# class Authorizer(ABC):
#     @abstractmethod
#     def IsAuthorized(self) -> bool:
#         pass


# class SMSAuth(Authorizer):
#     authorized = False

#     def VerifyCode(self, code):
#         print(f"Verifying Code {code}")
#         self.authorized = True

#     def IsAuthorized(self) -> bool:
#         return self.authorized


# class NotARobot(Authorizer):
#     authorized = False

#     def IsHuman(self):
#         print("Are you a robot? Naaa...")
#         self.authorized = True

#     def IsAuthorized(self) -> bool:
#         return self.authorized


# class PaymentProcessor(ABC):
#     @abstractmethod
#     def Pay(self, Order):
#         pass


# class CreditPaymentProcessor(PaymentProcessor):
#     def __init__(self, SecurityCode):
#         self.SecurityCode = SecurityCode
#         self.verified = False

#     def Pay(self, Order):
#         print("Processing Credit Payment...")
#         print(f"Verifying Security Code: {self.SecurityCode}")
#         Order.status = "paid"


# class DebitPaymentProcessor(PaymentProcessor):
#     def __init__(self, SecurityCode, authorizer: Authorizer):
#         self.authorizer = authorizer
#         self.SecurityCode = SecurityCode

#     def Pay(self, Order):
#         if not self.authorizer.IsAuthorized():
#             raise Exception("Debit card payment requires SMS verification.")
#         print("Processing Debit Payment...")
#         print(f"Verifying Security Code: {self.SecurityCode}")
#         Order.status = "paid"


# class PaypalPaymentProcessor(PaymentProcessor):
#     def __init__(self, EmailAddress, authorizer: Authorizer):
#         self.authorizer = authorizer
#         self.EmailAddress = EmailAddress

#     def Pay(self, Order):
#         if not self.authorizer.IsAuthorized():
#             raise Exception("PayPal payment requires SMS verification.")
#         print("Processing PayPal Payment...")
#         print(f"Verifying Email Address: {self.EmailAddress}")
#         Order.status = "paid"


# OrederOne = Order()
# OrederOne.AddItems("Keyboard", 1, 450)
# OrederOne.AddItems("Mouse", 2, 350)
# OrederOne.AddItems("Monitor", 1, 2500)

# print(OrederOne.TotalPrice())

# authorizer = SMSAuth()
# processes = DebitPaymentProcessor("07378565", authorizer)
# authorizer.VerifyCode("07378565")
# processes.Pay(OrederOne)


#----------------------------------------------------------
# ! Git And GitHub
# ----------------------------------------------------------
# Git is a version control system that helps developers track changes to their code and collaborate with others.
# It allows developers to create branches of code, make changes, and merge those changes back into the main codebase.
# Git also provides a way to (revert changes) if necessary (and to keep a history of all changes made to the code). Git
# You can use Git Without Github
#---------------------------------------------------------------------------------------------------------------------------
# Github Simplified using Git
# Github is a web-based platform that provides hosting for Git repositories.
# It allows developers to store their code on the web and collaborate with others on the same codebase.
# Github also provides a range of tools and features to help developers manage their code, such as issue tracking, pull requests, and code reviews.
# Github is a popular platform for open-source projects and is used by many developers to host their personal and professional projects.
#---------------------------------------------------------------------------------------------------------------------------
# ! Word You Will Hear 
# - Repositori: A collection of files and folders that are tracked by Git.
# - Branch: A separate line of development within a Git repository.
# - Local Repository: A copy of a repository on a developer's local machine such as laptop or PC.
# - Remote Repository: A copy of a repository on a remote server, such as Github.
# - Commit: A snapshot of the changes made to a repository at a specific point in time.(Snapshot Or Checkpoint In Your Locl Repo)
# - Clone: A copy of a repository that is created on a developer's local machine Or Remote Server.
# - Push: The process of transferring changes from a local repository to a remote repository.
# - Pull: The process of transferring changes from a remote repository to a local repository.
# - Pull Request: A request made by a developer to merge changes from one branch into another branch.[Tell Ohter About Your Changes To Pull It From Local to Remote]
#-------------------------------------------------------------------------------------------------------------------------------
# ! Important Nots 
# - Create Repo For Every Projrct You Work On.
# - Use Branches For Different Features Or Fixes Or Enhancements.
# - No Need To Connect To Remote When Working On Local Only and Push When You Want To Share Your Changes.
# - Always Pull Before Pushing To Avoid Conflicts.
# - Always Keep Your Local Repo Up To Date With The Remote Repo.
# - Abn One Can Push Or Pull Depending On The Permissions Set By The Repository Owner.
#---------------------------------------------------------------------------------------------------------------------------------
# ! Craete Repo GitHub And Clone It Locally
# Commend Line 
# D:
# mkdir MyGitHub
# cd mkdir MyGitHub\
# cd D:MyGitHub\
# D: MyGitHub
# git clone https://github.com/username/repository.git
# cd git_course\
#-------------------------------------------
# ! Add And Reset And Commit And Explain Progress

# - git status : Shows The Status Of The Working Directory And Staging Area.
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#         Css/
# - git reset head <file> : Removes The File From The Staging Area But Leaves It In The Working Directory.
# - git restore --staged <file> : Removes The File From The Staging Area But Leaves It In The Working Directory.
# - git commit -m "Create The Main project structure" : Commits The Changes With A Message.
# - git push RemteName BranchName: Pushes The Changes To The Remote Repository.
# - git remote -v : Shows The Remote Repository URL.

# ! Pull New Changes From Remote Repository
# - git pull RemoteName BranchName : Pulls The Changes From The Remote Repository.

# ! Every Thing About Git Configuration
# - git config --list : Lists All The Git Configuration.
# - git help config : Shows The Git Config Help.
# - git config --global user.name "Mahmoud Elsayed" : Configures The Global User Name.
# - git config --global user.email "mahmoud.elsayed@example.com" : Configures The Global User Email.
# - git config --global user.name : Shows The Global User Name.
# - git config --global user.email : Shows The Global User Email.
# - git config --global --edit : Edits The Global Git Configuration File.
# ! Create And Test Public Key
# - ssh-keygen -t rsa -b 4096 -C "your_email@example.com" : Generates A New Public SSH Key
# - ssh-add ~/.ssh/id_rsa : Adds The SSH Key To The SSH Agent
# - cat ~/.ssh/id_rsa.pup : Shows The Public Key Content
# - ssh -T git@github.com : Tests The SSH Connection To GitHub
# ! Repo From Existing Project
# - git init : Initializes A New Git Repository.