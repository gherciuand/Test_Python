class Weather:

    # Definim parametri initiali a clasei

    def __init__(self, day, month, year, tmin, tmax, s):
        self.date = {"day": day, "month": month, "year": year}
        self.temp_min = tmin
        self.temp_max = tmax
        self.sky = s
        self.avg_temp = round(((self.temp_min + self.temp_max) / 2), 3)

    #Setam parametri de afisare

    def __str__(self):
        month_str = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        return f'WEATHER for {self.date["day"]}-{month_str[(int(self.date["month"]) - 1)]}-{self.date["year"]} \n' \
               f'Night temperature is {self.temp_min}\u2103\n' \
               f'Day temperature is {self.temp_max}\u2103\n' \
               f'Average temperature is {self.avg_temp}\u2103\n' \
               f'The sky is {self.sky}\n ======================'

    #Definim parametri de comparatie

    def __gt__(self, value):
        return self.temp_max > value.temp_max

    def __eq__(self, other):
        return self.sky == other.sky and (int(other.avg_temp) in range(int(self.avg_temp)-3, int(self.avg_temp)+3))


t_1 = Weather("18", "8", "2020", 16, 25.6, "clear")
t_2 = Weather("19", "8", "2020", 18, 27, "clear")
print(t_1)
print(t_2)

if t_1 > t_2:
    print("Today is hotter then it will be tomorrow")
else:
    print("Tomorrow will be hotter then today")

if t_1 == t_2:
    print("The weather tomarrow will be like today")
