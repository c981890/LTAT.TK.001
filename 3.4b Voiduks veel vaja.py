def nurkademanguks_vaja(maatriks):
    """Funktsioon tagastab järjendi arvudest, mida on veel vaja loosida selleks,
       et antud mänguväli võidaks nurkademängu.

    """
    i = []
    if maatriks[0][0] != 'X':
        i.append(maatriks[0][0])
    if maatriks[0][-1] != 'X':
        i.append(maatriks[0][-1])
    if maatriks[-1][0] != 'X':
        i.append(maatriks[-1][0])
    if maatriks[-1][-1] != 'X':
        i.append(maatriks[-1][-1])
    return i


print(nurkademanguks_vaja([
                          [1, 'X', 34, 55, 75],
                          ['X', 16, 40, 50, 67],
                          [5, 20, 38, 48, 61],
                          [4, 26, 43, 49, 'X'],
                          ['X', 17, 33, 51, 66]
                          ]))


def peadiagonaalil_vaja(maatriks):
    x = []
    for i in range(len(maatriks)):
        for j in range(len(maatriks)):
            if i == j and maatriks[i][j] != 'X':
                x.append(maatriks[i][j])
    print(x)
    return x


def korvaldiagonaalil_vaja(maatriks):
    x = []
    for i in range(len(maatriks)):
        for j in range(len(maatriks)):
            if i == len(maatriks) - j - 1 and maatriks[i][j] != 'X':
                if maatriks[i][j] not in peadiagonaalil_vaja(maatriks):
                    x.append(maatriks[i][j])
    print(x)
    return x


def diagonaalidemanguks_vaja(maatriks):
    x = peadiagonaalil_vaja(maatriks)
    x.extend(korvaldiagonaalil_vaja(maatriks))
    print(x)
    return x


print(diagonaalidemanguks_vaja([
                         [1, 'X', 34, 55, 'X'],
                         ['X', 'X', 40, 'X', 67],
                         [5, 20, 38, 48, 61],
                         [4, 26, 43, 49, 'X'],
                         ['X', 17, 33, 'X', 66]
                         ]))


def taismanguks_vaja(maatriks):
    x = []
    for i in range(len(maatriks)):
        for j in range(len(maatriks)):
            if maatriks[i][j] != 'X':
                x.append(maatriks[i][j])
    return x


print(taismanguks_vaja([
                        [1, 'X', 34, 'X', 'X'],
                        ['X', 'X', 'X', 'X', 67],
                        [5, 'X', 'X', 48, 61],
                        ['X', 26, 43, 'X', 'X'],
                        ['X', 17, 'X', 'X', 'X']
                       ]))
