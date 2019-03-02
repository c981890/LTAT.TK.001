def symbolite_sagedus(jarjend):
    ''' (str) -> dict

    Funktsioon võtab argumendiks sõne ja tagastab sõnastiku, mis sisaldab
    selles sõnes esinevate tähemärkide esinemiste sagedusi. Tagastatav sõnastik
    sisaldab kirjeid, kus võtmeteks on ühetähemärgilised sõned (sümbolid) ja
    väärtusteks vastavate sõnede (sümbolite) esinemiste arv argumendiks antud
    sõnes.

    >>> symbolite_sagedus("Hommikul silmad on kinni ja huulil on naer")
    {'H': 1, 'o': 3, 'm': 3, 'i': 5, 'k': 2, 'u': 3, 'l': 4, ' ': 7, 's': 1,
    'a': 3, 'd': 1, 'n': 5, 'j': 1, 'h': 1, 'e': 1, 'r': 1}
    '''
    sonastik = {}
    for mark in jarjend:
        sonastik[mark] = jarjend.count(mark)

    return sonastik


print(symbolite_sagedus("Hommikul silmad on kinni ja huulil on naer"))
