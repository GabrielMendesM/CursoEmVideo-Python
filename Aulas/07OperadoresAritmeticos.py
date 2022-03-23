def operadoresAritmeticos():
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))

    res = n1 ** (1 / 2)
    print("Raiz quadrada = {};".format(res))

    res = n1 ** (1 / 3)
    print("Raiz cúbica = {}.".format(res))

    print()

    print("RESULTADO EM ORDEM DE PRECEDÊNCIA")

    res = n1 ** n2
    print("Potência = {}".format(res))

    res = n1 * n2
    print("Multiplicação = {}".format(res))

    res = n1 / n2
    print("Divisão = {}".format(res))

    res = n1 // n2
    print("Divisão sem resto = {}".format(res))

    res = n1 % n2
    print("Resto da divisão = {}".format(res))

    res = n1 + n2
    print("Soma = {}".format(res))

    res = n1 - n2
    print("Subtração = {}".format(res))

def printa():
    var = "Ahdisahds"
    print("Frase {:20}!".format(var))
    print("Frase {:>20}!".format(var))
    print("Frase {:<20}!".format(var))
    print("Frase {:^20}!".format(var))
    print("Frase {:=>20}!".format(var))
    print("Frase 1\nFrase 2\nFrase 3", end=">>>>")
    print("Frase 4")

#operadoresAritmeticos()
#printa()

casaDeci = 9/4
print(f"!{casaDeci:=^20}!")
