def p01():
    a = 4
    b = 5
    s = a + b
    print(s)
    a = 8
    b = 9
    s = a + b
    print(s)
    a = 2
    b = 1
    s = a + b
    print(s)

def p02():
    def soma(a, b):
        s = a + b
        print(s)
    soma(4, 5)
    soma(8, 9)
    soma(2, 1)
    soma(b=5, a=4)
    #soma(b=5, 4) => NÃO FUNCIONA

def p03_Empacotamento():
    def contador(*num):
        tam = len(num)
        print(f"Número de parâmetros: {tam}\nParâmetros: {num}")
    contador(2, 1, 7)
    contador(8, 0)
    contador(4, 4, 7, 6, 2)

def p04():
    def dobra(lst):
        pos = 0
        while pos < len(lst):
            lst[pos] *= 2
            pos += 1
    valores = [4,2,5,1,2,5,0,8]
    dobra(valores)
    print(valores)

def p05():
    def soma(*num):
        s = 0
        for n in num:
            s += n
        print(f"A soma entre {num} é igual a {s}")
    soma(5, 2)
    soma(4, 9, 12, 3)

p05()