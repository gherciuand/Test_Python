#<<<<<<<<<<<<<<<<<<< First 5 from range divided by 3 <<<<<<<<<<<<<<<<<<<<<<

#-----------Define the functions

def InputInt(text):
    num_int=input(text)
    return int(num_int)

def print_line (text):
    print("\n")
    print("_"*100)
    print("*"*10, text, "*"*10)
    print("_"*100, "\n")

#----------Define the global variables
start_value = InputInt("Start value:")
end_value = InputInt("End value:?")
print_line("Diapazon of values")
count = 0

#--------- Conditions for directions
if start_value < end_value:
    step = 1
else: step = -1

#----------Show the data
for n in range(start_value, end_value, step):
    print(n, end=" ",)
print_line("Divide by 3")
for n in range(start_value, end_value, step):
    if n % 3 == 0:
        print(n, end=" ",)
print_line("First 5 values divide by 3 ")
for n in range(start_value, end_value, step):
    if n % 3 == 0 and count < 5:
        count += 1
        print(n, end=" ",)
