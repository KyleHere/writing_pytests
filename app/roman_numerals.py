def parse(value):
    romans = ["I","II","III","IV","V","VI","VII","VIII", "IX"]
    for n in romans:
        if n == value:
            return romans.index(n) + 1
