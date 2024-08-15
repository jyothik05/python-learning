#everything in Python is an object
'''-->DATA TYPES (6):   {10}
     * TEXT TYPE --->(str)
     * NUMERIC TYPE--->(int,float,complex)
     * SEQUENCE TYPE--->(list,tuple,range)
     * MAPPING TYPE--->(dict)
     * SET TYPE--->(sets)
     * BOOLEAN TYPE--->(true,false)
      '''
#INTEGER
x = 1
print(type(x))


#FLOAT
y = 100.56
print(type(y))

#STRING
z = "justin"
print(type(z))

#COMPLEX
k = 1+2j
print(type(k))


#TYPE CONVERSION
#int----float    float----int
x = 10.56
print(int(x))
print(float(x))


# IMPLICT CONVERSION (autometically converts one data type to another data type)
y = 10
x = 35.0
print(x+y)
type(x+y)


#EXPLICIT CONVERSION
num = 165
num2 = 175.75
result = int(num2)
print(num+result)


#exmple
num6 = "123"
num = 1234
result = int(num6)
print(num+result)
print(type(result))
print(type(num+result))


#STRING (indexing)
name = "programming"
print(name[3])
print(name[4])
print(name[5])
print(name[6])


#LIST is  mutable and enclosed between square brackets 
#it can hold different type of data 
#it can store duplicate values
list1 = [10.23,12,"bird",100]
print(list1)


#TUPLE is immutable and enclosed between paranthesis
#it can hold different type of data 
#it can store duplicate values
t = (1,2,2,3,4,4,44)
print(t)


#DICTIONARY
'''enclosed with curly braces {} 
   set of value and key pair
    key and value is known as item 
    key is immutable and value is mutable
    doesnot support indexing'''
name = {'no':123,'nae':"john",'age':23}
print(name['no'])
print(name['nae'])
print(name['age'])


#SETS
'''mutable
   doest not support indexing
   useful to remove duplicate values from list and tuple
   '''

names = {"Nina", "Max", "Nina"}
print(names)
print(len(names))


#inorder
my_set = {1, "a", 2, "b", "cat"}
print(my_set)




my_set = {"a", "b", "cat", "dog", "red"}
print(my_set)
print(sorted(my_set))



#adding and removing
colors = {"Red", "Green", "pink"}
colors.add("Orange")
print(colors)


colors = {"Red", "Green", "pink"}
colors.discard("Green")
print(colors)


colors = {"Red", "Green", "pink"}
numbers = {1,2,3}
colors.update(numbers)
print(colors)


#UNION
rainbow_colors = {"Red", "Orange", "Yellow", "Green", "Blue", "Violet"}
favorite_colors = {"Blue", "Pink", "Black"}
print(rainbow_colors | favorite_colors)
#INTERSECTION
print(rainbow_colors & favorite_colors)
#EXCLUDING COMMON
print(rainbow_colors ^ favorite_colors)


