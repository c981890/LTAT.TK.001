def listid_sonastikuks(jarjend1, jarjend2):
    """(list, list) -> dict.

    Võtab argumendiks kaks ühepikkust järjendit ja tagastab nende põhjal
    moodustatud sõnastiku, kus võtmeteks on esimese järjendi elemendid ja
    väärtusteks teise järjendi vastavatel positsioonidel olevad elemendid.

    Kui esimeses (võtmete) järjendis on korduvaid elemente, siis sõnastikku
    pannakse neist viimane koos vastava elemendiga väärtuste järjendist.
    Teisisõnu kirjutavad sama võtmega kirjed eelnevaid väärtuseid üle nagu
    sõnastiku puhul ikka kombeks.
    >>> listid_sonastikuks([1, 2], [3, 4])
    {1: 3, 2: 4}
    >>> listid_sonastikuks(['ATI', 'KAMA'],
                           ['Arvutiteaduse instituut', 'Kasutatav masintõlge'])
    {'KAMA': 'Kasutatav masintõlge', 'ATI': 'Arvutiteaduse instituut'}
    >>> listid_sonastikuks([0, 1, 0], ['a', 'b', 'c'])
    {0: 'c', 1: 'b'}
    """
    sonastik = {}
    j = 0

    for i in jarjend1:
        sonastik[i] = jarjend2[j]
        j += 1

    return sonastik
