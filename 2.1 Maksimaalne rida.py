failinimi = input('Sisestage failinimi: ')
arvude_tabel = []
fail = open(failinimi, encoding="UTF-8")
for rida in fail:  # iga rea jaoks failist
    arvud = 0  # kogume ühe rea arve
    osad = rida.split()
    for osa in osad:  # osade kaupa
        arvud += int(osa)
 
    arvude_tabel.append(arvud)

fail.close()

print('Suurim summa on failis ' + str(arvude_tabel.index(max(arvude_tabel)) + 1) +
      '. real ja see on ' + str(max(arvude_tabel)) + '.')