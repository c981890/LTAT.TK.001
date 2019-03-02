def kala_kaal(kala_pikkus, fti):
    ''' (int, float) -> int
    Funktsioon võtab argumentideks kala pikkuse (täisarv, sentimeetrites) ja
    kalaliigi tüsedusindeksi (ujukomaarv) ning leiab ja tagastab kala kaalu
    ümardatuna täisgrammideks (arvuna).
    >>> kala_kaal(70, 0.19)
    652
    >>> kala_kaal(12, 1.34) 
    23
    '''
    
    return (round(kala_pikkus ** 3 * fti/100))

failinimi = input('Sisestage failinimi: ')
failisisu = []
f = open(failinimi, encoding="UTF-8")
for rida in f.read().split('\n'):
    failisisu.append(int(rida))
f.close()

püügi_alammõõt = int(input('Sisestage püügi alammõõt: '))
fti = float(input('Sisetage Fultorni tüsedusindeks: '))
kalade_kaalud = []

for i in failisisu:
    if i < püügi_alammõõt:
        print('Kala lasti vette tagasi')
    else:
        print('Püütud kala kaaluga ' + str(kala_kaal(i, fti)) + ' grammi')
    kalade_kaalud.append(round(kala_kaal(i, fti), 3))

raskeim_kala = max(kalade_kaalud)

print('Kõige raskem püütud kala: ' + str(raskeim_kala/1000) + ' kg')
    