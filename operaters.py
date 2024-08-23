print("2**3")


#eval():
eval("2**3")
eval("3**2-4*1*2")



text = "4*6-3"
result = eval(text)
print(result)
print("original string is:"+ text) 



#operaters
#arithematic operators
#addition  (+)
#subraction  (-)
#multiplication  (*)
#division  (/) always gives float
#modulus  (%)  returns the remainder of the division
#exponent  (**) 
#floor division //  returns integer part of the quotient


a = 100
b = 45
print(a+b)

a = 24
b = 9
print(a-b)


a = 28
b = 22
print(a*b)


a = 18
b = 9
print(a/b)


a = 14
b = 5
print(a%b)


a = 100
b = 0
print(a**b)

a = 100
b = 10
print(a//b)




#comprision operators  (true/false)c
#double equal to ==
name1 = "jyothika"
name2 = "jyothika"
print(name1 == name2)



#not equal to !=
numa = 24
numb = 22
print(numa != numb)


'''logical opertors used to join two or more conditions 
TRUTH TABLE
     AND  OR  XOR
0 0   0    0   0
0 1   0    1   1
1 0   0    1   1
1 1   1    1   0
 AND:returns true if both operands are true
 OR:returns true if anyone operands is true'''



#bitwise operators
#bitwise AND
a,b = 20,12
print(a&b)


#bitwise OR
a,b = 100,120
print(a|b)


#bitwise NOT x = -x-1
a = 12
print(~a)


#bitwise XOR
j,k = 9,24
print(j^k)


#bitwise left shift <<  (a<<b = a*2**b)
a = 100
print(a<<3)


#bitwise right shift >>   (a>>b = a/2**b)
b = 20
print(b>>6)


#membership operators : (in,not in)
m = "jyothika swamy"
print("swamy" in m)


num = 1,1,2,3,4,5
print(10 in num)


name= "jasmine,rose,lilly"
print("sunflowe" not in name)


#identity opertors:(is,is not)
t1 = 1,2,3,4,5
t2 = 1,2,3,4,5
print("wht is thhi type", type(t1))
print(t1 is t2)
print(id(t1))
print(id(t2))




name1 = "romeo"
name2 = "romeo"
print(name1 is name2)


num1 = 1.0
num2 = 1.0
print(num1 is not num2)
print(id(num1))




