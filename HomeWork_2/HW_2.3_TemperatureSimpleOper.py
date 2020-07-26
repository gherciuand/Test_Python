import numpy as np

#Am fugit un pic inaine,
#dar de ce sa nu ma folosesc daca tot am aftat cum.

############## DATA

unit_symbol = "℃"
unit_name = "celsius"
locallity_name = "Chisinau"
date = "26.06.2020"
tepm_mo = 18
temp_no = 32
temp_ev = 30
temp_ni = 22
temp_tot = [tepm_mo,temp_no,temp_ev,temp_ni] #type list for calculating average

############## CALCULATIONS

is_hot_day = temp_no >=25
is_cold_night = temp_ni < 15
is_hot_24h = True if ((is_hot_day == True) and (is_cold_night!= True)) else False

############## PRESENTATION

print("⬔"*40)
print("Locality:          ", locallity_name )
print("Date:              ",date)
print("______AVERAGE______")
print("Average Temp_float:", str(float(np.average(temp_tot)))+unit_symbol)
print("Average Temp_int:  ", str(int(np.average(temp_tot)))+unit_symbol)
print("Average Temp_round:", str(round(np.average(temp_tot)))+unit_symbol)
print("___________________")
print("min Temp:          ",str(min(temp_tot))+unit_symbol)
print("max Temp:          ",str(max(temp_tot))+unit_symbol)
print("Hot day?:          ",str(is_hot_day))
print("Cold night?:       ",str(is_cold_night))
print("Hot during 24h?:   ",str(is_hot_24h))
print("⬔"*40)
