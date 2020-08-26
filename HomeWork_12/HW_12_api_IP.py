import requests
import json

query = None
data = {'status': None}


def menu_domen():
    option = None
    while option != "0":
        print("\n")
        print(f'Te rugam sa selectezi datele care te intereseaza despre'
              f'\n {query:^30}')
        print(f"1 - Informatia juridica a {query}:"
              f"\n\t Adresa (tara, orasul), codul postal, denumirea. ")
        print(f"2 - Informatia geografica a {query} :\n"
              f"\t Continentul, tara, coordonatele geografice, fusul orar, valuta tarii")
        print(f'* - Incerca o alta cautare:')
        print("0 - Parasire menu")
        option = input()
        if option == "0":
            exit("Va multumim ca ati testat serviciul nostru")
        if option == "1":
            print(f'Tara -           {data["country"]}\n'
                  f'Orasul -         {data["city"]}\n'
                  f'Cod postal -     {data["zip"]}\n'
                  f'Nume detinator - {data["org"]}\n ')
        if option == "2":
            print(f'Continent -      {data["continent"]}\n'
                  f'Tara -           {data["country"]}\n'
                  f'Orasul -         {data["city"]}\n'
                  f'Latidudinea -    {data["lat"]}\n'
                  f'Longitudinea -   {data["lon"]}\n'
                  f'Fus orar -       {data["timezone"]}\n'
                  f'Valuta -         {data["currency"]}\n')
        if option == "*":
            return None


print("*" * 15, "Salut", "*" * 15)
print("Ai accesat cautarea info dupa DOMEN sau IP")

while query != "0":
    query = input("Introduceti numele DOMEN sau adresa IP: \n"
                  "0 - pentru iesire\n")
    if query != "":
        endpoint = f'http://ip-api.com/json/{query}?fields=status,message,continent,country,' \
                   f'region,city,zip,lat,lon,timezone,currency,org' \

        response = requests.get(endpoint)
        data = json.loads(response.text)
        if data['status'] == 'success':
            menu_domen()
        elif query == "0":
            break
        else:
            print(f'Ne pare rau {query} nu a fost gasit')
        pass
    else:
        exit(f'Nu a fost introdusa nici o solicitare\n'
             f'Presupunem ca ai intrat din gresiala aici \n'
             f'☺ SUCCES ☺')
        break
