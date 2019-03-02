'''
bingo_tabel = [[1, 30, 34, 55, 75],
               [10, 16, 40, 50, 67],
               [5, 20, 38, 48, 61],
               [4, 26, 43, 49, 70],
               [15, 17, 33, 51, 66],
               ]
'''


def on_bingo_tabel(bingo_tabel):
    ''' (list) -> Boolean
    Võtab argumendiks 5 x 5 maatriksi, milles iga element on täisarv lõigust
    1 - 75, ning tagastab tõeväärtuse vastavalt sellele, kas arvud selles
    tabelis on veergudesse jaotatud vastavalt Bingo Loto reeglitele.
    >>> on_bingo_tabel([[1, 30, 34, 55, 75], [10, 16, 40, 50, 67], [5, 20, 38, 48, 61], [4, 26, 43, 49, 70], [15, 17, 33, 51, 66]]) 
    True
    >>> on_bingo_tabel([[1, 30, 34, 55, 76], [10, 16, 40, 50, 67], [5, 20, 38, 48, 61], [4, 26, 43, 49, 70], [15, 17, 33, 51, 66]])
    False
    '''
    for i in range(len(bingo_tabel)):
        for j in range(len(bingo_tabel[i])):
            if not (bingo_tabel[i][j] >= j * 15 + 1 and bingo_tabel[i][j] <= j * 15 + 15):
                return False
    return True

#print(on_bingo_tabel(bingo_tabel))
        
        
        
        
        
        