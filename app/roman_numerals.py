def parse(value):
    # romans = ["I","II","III","IV","V","VI","VII","VIII", "IX","X"]
    dictionary = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    total = 0
    i = 0

    while i < len(value):
        first = value[i]
        second = value[i+1]
        if i == 0:
            total += dictionary[first]
        elif dictionary[first] >= dictionary[second] :
            total += dictionary[first]
        elif dictionary[first] < dictionary[second]:
            total = dictionary[second] - dictionary[first]
        i += 1
    return total




    # for n in romans:
    #     if n == value:
    #         return romans.index(n) + 1
