def vahimatest_suurim(järjend):
    ''' (list) -> int
    Funktsioon võtab argumendiks täisarvude maatriksi kahemõõtmelise järjendina
    ja tagastab antud maatriksist kõikide ridade vähimatest elementidest suurima.
    >>> vahimatest_suurim([[3, 0], [0, -1], [2, 1]]) 
    1
    >>> vahimatest_suurim([[3, 0], [0, -1], [2, 2]]) 
    2
    >>> vahimatest_suurim([[3, 0]]) 
    0
    >>> vahimatest_suurim([[0], [1], [2], [3], [-1]]) 
    3
    '''
    vähimad_elemendid = []
    for liige in järjend:
        vähimad_elemendid.append(min(liige))
    return (max(vähimad_elemendid))