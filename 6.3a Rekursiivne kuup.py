def kuup(jarj):
    if len(jarj) == 0:
        return []
    return[jarj[0] ** 3] + kuup(jarj[1:])
