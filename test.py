names=["pavi", "amogh", "sakura", "pavi", "sakura","sakura"]
namecount={}
for name in names:
    if name in namecount:
        namecount[name]+=1
    else:
        namecount[name] = 1
for n, c in namecount.items():
    print(n+" = "+str(c))

    