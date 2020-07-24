#_______________Part I - type of variables

integer_value = 100
float_value = 0.100
boolean_value = True
string_value = "100_B"
print(integer_value, "is ", type(integer_value))
print(float_value, "is ",type(float_value))
print(boolean_value,"is ", type(boolean_value))
print(string_value, "is ", type(string_value))
print()
print("*"*20)

#_______________Part II - change type from str (input) to integer for arithmetic mean

a = input("insert 1st integer number:  ")
b = input("insert 2nd integer number:  ")
c = input("insert 3rd integer number:  ")
result = (int(a)+int(b)+int(c))/3
print("The integer arithmetic mean between ",a, ", ",b, " and", c, "is equal to ", int(result))
print()
print("*"*20)

#_______________Patr III Auto transferm type of variable from integer to float
x=10
print(x,type(x))
x+=0.1
print(x,type(x))
