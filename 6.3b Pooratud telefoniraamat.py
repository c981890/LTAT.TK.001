def kes_on(arv, jarj):
    if len(jarj) == 0:
        return None
    if jarj[0][0] == arv:
        return jarj[0][1]
    return kes_on(arv, jarj[1:])
