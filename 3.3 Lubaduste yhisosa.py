def kooslubajad(hulk):
    """(set) -> tuple.

       Võtab argumendiks järjendi erakondade lubaduste hulkadest ja tagastab
       paarina (kaheelemendilise ennikuna) nende kahe erakonna indeksid
       järjendis, mille lubadustel on kõige suurem ühisosa. Kui selliseid paare
       on mitu, siis võib neist ükskõik millise tagastada.
       >>> kooslubajad([{"maamaks kaotada",
                         "pensione tõsta",
                         "kaitsekulutusi tõsta"},
                        {"lasteaiaõpetajate palku tõsta",
                         "kindlustada tasuta hambaravi kuni 30-aastastele"},
                        {"sisserännet piirata",
                         "pensione tõsta",
                         "kaitsekulutusi tõsta"},
                        set()])
       (0, 2)
    """
    suurus = 0
    suurimad = [0, 0]
    for i in range(len(hulk)):
        for j in range(i + 1, len(hulk)):
            if (len(hulk[i] & hulk[j])) >= suurus:
                suurus = len(hulk[i] & hulk[j])
                suurimad[0] = i
                suurimad[1] = j

    return tuple(suurimad)


print(kooslubajad([{'algatada koduloometoetus', 'rajada spordiväljakud igasse linna', 'suurendada kõiki palkasid', 'kuritegevust vähendada', 'kõiki toetusi suurendada', 'kaotada kõik maksud'}, {'toetada pensionäre', 'vähendada suremust', 'suurendada vastsündinute arvu', 'edendada maaelu', 'aidata noorperesid'}]))
