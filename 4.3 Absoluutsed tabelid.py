from copy import deepcopy

def absoluutne_tabel (tabel):
    """(list) -> list.

    Võtab argumendiks kahemõõtmelise arvude järjendi ja tagastab uue
    kahemõõtmelise järjendi, mis on saadud algsest nii, et kõik arvud on
    asendatud nende absoluutväärtustega.
    >>> tabel = [[1, -2], [-3, 4]]
    >>> absoluutne_tabel(tabel)
    [[1, 2], [3, 4]]
    >>> tabel
    [[1, -2], [-3, 4]]
    """
    uus_tabel = deepcopy(tabel)
    for i in range(len(tabel)):
        for j in range(len(tabel[i])):
            uus_tabel[i][j] = abs(tabel[i][j])
    return uus_tabel


def absolutiseeri_tabel (tabel):
    """(list) -> list.

    Võtab argumendiks kahemõõtmelise arvude järjendi ja asendab selles
    järjendis kõik arvud nende absoluutväärtustega. Funktsioon ei tagasta
    midagi.
    >>> tabel = [[1, -2], [-3, 4]]
    >>> absolutiseeri_tabel(tabel)
    >>> tabel
    [[1, 2], [3, 4]]
    """

    uus_tabel = tabel.copy()
    for i in range(len(tabel)):
        for j in range(len(tabel[i])):
            uus_tabel[i][j] = abs(tabel[i][j])
