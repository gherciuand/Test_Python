# <<<<<<<<<<Define data
year_of_birth = int(input("insert year of birth "))
current_year = 2020
age = current_year - year_of_birth #define the variable "age"
# <<<<<<<<<<Logical layer
if year_of_birth < 1900 or year_of_birth > current_year:
    print("The year of birth is not valid")
else:
# <<<<<<<<<<Output Data
    if age < 4:
        print("[0-3 years] - it is a baby, he has ", age, " age")
    elif age < 10:
        print("[4-9 years] - it is a kid, he has ", age, " age")
    elif age < 16:
        print("[10-15 years] - it is a teen, he has ", age, " age")
    elif age < 19:
        print("[16-18 years] - it is a young, he has ", age, " age")
    elif age < 51:
        print("[19-50 years] - it is an adult, he has ", age, " age")
    else:
        print("[51+ years] - it is an old, he has ", age, " age")
