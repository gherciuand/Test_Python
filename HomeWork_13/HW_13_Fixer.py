import requests
import json
import datetime as dt
from os import path
print(f'{"Welcome to my convertor":^30}\n'
      f'{"Referance currency is EUR":^30}\n')

def get_data(day):
    key = '840651f9dd1199f82f94b9340154cdcf'
    endpoint = 'http://data.fixer.io/api/' + day + '?access_key=' + key + '&symbols=USD,MDL,RUB'
    file_name = f'./rates_{day}.json'

    if path.exists(file_name):
        file_name = open(file_name, 'r')
        data = json.loads(file_name.read())
    else:
        response = requests.get(endpoint)
        data = json.loads(response.text)
        file = open(file_name, 'w')
        file.write(response.text)
        file.close()

    if data['success'] is False:
        print('CANNOT ACCESS THE DATE')
    else:
        return data

def show_rates(day):
    data = get_data(day)
    if data['success'] is False:
        print('CANNOT ACCESS THE DATE')
    else:
        print(f'EUR = {round(data["rates"]["USD"], 3):>7} USD\n'
              f'EUR = {round(data["rates"]["MDL"], 3):>7} MDL\n'
              f'EUR = {round(data["rates"]["RUB"], 3):>7} RUB\n')

def convertor(sum_val):
    data = get_data(str(dt.date.today()))
    try:
        from_val = data['rates'][input('enter the code currency "from"  ').upper()]
    except KeyError:
        from_val = 1
    try:
        to_val = data['rates'][input('enter the code currency "to"  ').upper()]
    except KeyError:
        to_val = 1
    echiv = sum_val / (from_val / to_val)
    print(echiv)

def evolution(start, end, currency):
    count = 0
    while count < 3:
        try:
            s = dt.date.fromisoformat(start)
            e = dt.date.fromisoformat(end)
            period = str(e - s).split(" ", 3)
            p = int(period[0])
            if p > 31:
                print('Please set period less or equal than 31 day')
                start = input('start')
                end = input('end')
                pass
            else:
                o = 0
                while o <= p:
                    date_ev = (s + dt.timedelta(o))
                    data = get_data(str(date_ev))
                    print(f'For {date_ev}   1 EUR = {data["rates"][currency]} {currency}')
                    o = o + 1
                return date_ev
        finally:
            count += 1
            if count == 3:
                return False

def menu():
    option = None
    while option != 0:
        print(f'\nPlease select the option:\n'
              f'\t1 - show the latest exchange rates\n'
              f'\t2 - show the historical rates\n'
              f'\t3 - convert amount from XXX to YYY\n'
              f'\t4 - show evolution rates for 1 month\n'
              f'\t0 - Exit')
        option = int(input())
        if option == 1:
            show_rates(str(dt.date.today()))
        elif option == 2:
            show_rates(input('Please set the date (format: yyyy-mm-dd)\n'))
        elif option == 3:
            convertor(int(input("Please enter amount:\n")))
        elif option == 4:
            evolution(input('Start date(yyyy-mm-dd): '), input('End date(yyyy-mm-dd): '), input('Cod currency:').upper())
        elif option == 0:
            break
menu()

