cellLookup = {
    "wall": "*",
    "empty": " ",
    "path": "·",
    "player": "!",
    "start": "S",
    "end": "E",
    "staircase": "U"
}

def printSymbolLegend():
    print("legend of symbols\n")
    print("{:<15} {:<19}".format("symbol", "map"))
    for name, symbol in cellLookup.items():
        print("{name:<15} {symbol:<19}".format(name=name, symbol=symbol))
