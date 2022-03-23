def ex1():
    print("Olá, Mundo!")

def ex2():
    var = input("Digite um nome: ")
    print("Nome digitado foi {}.".format(var))

def ex3():
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    res = n1 + n2
    print("A soma entre {} e {} é igual a {}".format(n1, n2, res))

def ex4():
    var = input("Digite: ")
    print("Tipo da variável: ", type(var))
    print("Alfanumérico: {};".format(var.isalnum()))
    print("Alfa: {};".format(var.isalpha()))
    print("? ASCII ?: {};".format(var.isascii()))
    print("Decimal: {};".format(var.isdecimal()))
    print("Dígito: {};".format(var.isdigit()))
    print("Identifier: {};".format(var.isidentifier()))
    print("Lower case: {};".format(var.islower()))
    print("Upper case: {};".format(var.isupper()))
    print("Numérico: {};".format(var.isnumeric()))
    print("Printable: {};".format(var.isprintable()))
    print("Espaço: {};".format(var.isspace()))
    print("Inicial maiúscula: {}.".format(var.istitle()))

def ex5():
    var = int(input("Digite um número: "))
    print("Número {}, antecessor {}, sucessor {}.".format(var, (var - 1), (var + 1)))

def ex6():
    var = int(input("Digite um número: "))
    print("Número {}, dobro {}, triplo {}, raiz quadrada {:.2f}".format(var, (var * 2), (var * 3), (var ** (1 / 2))))

def ex7():
    n = []
    n.append(int(input("Digite o primeiro número: ")))
    n.append(int(input("Digite o segundo número: ")))

    print("Número 1: {}\nNúmero 2: {}\nMédia: {:.1f}".format(n[0], n[1], (n[0] + n[1]) / len(n)))

def ex8():
    var = int(input("Valor em metros: "))
    print("Metros: {}m\nCentímetros: {:.0f}cm\nMilímetros: {:.0f}mm".format(var, var * 100, var * 1000))

def ex9():
    var = int(input("Digite um número: "))
    print("-" * 12)
    print("{} x 1 = {}\n{} x 2 = {}\n{} x 3 = {}\n{} x 4 = {}\n{} x 5 = {}\n{} x 6 = {}\n{} x 7 = {}\n{} x 8 = {}\n{} x 9 "
        "= {}\n{} x 10 = {}".format(var, var, var, var * 2, var, var * 3, var, var * 4, var, var * 5, var, var * 6, var,
                                    var * 7, var, var * 8, var,
                                    var * 9, var, var * 10))
    print("-" * 12)

def ex10():
    real = float(input("Reais: "))
    dolar = float(5.33)
    print("Você tem {:.2f} dólares.".format(real / dolar))
