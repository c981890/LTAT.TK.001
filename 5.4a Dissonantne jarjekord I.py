def on_rahulik(arvamus1, arvamus2, erinevus):
    return abs(arvamus1 - arvamus2) <= erinevus or arvamus1 * arvamus2 >= 0


def dissonantside_arv(arvamused, lubatud_erinevus):
    dissonantsid = 0
    for i in range(len(arvamused) - 1):
        # print(arvamused[i], arvamused[i+1])
        if on_rahulik(arvamused[i], arvamused[i+1], lubatud_erinevus) is False:
            dissonantsid += 1
    return dissonantsid
