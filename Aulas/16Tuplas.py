lanche = ("Ham", "Suco", "Pizza", "Pudim", "Crepe", "Pastel", "Refri", "Bolo")
#Tuplas são imutáveis. Boas práticas: usar ()

def p01():
    print(lanche[2:])
    print(lanche[2:5])
    print(lanche[:5])
    print(lanche[0::2])
    print(lanche[-1])
    print(lanche[-8:])

def p02():
    for x in range(0, len(lanche)):
        print(f"Lanche: {lanche[x]}.")
    print()
    for x in lanche:
        print(f"Lanche: {x}.")
    print()
    for x, y in enumerate(lanche):
        print(f"Lanche: {y} na posição {x}.")

def p03():
    print(sorted(lanche))

def p04():
    a = (2, 5, 8, 5)
    b = (3, 9, 27)
    c = a + b
    d = b + a
    print(f"{c}\n{sorted(d)}")
    print(c.count(5))
    print(c.index(2))
    print(c.index(5,2))

def p05():
    tupla = ("String", 2, True, 3.2)
    print(tupla)

def p06():
    tupla = ("String", 2, True, 3.2)
    del(tupla)
    print(tupla)
