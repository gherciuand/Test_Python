#### Sum input number ###

            #### Initial data
num = 0
sum = 0
count = 0
print("Introduceti cate un numar intreg:")

            #### Logical calc
while num >= 0:
    num = float(input("Numar:"))
    if  (num-int(num)!=0):
        print("Numarul",num, "nu este intreg si nu va fi luat in conisderatie") #<<<<<<<<<<< Not integer
        continue
    if num >=0:
        sum += num
        count += 1
    else:
        #<<<<<<<<<<<<<<<<<<<< OUTPUT RESULTS
        print("*"*40)
        print("Ati introdus", count, "numere intregi pozitive")
        print("Suma numerilor introduse este :", int(sum))
        print("Media aritmetica a numerilor introduse este:", round(sum/count, 2))
        print("*" * 40)
