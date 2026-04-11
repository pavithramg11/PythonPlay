s = "aabbcdydccssr"

smap = {}
for c in s:
    smap[c] = smap.get(c, 0)+1

def firstnonrepeating(s):
    for c in s:
        if smap[c] == 1:
            return c


print(firstnonrepeating(s))
