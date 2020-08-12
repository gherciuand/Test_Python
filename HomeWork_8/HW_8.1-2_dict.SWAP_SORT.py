# ======= SORTAREA PARTIDELOR DUPA ALEGERI 2019 =========

# ---Datele partidelor---

partid = [
    {"nume": "ACUM", "orientarea": "Pro_vest", "voturi": 25.74, "mandate": 26},
    {"nume": "PD", "orientarea": "Pro_vest", "voturi": 29.70, "mandate": 30},
    {"nume": "PSRM", "orientarea": "Pro_est", "voturi": 34.65, "mandate": 35},
    {"nume": "Cand_Indep", "orientarea": "Individual", "voturi": 2.97, "mandate": 3},
    {"nume": "PP_SOR", "orientarea": "Statalist", "voturi": 6.93, "mandate": 7}
]


# --- defenirea functiei de schimbarea cu locul

def swap(n):
    temp = partid[n]
    partid[n] = partid[n + 1]
    partid[n + 1] = temp


# ---sortarea dupa voturi acumulate (ascendent / descendent)
def sort(ascendic=False):
    if ascendic == 0:
        for j in range(len(partid)):
            for i in range(len(partid) - 1):
                if partid[i]["voturi"] < partid[i + 1]["voturi"]:
                    swap(i)
    else:
        for j in range(len(partid)):
            for i in range(len(partid) - 1):
                if partid[i]["voturi"] > partid[i + 1]["voturi"]:
                    swap(i)


# ---Afisare rezultat---

sort(True)
print('Lista partidelor:')
for p in partid:
    print(f' >> {p["nume"]:10s} (orientarea - {p["orientarea"]:10s})'
          f' {p["voturi"]:10f}% -- {p["mandate"]:2} mandate in parlament ')
