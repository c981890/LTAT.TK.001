def yhisosa(jarjend1, jarjend2):
    """ (list, list) -> list.

    Võtab argumendiks kaks järjendit ja tagastab uue järjendi, mis sisaldab
    ühekordselt neid elemente, mis esinesid mõlemas sisendjärjendis. Tagastatav
    järjend sisalab ainult neid elemente, mis eelnevale tingimusele vastavad.
    >>> yhisosa(['ich', 'du', 'er', 'sie', 'es'], ['wir', 'ihr', 'sie', 'Sie'])
    ['sie']
    >>> yhisosa([], [1, 1])
    []
    >>> yhisosa([1, 1, 1], [1, 1])
    [1]
    """
    yhised_elemendid = []
    for i in jarjend1:
        for j in jarjend2:
            if i == j and i not in yhised_elemendid:
                yhised_elemendid.append(i)
    print(yhised_elemendid)
    return yhised_elemendid
