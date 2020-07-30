            #<<<<<<<<<< TEXT_BRACKETS <<<<<<<<<<<<

def Brackets (text):
    return "("+text+")"
def SqBrackets (text,num):
    return "["*num + text + "]"*num
def LesGreatBrackets (text,num):
    return "<"*num +text + ">"*num

print(LesGreatBrackets(SqBrackets(Brackets(input("Input some text:")),int(input("Number of '[' brackets:"))), int(input("Number of '<' brackets:"))))

#Var_2 Number of brackets --->global var

#num = int(input("Number of Brackets"))
#print(LesGreatBrackets(SqBrackets(Brackets(input("Input some text:")),num), num))


