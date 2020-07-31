#   ================User Friends========================
def user_friends():
#   <<<<<<<<<<<<< Define local variables <<<<<<<<<<<<
    num = int(input("How many friends do you want to input?:\n"))
    friends = None
    sep = ""
    friend = ""
    i = 1
#   <<<<<<<<<<<< Conditional loop <<<<<<<<<
    while i <= num:
#   <<<<<<<<<<<< Conditional separators <<<<<<<<<
        if i == num:
            sep = "."
        else:
            sep = ", "
        friend = input("Friend name:")
        friends += friend + sep
        i += 1
    print("User friends:", friends)

user_friends()
