def ex41():
    from datetime import date

    x = date(int(input("Ano: ")), int(input("Mês: ")), int(input("Dia: ")))
    ano = x.year
    mes = x.month
    dia = x.day
    if x.month <= date.today().month and x.day <= date.today().day:
        idade = date.today().year - x.year
    else:
        idade = date.today().year - x.year - 1
    print("Você tem {} anos. Está na categoria ".format(idade),end="")
    if idade <= 9:
        print("mirim.")
    elif idade > 9 and idade <= 14:
        print("infantil.")
    elif idade > 14 and idade <= 18:
        print("junior.")
    elif idade > 18 and idade <= 20:
        print("sênior.")
    else:
        print("master.")

def ex42():
    x = float(input("Digite o comprimento da reta 1: "))
    y = float(input("Digite o comprimento da reta 2: "))
    z = float(input("Digite o comprimento da reta 3: "))
    if x + y > z and x + z > y and y + z > x:
        print("Formou um triângulo ",end='')
        if x == y == z:
            print("equilátero.")
        elif x != y != z != x:
            print("escaleno.")
        else:
            print("isósceles.")
    else:
        print("Não formou um triângulo.")

def ex43():
    altura = float(input("Digite altura: "))
    peso = float(input("Digite peso: "))
    imc = peso / (altura ** 2)
    print("Seu IMC é {:.1f}kg/m². ".format(imc),end="")
    if imc < 18.5:
        print("Está abaixo do peso.")
    elif 18.5 <= imc < 25:
        print("Peso ideal.")
    elif 25 <= imc < 30:
        print("Sobrepeso.")
    elif 30 <= imc < 40:
        print("Obesidade.")
    else:
        print("Obesidade mórbida.")

def ex44():
    i = 0
    while i < 1:
        x = float(input("Digite valor do produto: "))
        y = int(input("Digite pagamento (1-dinheiro, 2-cartão): "))
        if y == 2:
            z = int(input("Digite o número de parcelas: "))
            print("Seu produto vai custar R$", end="")
            if z <= 1:
                print(f"{x - x * 0.05:.2f} com 5% de desconto.")
            elif z == 2:
                print(f"{x} sem desconto.")
            else:
                print(f"{x + x * 0.2:.2f} com 20% de juros.")
            i += 1
        elif y == 1:
            print(f"Seu produto vai custar R${x - x * 0.1:.2f} com 10% de desconto.")
            i += 1

def ex45():
    from random import randint

    x = int(input("Insira nº de partidas: "))
    y = 0
    ptJ = 0
    ptP = 0
    jogadas = ["","pedra", "papel", "tesoura"]
    while y < x:
        pc = randint(1,3)
        jog = int(input("Digite 1 para PEDRA, 2 para PAPEL ou 3 para TESOURA: "))
        print(f"\nVocê jogou {jogadas[jog]}.")
        if jog == pc:
            ganhou = "empatou."
        elif (jog == 1 and pc == 2) or (jog == 2 and pc == 3) or (jog == 3 and pc == 1):
            ganhou = "perdeu."
            ptP += 1
            y += 1
        else:
            ganhou = "ganhou!"
            ptJ += 1
            y += 1

        print(f"O adversário jogou {jogadas[pc]}.\nVocê {ganhou}\nJogador: {ptJ}\nAdversário: {ptP}\n")

        if y == x:
            if ptJ == ptP:
                print("Pra desempatar! ",end="")
                y -= 1
            elif ptJ > ptP:
                print("==========VOCÊ VENCEU!==========")
            else:
                print("==========VOCÊ PERDEU...==========")

def ex46():
    from time import sleep

    for x in range(10, -1, -1):
        print(x)
        sleep(1)
    print("FOGO!!!")

def ex47():
    for x in range(1, 51, 2):
        print(x)

def ex48():
    s = 0
    for x in range(0, 501, 3):
        if x % 2 != 0:
            print(x)
            s += x
    print(s)

def ex48Prof():
    soma = 0
    cont = 0
    for c in range(1, 501, 2):
        if c % 3 == 0:
            soma += c
            cont += 1
    print(f"A soma entre os {cont} números é igual a {soma}.")

def ex49():
    n = int(input("Digite um número inteiro: "))
    tam = int(input("Digite tamanho da tabuada: "))
    print(f"TABUADA DE {n}:")
    for x in range(1, tam + 1):
        print(f"{n} x {x:2} = {n * x}")

def ex50():
    n = []
    s = 0
    for x in range(0,6):
        n.append(int(input("Insira um número: ")))
        x -= 1
        if n[x] % 2 == 0: s += n[x]
    print(f"A soma de todos os números pares é: {s}")

def ex50Prof():
    soma = 0
    cont = 0
    for c in range(1,7):
        num = int(input(f"Digite o valor {c}: "))
        if num % 2 == 0:
            soma += num
            cont += 1
    print(f"Você informou {cont} números pares. O resultado da soma foi {soma}.")
