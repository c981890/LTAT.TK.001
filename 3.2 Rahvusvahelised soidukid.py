def failist_sonastik(failinimi):
    ''' (file) -> dict

    Võtab argumendiks andmebaasi faili nime ning tagastab vastava faili sisu
    põhjal sõnastiku, kus võtmeteks on riigitähised (sõned) ja väärtusteks
    riikide nimed (sõned).

    >>> failist_sonastik("aasia.txt")
    {'J': 'Jaapan', 'SGP': 'Singapur', 'IND': 'India', 'LAO': 'Laos',
    'T': 'Tai', 'CHN': 'Hiina'}
    '''

    fail = open(failinimi, encoding="UTF-8")
    sonastik = {}
    for rida in fail:
        osad = rida.strip('\n').split(' ')
        sonastik[osad[0]] = osad[1]
    fail.close()

    return sonastik


# print(failist_sonastik("aasia.txt"))


def tahised_nimedeks(jarjend, funktsioon):
    """(list, function) -> list.

    Võtab argumendiks järjendi riikide tähistest (sõned) ja failist_sonastik
    funktsiooni poolt koostatud sõnastiku ning tagastab järjendi vastavate
    riikide nimedest. Kui mõni tähis argumendiks antud järjendis on tundmatu,
    siis selle riigi nimi tuleb asendada tagastatavas järjendis väärtusega
    None.

    >>> tahised_nimedeks(['FIN', 'RUS', 'CHN', 'IND', 'F', 'LAO'],
    failist_sonastik("aasia.txt"))
    [None, None, 'Hiina', 'India', None, 'Laos']
    """
    loppjarjend = []

    for element in jarjend:
        if element in funktsioon:
            loppjarjend.append(funktsioon[element])
        else:
            loppjarjend.append(None)
    return loppjarjend


# print(tahised_nimedeks(['FIN', 'RUS', 'CHN', 'IND', 'F', 'LAO'],
#       failist_sonastik("aasia.txt")))

failinimi = input('Sisestaga andmebaasi faili nimi: ')

piiriyletajad = input('Piiriületajad: ')
jarjend = piiriyletajad.split(' ')


failist_sonastik(failinimi)
for element in tahised_nimedeks(jarjend, failist_sonastik(failinimi)):
    if element is None:
        print('Tundmatu maa')
    else:
        print(element)
