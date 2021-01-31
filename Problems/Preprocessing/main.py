punct_symbols = ",.!?"

text = input()

for symbol in punct_symbols:
    text = text.replace(symbol, "")

print(text.lower())
