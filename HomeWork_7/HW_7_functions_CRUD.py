basm = ["Harap Alb", "Fat Frumos", "Danila Prepeleac", "Pinochio", "Mica Sirena"]
tara_provenenta = ["Romania", "Romania", "Romania", "Italia", "Danemarca"]
popularitate = [8.53, 8.11, 7.69, 8.47, 7.3]


def read():
    for i in range(len(basm)):
        print(f" < {basm[i]} ")


def details():
    nume = input("Introduceti numele basmului: \n>").title()
    for i in range(len(basm)):
        if nume not in basm:
            print("Basmul", nume, "nu a fost gasit in lista")
            break
        if basm[i] == nume:
            print(f" < {basm[i]:20s} Tara - {tara_provenenta[i]:10s} Rating - {popularitate[i]:3.1f}")


def edit():
    nume = input("Introduceti numele basmului ce urmeaza a fi editat? \n>").title()
    for i in range(len(basm)):
        if basm[i] == nume:
            print(f"Editarea basmului {basm[i]}")
            edit_basm = input("Introduceti numele basmului: - ").title()
            if edit_basm == "":
                pass
            else:
                basm[i] = edit_basm
            edit_tara = input("Introduceti tara basmului: - ").title()
            if edit_tara == "":
                pass
            else:
                tara_provenenta[i] = edit_tara
            new_rating = input("Introduceti popularitatea basmului: - ")
            if new_rating == "":
                pass
            else:
                popularitate[i] = float(new_rating)


def delit():
    nume = input("Introduceti numele basmului? \n>").title()
    for i in range(len(basm)):
        if nume not in basm:
            print("Basmul", nume, "nu a fost gasit in lista")
            break
        if basm[i] == nume:
            print(f"Basmul {basm[i]} a fost sters")
            basm.pop(i)
            tara_provenenta.pop(i)
            popularitate.pop(i)
            break


def menu():
    option = None
    while option != 0:
        print("\n")
        print("=" * 20, "MENU", "=" * 20)
        print("1 - Arata lista basmelor:")
        print("2 - Arata detaliile basmului:")
        print("3 - Editare detalii basm:")
        print("4 - Sterge basmul:")
        print("0 - Iesire:")
        print("-" * 47)
        print("Alege optiunea")
        option = int(input())
        if option == 1:
            read()
        elif option == 2:
            details()
        elif option == 3:
            edit()
        elif option == 4:
            delit()
        else:
            print("\nSelectati valorile propuse:")


menu()
