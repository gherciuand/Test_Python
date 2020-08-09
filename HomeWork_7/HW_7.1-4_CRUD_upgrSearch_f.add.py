basm = ["Harap Alb", "Fat Frumos", "Danila Prepeleac", "Pinochio", "Mica Sirena"]
tara_provenenta = ["Romania", "Romania", "Romania", "Italia", "Danemarca"]
popularitate = [8.53, 8.11, 7.69, 8.47, 7.3]


def search():
    count = 0
    while count <= 3:
        try:
            nume = input("introduceti basmul: ").title()
            for i in range(len(basm)):
                if nume not in basm:
                    print(f'Basmul {nume} nu a fost gasit')
                    break
                else:
                    return basm.index(nume)
        finally:
            count += 1
            if count == 3:
                print("Consultati lista basmelor (1 din meniu)")
                return None


def read():
    for i in range(len(basm)):
        print(f" < {basm[i]} ")


def details():
    i = search()
    if i is not None:
        print(f" < {basm[i]:20s} Tara - {tara_provenenta[i]:10s} Rating - {popularitate[i]:3.1f}")
    else:
        pass


def edit():
    i = search()
    if i is not None:
        print(f"Editarea basmului {basm[i]}")
        edit_basm = input("Introduceti numele nou al basmului: - ").title()
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
    else:
        pass

#-------Functia add() adauga elemente insa mai necesita imbunatatire
#               (verificare daca toate elementele au fost introduse corect)
def add():
    print("!" * 10, "TOATE CAMPURILE SUNT OBLIGATORII", "!" * 10)
    new_basm = input("Nume basm: <").title()
    new_tara = input("Tara de provenienta: <").title()
    new_rating = float(input("Popularitatea basmului: <"))
    basm.append(new_basm)
    tara_provenenta.append(new_tara)
    popularitate.append(new_rating)


def delete():
    i = search()
    if i is not None:
        print(f"Basmul {basm[i]} a fost sters")
        basm.pop(i)
        tara_provenenta.pop(i)
        popularitate.pop(i)
    else:
        pass


def menu():
    option = None
    while option != 0:
        print("\n")
        print("=" * 20, "MENU", "=" * 20)
        print("1 - Arata lista basmelor:")
        print("2 - Arata detaliile basmului:")
        print("3 - Editare detalii basm:")
        print("4 - Sterge basmul:")
        print("5 - Adauga un basm nou")
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
            delete()
        elif option == 5:
            add()
        elif option == 0:
            break
        else:
            print("\nSelectati doar valorile propuse:")


menu()
