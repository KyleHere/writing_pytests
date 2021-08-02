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

    total = 0 #10 #
    i = 0

    while i < len(value):
        current = value[i] # C 100
        previous = value[i-1] # X 10
        if i == 0:
            total += dictionary[current]
        elif dictionary[current] <= dictionary[previous]:
            total += dictionary[current]
        elif dictionary[current] > dictionary[previous]: # 100 > 10
            total -= dictionary[previous] # 10 -= 10
            total += (dictionary[current] - dictionary[previous]) # 0 += 100 - 10
        print(f"{value[i]} : {total}")
        i += 1

    return total

print(parse("MCMLXXII"))
