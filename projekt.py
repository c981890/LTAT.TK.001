import pandas as pd
import matplotlib.pyplot as plot


def kysimused():
    """Kasutajale kuvatakse valikmenüü programmi põhifunktsioonidega."""
    jarjend = aastad("RV045s_mehed.csv")
    print("")
    print("")
    print("  OODATAV ELUIGA")
    while (True):
        print("")
        print("  Tee valik:")
        print("  [1] Oodatav eluiga")
        print("  [2] Milline oleks olnud oodatav eluiga olnud aastatel " +
              jarjend[2] + " - " +
              jarjend[-1])
        print("  [3] Oodatav eluiga läbi aastate graafikul")
        print("  [q] Soov lõpetada ja programm sulgeda")
        vastus = input("  > ")
        kas_lopp = kasud(vastus)
        if kas_lopp == 'q':
            break


def kasud(vastus):
    """Kasutaja valikute parsimine ja vajalike funktsioonide välja
    kutsumine.
    """
    for symbol in vastus:
        if vastus == 'q':
            return 'q'
            break
        elif vastus == '1':
            oodatav_eluiga()
        elif vastus == '2':
            oodatav_eluiga_aastal()
        elif vastus == '3':
            graafik()


def oodatav_eluiga():
    """Tabelist võetakse vastavalt kasutaja sisesatud parameetritele oodatav
    elada jäänud aastate arv.
    """
    print("  Valige sugu:")
    print("  [n] Naine")
    print("  [m] Mees")
    sugu = input("  > ")
    print("  Sisestage vanus:")
    vanus = input("  > ")
    tabel = faili_sisselugemine(sugu)
    print("  Oodatav elada jäänud aastate arv: ",
          tabel.loc["Vanus " + str(vanus), "2017"])


def oodatav_eluiga_aastal():
    """Tabelist võetakse vastavalt kasutaja sisesatud parameetritele oodatav
    elada jäänud aastate arv.
    """
    jarjend = aastad("RV045s_mehed.csv")
    print("  Siin saad uurida, et kui oleks tänase vanuseni jõudnud")
    print("  aastatel " + jarjend[2] + " - " +
          jarjend[-1] +
          ", siis mis oleks oodatav elada jäänud aastate arv.")
    print("  Valige sugu:")
    print("  [n] Naine")
    print("  [m] Mees")
    sugu = input("    > ")
    print("  Sisestage vanus:")
    vanus = input("  > ")
    print("  Mis aastal oleks tänase vanuseni jõudnud?")
    aasta = input("  > ")
    tabel = faili_sisselugemine(sugu)
    print("  Oodatav elada jäänud aastate arv aastal " + aasta + ": ",
          tabel.loc["Vanus " + vanus, str(aasta)])


def graafik():
    """Joonistatkse graafik, kus on näha oodatava eluea muutus aastatel 1989 -
    2017.
    """
    print("  Valige sugu:")
    print("  [n] Naine")
    print("  [m] Mees")
    sugu = input("  > ")

    if sugu == 'm':
        sugu_kaandes = "mehe"
    else:
        sugu_kaandes = "naise"

    print("  Sisestage vanus:")
    vanus = input("  > ")

    tabel = faili_sisselugemine(sugu)
    transponeeritud_andmed = tabel.T
    plot.xlabel("Aastatel")
    plot.ylabel("Oodatav aastate arv")
    plot.title(vanus + " aastase " + sugu_kaandes +
               " oodatav elada jäänud aastate arv")
    transponeeritud_andmed["Vanus " + str(vanus)].plot()
    plot.show()


def faili_sisselugemine(sugu):
    if sugu == "m":
        failinimi = "RV045s_mehed.csv"
    elif sugu == "n":
        failinimi = "RV045s_naised.csv"
    andmed = pd.read_csv(failinimi, delimiter=';')
    andmed = andmed.set_index(' ')
    indexNamesArr = andmed.index.values

    for i in range(len(indexNamesArr)):
        indexNamesArr[i] = "Vanus " + str(i)

    return andmed


def aastad(failinimi):
    """Tagastab järjendi tulpade pealkirjadega."""
    fail = open(failinimi, encoding="UTF-8")
    rida = fail.readline()
    jarjend = rida.strip('\n').strip('"').split(';')
    jarjend = [element.strip('"') for element in jarjend]
    return jarjend


kysimused()
