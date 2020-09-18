with open("referat.txt","r",encoding="utf-8") as f:
    tref = f.read()
    print(len(tref))
    nword = len(tref.split())
    print(nword)
    a = (tref.replace(".","!"))
    with open("referat2.txt","w",encoding="utf-8") as f1:
        f1.write(a)