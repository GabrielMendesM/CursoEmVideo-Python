def ex61():
    primeiro = int(input("Primeiro termo: "))
    razao = int(input("Razão: "))
    aux = 0
    x = 0
    print(primeiro, end=' → ')
    while aux < 9:
        x += razao
        print(primeiro + x,end=' → ')
        aux += 1
    print("ACABOU")

def ex62():
    primeiro = int(input("Primeiro termo: "))
    razao = int(input("Razão: "))
    aux2 = 1
    x = 0
    while aux2 > 0:
        aux1 = 0
        aux2 = int(input("Quantos termos deseja mostrar: "))
        while aux1 < aux2:
            print(primeiro + x,end=' → ')
            x += razao
            aux1 += 1
        print()
    print("ACABOU")

def ex63():
    n = int(input("Digite a quantidade de elementos da sequência de Fibonacci a serem mostrados: "))
    print()
    aux = 0
    x = 1
    y = 0
    while aux < n - 1:
        z = x + y
        x = y
        y = z
        print(f"{z}, ", end='')
        aux += 1
    print(x + y)

def ex64():
    print("Digite números inteiros e aperte Enter.\nDigite 999 para finalizar.")
    x = 0
    y = 0
    s = 0
    while x != 999:
        y += 1
        x = int(input("Digite: "))
        s += x
    print(f"{y-1} números foram digitados.\nA soma entre eles é {s-999}")

def ex65():
    print("Digite números inteiros e aperte Enter.\nDigite 0 para finalizar.")
    x = 1
    y = s = 0
    maior = 0
    menor = 1e999
    print(menor)
    while x != 0:
        y += 1
        x = int(input(f"Número {y}: "))
        s += x
        if x > maior:
            maior = x
        if x < menor and x != 0:
            menor = x
    print(f"A média aritmética entre todos os números é {s/(y - 1):.0f}\nO maior é {maior}\nO menor é {menor}")

def ex66():
    print("Digite números inteiros e aperte Enter.\nDigite 999 para finalizar.")
    x = y = s = 0
    while True:
        x = int(input("Digite: "))
        if x == 999:
            break
        y += 1
        s += x
    print(f"{y} números foram digitados.\nA soma entre eles é {s}")

def ex67():
    while True:
        n = int(input("Digite um número inteiro (número negativo finaliza o programa): "))
        if n < 0:
            break
        print(f"TABUADA DE {n}:")
        for x in range(1,11):
            print(f"{n} x {x:2} = {n * x}")
    print("FIM")

def ex68():
    from random import randint
    ia = jog = vit = 0
    esc = ''
    while True:
        ia = randint(0,10)
        esc = str(input("Par ou ímpar? [P/I]")).strip().upper()[0]
        while esc not in "PI":
            esc = str(input("Opção inválida. Par ou ímpar? [P/I]")).strip().upper()[0]
        jog = int(input("Digite um número de 0 a 10: "))
        while jog > 10 or jog < 0:
            jog = int(input("Opção inválida. Digite um número de 0 a 10: "))
        if (ia + jog) % 2 == 0:
            if esc == "P":
                print(f"O computador escolheu {ia}. {ia} + {jog} = {ia + jog}. Você venceu!")
                vit += 1
            else:
                break
        else:
            if esc == "I":
                print(f"O computador escolheu {ia}. {ia} + {jog} = {ia + jog}. Você venceu!")
                vit += 1
            else:
                break
    print(f"O computador escolheu {ia}. {ia} + {jog} = {ia + jog}. Você perdeu!\nForam {vit} vitórias consecutivas.")

def ex69():
    idade = homem = mulher = maior = 0
    while True:
        idade = int(input("Digite a idade: "))
        sexo = str(input("Digite o sexo: [M/F]")).strip().upper()[0]
        while sexo not in "MF":
            sexo = str(input("Opção inválida. Digite o sexo: [M/F]")).strip().upper()[0]
        if idade > 18:
            maior += 1
        if sexo == "M":
            homem += 1
        elif sexo == "F" and idade < 20:
            mulher += 1
        cont = input("Quer continuar? [S/N]").strip().upper()[0]
        while cont not in "SN":
            cont = input("Opção inválida. Quer continuar? [S/N]").strip().upper()[0]
        if cont == "N":
            break
    print(f"{maior} pessoas têm mais de 18 anos.\n{homem} são homens.\n{mulher} têm menos de 20 anos.")

def ex70():
    total = caro = 0
    barato = 1e999
    baratoNome = ''
    while True:
        nome = str(input("Nome do produto: ")).strip().title()
        preco = float(input("Digite o preço: R$"))
        total += preco
        if preco > 1000:
            caro += 1
        if preco < barato:
            barato = preco
            baratoNome = nome
        cont = input("Quer continuar? [S/N]").strip().upper()[0]
        while cont not in "SN":
            cont = input("Opção inválida. Quer continuar? [S/N]").strip().upper()[0]
        if cont == "N":
            break
    print(f"O total da compra deu R${total:.2f}.\n{caro} produtos custam mais de R$1000.00.\n{baratoNome} é o produto mais barato.")
