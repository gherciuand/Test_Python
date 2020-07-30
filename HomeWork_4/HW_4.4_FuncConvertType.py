                #<<<<<<CONVERT INPUT <<<<<<<<<<<<<

def InputInt(text):
    num_int=input(text)
    return int(num_int)             #Convert input value to integer
def InputFloa(text):
    num_float=input(text)
    return float(num_float)         #Convert input value to float
def InputBoolean(text):
    num_bool = int(input(text))     #Convert input value to integer
    return bool(num_bool)           #All value !=0 == True

n = InputInt("Enter first number:")
p = InputFloa("Enter the second number:")

print("The sum of", n, "&", p, "equal to", (n+p))
