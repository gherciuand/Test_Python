            #<<<<<<<<<< Horizontal_Vertical_LINES <<<<<<<<<<<<
def DrawLine(length, direction):

        if direction == "h":
            print("_ "*length, end="")
        elif direction == "v":
            i = 0
            while i < length:
                print("|")
                i += 1
        else:
            print("Oops, wrong direction")

DrawLine(int(input("Number of lines:")), input("Direction:\n v - vertical\n h - horizontal\n"))
