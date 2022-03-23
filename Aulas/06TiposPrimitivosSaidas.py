def EX01():
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    res = n1 + n2
    print("A soma entre {} e {} é igual a {}".format(n1, n2, res))

def EX02():
    var = input("Digite: ")
    print(type(var))
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
    print("Título: {}.".format(var.istitle()))

EX01()
EX02()