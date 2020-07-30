########## Suma a doua numere cu verificare tipului variabilei
def suma_num():
    while True:
        try:                   # PASUL 1
            a = float(input("Introduceti primul numar:"))               #se introduce variabila "a"
        except ValueError:                                              #in caz cad type (a) != foat
            print("valoarea introdusa nu este numar, mai incercati:")   #revine la pasul precedent cu mesaj
        else:                                                           #cand conditia este indeplinita trece la PASUL 2
            while True:         #PASUL_2 (similar PAS 1)
                try:
                    b = float(input("Introduceti al doilea numar:"))
                except ValueError:
                    print("valoarea introdusa nu este numar, mai incercati:")
                else:
                    break
            break
    result = a + b
    print("suma numerilor introduse este:", result)
suma_num()
