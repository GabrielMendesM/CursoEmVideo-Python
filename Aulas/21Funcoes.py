def p01():
    help(print)
    print(print.__doc__)
    help()

def p02():
    def contador(i, f, p):
        """
        Faz uma contagem e mostra na tela
        :param i: inicio da contagem
        :param f: fim da contagem
        :param p: passo da contagem
        :return: sem retorno
        """
        c = i
        while c <= f:
            print(f"{c} ", end="")
            c += p
        print("FIM!")

    contador(0,100,10)
    help(contador)

def p03():
    def somar(a=0, b=0, c=0):
        s = a + b + c
        print(f"A soma vale {s}. ")
    somar(1, 3, 5)
    somar(b=3, a=2)
    somar(1)
    somar()

def p04():
    def teste(b):
        a = 8
        b += 4
        c = 2
        print(f"A dentro vale {a}")
        print(f"B dentro vale {b}")
        print(f"C dentro vale {c}")
    a = 5
    teste(a)
    print(f"A fora vale {a}")

def p05():
    def teste(b):
        global a
        a = 8
        b += 4
        c = 2
        print(f"A dentro vale {a}")
        print(f"B dentro vale {b}")
        print(f"C dentro vale {c}")
    teste(a)
    print(f"A fora vale {a}")
a = 5
# p05()

def p06():
    def somar(a=0, b=0, c=0):
        s = a + b + c
        return s
    r1 = somar(3, 2, 5)
    r2 = somar(1, 7)
    r3 = somar(4)
    print(f"Meus cálculos deram {r1}, {r2} e {r3}.")

def p07():
    def fatorial(num=1):
        f = 1
        for c in range(num, 0, -1):
            f *= c
        return f
    n = int(input("Digite um número: "))
    print(f"O fatorial de {n} é igual a {fatorial(n)}")

def p08():
    def par(n=0):
        if n % 2 == 0:
            return True
        else:
            return False

    num = int(input("Digite um número: "))
    if par(num):
        print("É par!")
    else:
        print("Não é par!")
