def kastid_korras(maatriks):
    # Vaatame igat 3x3 kasti
    for rea_nurk in range(0, 9, 3):
        for veeru_nurk in range(0, 9, 3):
            # Iga kasti korral kogume tema elemendid järjendisse 'kast'
            kast = []
            for i in range(3):
                for j in range(3):
                    kast.append(int(maatriks[rea_nurk + i][veeru_nurk + j]))
            # Ja kontrollime, kas elemendid on korrektsed
            if sorted(kast) != list(range(1, 10)):
                return False
    return True


def read_korras(maatriks):
    for rida in maatriks:
        if sorted(rida) != list(range(1, 10)):
            return False
    return True


def veerud_korras(maatriks):
    for veerg in range(len(maatriks[0])):
        kast = []
        for rida in range(len(maatriks)):
            kast.append(maatriks[rida][veerg])
        if sorted(kast) != list(range(1, 10)):
            return False
    return True

failinimi = input('Sisestage failinimi: ')
maatriks = []
fail = open(failinimi, encoding="UTF-8")
for rida in fail:  # iga rea jaoks failist
    arvud = []  # kogume ühe rea arve
    osad = rida.split()
    for osa in osad:  # osade kaupa
        arvud.append(int(osa))
    maatriks.append(arvud)
fail.close()

if kastid_korras(maatriks) and read_korras(maatriks) and veerud_korras(maatriks):
    print('OK')
else:
    print('VIGA')
