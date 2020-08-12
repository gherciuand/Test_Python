basme = [
    {"nume_basm": "Harap Alb", "tara_prov": "Romania", "rating": 8.53},
    {"nume_basm": "Fat Frumos", "tara_prov": "Romania", "rating": 8.11},
    {"nume_basm": "Danila Prepeleac", "tara_prov": "Romania", "rating": 7.69},
    {"nume_basm": "Pinochio", "tara_prov": "Italia", "rating": 8.47},
    {"nume_basm": "Mica Sirena", "tara_prov": "Danemarca", "rating": 7.30}
]
# am definit o functie ce pune toate denumirile la basme in lista
# pentru o mai simpla cautare dupa nume

def lista_basme():
    list_basm = []
    for b in basme:
        list_basm.append(b['nume_basm'])
    return list_basm


def search():
    count = 0
    while count <= 3:
        try:
            nume = input("Introduceti numele basmului:").title()
            for b in basme:
                if nume not in lista_basme():
                    print(f'Basmul {nume}  nu a fost gasit')
                    break
                else:
                    return lista_basme().index(nume)
        finally:
            count += 1
            if count == 3:
                print("Consultati lista basmelor (1 din meniu)")
                return None


def read():
    for b in range(len(basme)):
        print(basme[b]['nume_basm'])

# =======inca o metoda a functiei read()

# def read():
#    lista_basme()
#    for i in range(len(lista_basme())):
#        print(f'<< {lista_basme()[i]}')

def details():
    i = search()
    if i is not None:
        print(f'Detalii:\n'
              f'\t ==={basme[i]["nume_basm"]}=== \n'
              f'>> Tara de provenienta: \t{basme[i]["tara_prov"]}\n'
              f'>> Popularitatea: \t\t\t{basme[i]["rating"]}')


def edit():
    i = search()
    if i is not None:
        print(f"Editarea basmului {basme[i]['nume_basm']}")
        edit_basm = input("Introduceti numele nou al basmului: - ").title()
        if edit_basm == "":
            pass
        else:
            basme[i]['nume_basm'] = edit_basm
        edit_tara = input("Introduceti tara basmului: - ").title()
        if edit_tara == "":
            pass
        else:
            basme[i]['tara_prov'] = edit_tara
        new_rating = input("Introduceti popularitatea basmului: - ")
        if new_rating == "":
            pass
        else:
            basme[i]['rating'] = float(new_rating)


def delete():
    i = search()
    if i is not None:
        basme.pop(i)


def add():
    print("!" * 10, "TOATE CAMPURILE SUNT OBLIGATORII", "!" * 10)
    basme.append({
        'nume_basm': input("Introduceti numele basmului").title(),
        'tara_prov': input("Introduceti tara de provinienta a basmului").title(),
        'rating': float(input("Introducet popularitatea basmului"))
    })
    print(f"A fost adaugat basmul \n======= {basme[-1]['nume_basm']}==========\n"
          f"Originar din {basme[-1]['tara_prov']}\n"
          f"cu popularitatea : {basme[-1]['rating']}")


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
