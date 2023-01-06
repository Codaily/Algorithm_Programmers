def solution2(babbling):
    enables = ["aya", "ye", "woo", "ma"]

    counter = 0
    for babble in babbling:

        for enable in enables:
            babble = babble.replace(enable, " ").strip()
            if len(babble) == 0:
                counter += 1
                break

    return counter
