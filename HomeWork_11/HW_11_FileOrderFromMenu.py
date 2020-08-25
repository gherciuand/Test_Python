from os import path

menu_file = "menu.txt"
order_file = "order.txt"
output_file = "Output_order.txt"

if path.exists(menu_file) and path.exists(order_file):
    print (f'You can place the order')
    menu = open(menu_file, "r")
    order = open(order_file, "r")
    output_order = open(output_file, "w")
    output_order.write(f'Your order is:\n\n')
    list_line_m = menu.readlines()
    list_line_o = order.readlines()
    list_menu=[]
    list_order=[]
    total_price=[]
    for i in range(len(list_line_m)):
        list_menu.append(list_line_m[i].strip().split("-"))
        for j in range(len(list_line_o)):
            list_order.append(list_line_o[j].strip().split("-"))
            if list_order[j][0]==list_menu[i][0]:
                tp = int(list_order[j][1])*int(list_menu[i][1])
                total_price.append(tp)
                print(f'You ordered: '
                  f'{list_order[j][0]:>15} - quantity {str(list_order[j][1]):2} pcs,'
                  f' price {str(int(list_order[j][1])*int(list_menu[i][1])):>4} {list_menu[i][2]}')
                output_order.write(
                  f'{list_order[j][0]:15} - quantity {str(list_order[j][1]):2} pcs,'
                  f' price {str(int(list_order[j][1])*int(list_menu[i][1])):>4} {list_menu[i][2]}\n')
    print(f'Total price:{"-"*40}  {sum(total_price):>4} MDL')
    output_order.write(f'\nTotal price:{"-"*27}  {sum(total_price):>4} MDL')
else:
    print(f'You can NOT place the order, some files missing')
