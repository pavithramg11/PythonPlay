s = "hello"

charmap ={}

for c in s:
    charmap[c]=charmap.get(c, 0)+1

for k, v in charmap.items():
    print(k, v)