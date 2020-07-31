#==================Drow the square================
def DrowSquare(size):
    n=0
    while n < size:
        print("* "*size)
        n += 1

#===================Convert input value to integer=============

def InputInt(value):
    while True:
        try:
            num_int = input(value)
            return int(num_int)
        except ValueError:
            print("Ooops, wrong value. Please enter only integer number:")

DrowSquare(InputInt("Size of square is:\n"))