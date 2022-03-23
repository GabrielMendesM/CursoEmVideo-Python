def ex11():
    largura = int(input("Largura: "))
    altura = int(input("Altura: "))
    print("Tinta: {} litros.".format(largura * altura / 2))

def ex12():
    val = float(input("Valor: "))
    porc = int(input("Porcentagem de desconto: "))
    print("{:.0f}% de desconto = {:.2f}".format(porc, val - val * (porc / 100)))

def ex13():
    val = int(input("Valor: "))
    porc = int(input("Porcentagem de aumento: "))
    print("{}% de acréscimo: {}".format(porc, val + val * (porc / 100)))

def ex14():
    # Converter ºC em ºF
    var = int(input("Digite o ºC: "))
    print("{}ºC = {}ºF".format(var, 9 * var / 5 + 32))

def ex15():
    # input dias alugado e km rodados; R$60 por dia; R$0,15 por km
    dias = int(input("Dias alugado: "))
    km = int(input("Km rodado: "))
    diasR = 60 * dias
    kmR = 0.15 * km
    print("Valor final = {:.2f} ({} por dia rodado + {} por km rodado.".format(800 + (diasR + kmR), diasR, kmR))

def ex16():
    from math import floor
    from math import ceil
    from random import randint

    var = randint(10, 1001)
    deciVar = 0.123456789
    mult = var * deciVar
    print(
        "Número: {}\nNúmero inteiro: {}\nArrendondado para cima: {}\nArredondado para baixo: {}".format(mult, int(mult),
                                                                                                        ceil(mult),
                                                                                                        floor(mult)))

def ex17():
    import math

    catOp = float(input("Insira o comprimento do cateto oposto: "))
    catAd = float(input("Insira o comprimento do cateto adjacente: "))
    hip = math.sqrt(catOp ** 2 + catAd ** 2)

    hipUsandoMath = math.hypot(catOp, catAd)

    print(hipUsandoMath)

def ex18():
    import math

    ang = float(input("Ângulo: "))
    seno = math.sin(math.radians(ang))
    cos = math.cos(math.radians(ang))
    tan = math.tan(math.radians(ang))
    print("Seno = {:.2f}\nCosseno = {:.2f}\nTangente = {:.2f}".format(seno, cos, tan))

def ex19():
    import random

    def Nome():
        n = ["Nome 1", "Nome 2", "Nome 3", "Nome 4"]
        return n

    def Sorteio():
        rand = random.randint(0, 3)
        print("Nome sorteado: ", Nome()[rand])

    def SorteioProf():
        rand = random.choice(Nome())
        print("Nome sorteado: ", rand)

    def SorteioExtra(n):
        random.shuffle(n)
        print(n)

    # Nome()
    # Sorteio()
    # SorteioProf()
    # SorteioExtra(Nome())

def ex20():
    import random

    def Meu():
        a1 = random.randint(0, 3)
        a2 = random.randint(0, 3)
        while a2 == a1:
            a2 = random.randint(0, 3)
        a3 = random.randint(0, 3)
        while a3 == a1 or a3 == a2:
            a3 = random.randint(0, 3)
        a4 = random.randint(0, 3)
        while a4 == a1 or a4 == a2 or a4 == a3:
            a4 = random.randint(0, 3)

        print("Ordem:\n1 - {}\n2 - {}\n3 - {}\n4 - {}".format(ex19().Nome()[a1], ex19().Nome()[a2], ex19().Nome()[a3], ex19().Nome()[a4]))

    def Prof():
        ex19().SorteioExtra(ex19().Nome())

    # Meu()
    Prof()
