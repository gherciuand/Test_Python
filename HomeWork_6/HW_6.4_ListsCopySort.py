# ------------------------Unique list of guests-----------------

# Definirea variabilelor
guests_1 = ["Bethaney Bain", "Kacey Johns", "Manpreet Saunders"]
guests_2 = ["Elwood Curtis", "Diya Griffin", "Kacey Johns"]
guests_3 = ["Tobey Weiss", "Kadie Barnes", "Diya Griffin"]
guest_unique = []
n = 0

guest_All = guests_1 + guests_2 + guests_3
for n in range(len(guest_All)):  # Parcurgerea prin lista comuna
    if guest_All[n] not in guest_unique:  # Conditionarea copierii
        guest_unique.append(guest_All[n])  # Adaugarea in lista unica
        n += 1
print("1.unique-", guest_unique)
guest_unique.sort()  # Sortarea listei
print("2.sort -", guest_unique)

# -------------------- Variana II (simplificata) -----------------

# guest_unique = list(dict.fromkeys(guest_All))
# print(guest_unique)
