import pandas as pd


def taienda_tabelit(tabel):
    tabel = tabel.drop(['2012'], axis=1)
    tabel['Keskmine'] = tabel[list(tabel.columns)].mean(axis=1)
    return tabel


def raamatukogud(name):
    andmed = pd.read_csv(name, delimiter=';')
    andmed = andmed.set_index(' ')
    tabel = taienda_tabelit(andmed)
    tabel.to_csv('raamatukogud_uus.csv', sep=';')


raamatukogud('raamatukogud.csv')
