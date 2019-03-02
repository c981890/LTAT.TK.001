def pikim_pikkus(struktuur):
    if (not isinstance(struktuur, list)):
        return 0
    jarjend = len(struktuur)
    for element in struktuur:
        pikim_jarjend = pikim_pikkus(element)
        if jarjend < pikim_jarjend:
            jarjend = pikim_jarjend
    return jarjend
