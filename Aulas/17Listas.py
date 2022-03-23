def p01():
    nums = [2, 5, 9, 11]
    print(f"Declaração {nums}")

    nums[2] = 3
    print(f"lista[x] = y: {nums}")

    nums.append(7)
    print(f"append 7: {nums}")

    nums.sort(reverse=True)
    print(f"Sort reverse: {nums}")

    nums.insert(2, 2)
    print(f"Insert: {nums}")

    nums.pop()
    print(f"Pop: {nums}")

    del nums[3]
    print(f"Del: {nums}")

    nums.remove(2)
    print(f"Remove: {nums}")

    print(f"Essa lista tem {len(nums)} elementos.")

def p02():
    valores = list()
    valores.append(5)
    valores.append(9)
    valores.append(4)
    for c, v in valores:
        print(f"Na posição {c} encontrei o valor {v}! ", end=' ')
    print("Cheguei ao final da lista")

def p03():
    a = [2,3,4,7]
    #Faz uma ligação entre as listas: b = a
    b = a[:]
    b[2] = 8
    print(a)
    print(b)

p03()