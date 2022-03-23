def ex71():
    from math import floor

    while True:
        valor = int(input("Digite o valor a ser sacado: R$"))
        cinq = floor(valor / 50)
        cinqrest = valor % 50
        vint = floor(cinqrest / 20)
        vintrest = cinqrest % 20
        dez = floor(vintrest / 10)
        dezrest = vintrest % 10

        print(f"{cinq} notas de R$50,00\n"
              f"{vint} notas de R$20,00\n"
              f"{dez} notas de R$10,00\n"
              f"{dezrest} notas de R$1,00")

        cont = input("Quer continuar? [S/N]").strip().upper()[0]
        while cont not in "SN":
            cont = input("Opção inválida. Quer continuar? [S/N]").strip().upper()[0]
        if cont == "N":
            break

def ex71Prof():
    print("="*30)
    print("{:^30}".format("BANCO CEV"))
    print("="*30)
    valor = int(input("Que valor você quer sacar? R$"))
    total = valor
    ced = 50
    totced = 0
    while True:
        if total >= ced:
            total -= ced
            totced += 1
        else:
            if totced > 0:
                print(f"Total de {totced} cédulas de R${ced}")
            if ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 1
            if total == 0:
                break
    print("="*30 + "\nFIM")

def ex72():
    '''
    Crie um programa q tenha uma tupla totalmente preenchida q tenha uma contagem por extenso de 0 a 20
    O programa vai ler um número pelo teclado e mostrar o valor
    '''
    extenso = ("zero", "um", "doi", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez")
    op = int(input("Digite um número de 0 a 10: "))
    while op < 0 or op > 10:
        op = int(input("Opção inválida. Digite um número de 0 a 10: "))
    print(f"O número digitado foi {extenso[op]}.")

def ex72Prof():
    cont = ("zero", "um", "doi", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
            "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
    while True:
        num = int(input("Digite um número entre 0 e 20: "))
        if 0 <= num <= 20:
            break
        print("Tente novamente. ", end="")
    print(f"Você digitou o número {cont[num]}.")

def ex73():
    '''
    Tupla com os 20 primeiros colocados do Brasileirao, dps mostre
    A) Os 5 primeiros
    B) Os últimos 4
    C) Times em ordem alfabetica
    D) Posição do Santos
    '''
    times = ("Internacional", "Vasco", "AMG", "Palmeiras", "SP", "Santos", "Fluminense", "Bahia", "Grêmio", "APR")
    print(f"TIMES: {times}\n", "=" * 100)
    print(f"A) Os 5 primeiros colocados são: {times[:5]}")
    print(f"B) Os 4 últimos são: {times[-4:]}")
    print(f"C) Em ordem alfabética: {sorted(times)}")
    for pos, x in enumerate(times):
        if "Santos" in x:
            print(f"D) O Santos está na {pos + 1}ª posição.")

def ex73Prof():
    times = ("Internacional", "Vasco", "AMG", "Palmeiras", "SP", "Santos", "Fluminense", "Bahia", "Grêmio", "APR")
    print(f"TIMES: {times}\n", "=" * 100)
    print(f"A) Os 5 primeiros colocados são: {times[:5]}")
    print(f"B) Os 4 últimos são: {times[-4:]}")
    print(f"C) Em ordem alfabética: {sorted(times)}")
    print(f"D) O Santos está na {times.index('Santos') + 1}ª posição.")

def ex74():
    '''
    Gerar 5 números aleatórios e colocar numa tupla
    Mostre a lista e indique o menor e o maior valor da tupla
    '''
    from random import randint

    alea = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
    print(f"Números sorteados foram {alea}")
    maior = 0
    menor = 1e309
    for pos, x in enumerate(alea):
        if alea[pos] > maior:
            maior = alea[pos]
        if alea[pos] < menor:
            menor = alea[pos]
    print(f"O maior é {maior}.\nO menor é {menor}.")

def ex74Prof():
    from random import randint

    numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
    print(f"Eu sorteei os valores {numeros}")
    for n in numeros:
        print(f"{n} ", end="")
    print(f"\nO maior valor sorteado foi {max(numeros)}")
    print(f"O menor valor sorteado foi {min(numeros)}")

def ex75():
    '''
    Leia 4 valores pelo teclado e colocar numa tupla
    A) Quantas vezes apareceu 9
    B) Primeira posição no valor 3
    C) Quais os números pares
    '''
    pares = 0
    nums = (int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: ")))
    print(f"Você digitou {nums}")
    print(f"O número 9 apareceu {nums.count(9)} vezes.")
    if 3 in nums:
        print(f"O número 3 apareceu na {nums.index(3) + 1}ª posição.")
    else:
        print("O número 3 não foi digitado.")
    for x in nums:
        if x % 2 == 0:
            pares += 1
    if pares > 0:
        print("Os valores pares digitados foram ", end='')
        for x in nums:
            if x % 2 == 0:
                print(x, end=' ')
    else:
        print("Nenhum número par foi digitado.")

def ex76Prof():
    '''
    Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços, dna sequencia (ex: Pao, 1, Sal, 5)
    Dps mostre uma lista de preços organizando de forma tabular
    '''
    listagem =  ("Lápis", 1.75,
                 "Borracha", 2,
                 "Caderno", 15.90,
                 "Estojo", 25,
                 "Compasso", 9.99,
                 "Mochila", 120.30)
    print("-" * 40)
    print("LISTAGEM DE PREÇOS")
    print("-" * 40)
    for pos in range(0, len(listagem)):
        if pos % 2 == 0:
            print(f"{listagem[pos]:.<30}", end="")
        else:
            print(f"R${listagem[pos]:>7.2f}")
    print("-" * 40)

def ex77Prof():
    '''
    Crie um progrma q tenha uma tupla com varias palavras
    Dps, para cada palavra, mostrar as vogais
    '''
    palavras = ("João", "Gabriel", "Bia")
    for p in palavras:
        print(f"\nNa palavra {p.upper()} temos ", end='')
        for letra in p:
            if letra.lower() in "ãáâaéêeíióôoúu":
                print(letra, end='')

def ex78():
    '''
    Faça um programa que leia 5 valores numéricos e guarde-os em uma lista
    No final mostre maior e menor e suas respectivas posições
    '''
    nums = list()
    for v in range(0,5):
        nums.append(int(input("Digite um valor: ")))
    print(nums)
    print(f"Maior número digitado foi {max(nums)}. Foi o {(nums.index(max(nums))) + 1}º a ser digitado.")
    print(f"Menor número digitado foi {min(nums)}. Foi o {(nums.index(min(nums))) + 1}º a ser digitado.")

def ex78Prof():
    listanum = []
    mai = 0
    men = 0
    for c in range(0,5):
        listanum.append(int(input(f"Digite um valor para a posição {c}: ")))
        if c == 0:
            mai = men = listanum[c]
        else:
            if listanum[c] > mai:
                mai = listanum[c]
            if listanum[c] < men:
                men = listanum[c]
    print("=-"*30)
    print(f"Você digitou os valores {listanum}")
    print(f"O maior valor digitado foi {mai} nas posições ", end='')
    for i, v in enumerate(listanum):
        if v == mai:
            print(f"{i}...", end="")
    print()
    print(f"O menor valor digitado foi {men} nas posições ", end="")
    for i, v in enumerate(listanum):
        if v == men:
            print(f"{i}...", end="")

def ex79():
    '''
    Crie um programa onde o usuário pode digitar quantos valores quiser e cadastre em uma lista
    Caso o número já exista na lista, o número não será adicionado
    No final será exibido todos os valores em ordem crescente
    '''
    nums = list()
    while True:
        n = int(input("Digite um valor: "))
        if n not in nums:
            nums.append(n)
            print(f"{n} adicionado.")
        else:
            print(f"{n} já existe. Não foi adicionado.")
        cont = input("Deseja continuar? [S/N] ").upper().strip()
        while cont not in "SN":
            cont = input("Opção inválida. Deseja continuar? [S/N] ").upper().strip()
        if cont == "N":
            break
    nums.sort()
    print("Você digitou ", nums)

def ex79Prof():
    numeros = list()
    while True:
        n = int(input("Digite o valor: "))
        if n not in numeros:
            numeros.append(n)
            print("Valor adicionado...")
        else:
            print("Valor duplicado...")
        r = input("Quer continuar? [S/N] ")
        if r in "Nn":
            break
    print("=-" * 30)
    numeros.sort()
    print(f"Você digitou os valores {numeros}")

def ex80Prof():
    '''
    Crie um programa onde o usuário possa digitar 5 valores numéricos e coloque numa lista, já em ordem crescente sem usar o sort
    No final mostre
    '''
    lista = []
    for c in range(0, 5):
        n = int(input("Digite um valor: "))
        if c == 0 or n > lista[-1]:
            lista.append(n)
            print("Adicionado ao final da lista...")
        else:
            pos = 0
            while pos < len(lista):
                if n <= lista[pos]:
                    lista.insert(pos, n)
                    print(f"Adicionado na posição {pos} da lista...")
                    break
                pos += 1
    print("=-" * 30)
    print(f"Os valores digitados em ordem foram {lista}")
