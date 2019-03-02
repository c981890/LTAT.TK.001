def seosta_lapsed_ja_vanemad(lapsed, nimed):
    fail = open(nimed, encoding="UTF-8")
    nimed_sonastik = {}
    for rida in fail:
        osad = rida.strip('\n').split(' ', 1)
        nimed_sonastik[osad[0]] = osad[1]
    fail.close()
    seostatud_sonastik = {}
    fail = open(lapsed, encoding="UTF-8")
    lapsed_sonastik = {}
    for rida in fail:
        osad = rida.strip('\n').split(' ')
        lapsed_sonastik[osad[0]] = osad[1]
        vanem = nimed_sonastik[osad[0]]
        laps = nimed_sonastik[osad[1]]
        if vanem not in seostatud_sonastik:
            seostatud_sonastik[vanem] = set()
        seostatud_sonastik[vanem].add(laps)
    fail.close()
    return seostatud_sonastik
