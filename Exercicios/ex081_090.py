def ex81():
    '''
    Crie um programa que leia vários números
    A) Quantos números foram digitados
    B) A lista de valores em ordem decrescente
    C) Se o valor 5 está na lista
    '''
    nums = list()
    while True:
        nums.append(int(input("Digite um valor: ")))
        cont = input("Deseja continuar? [S/N] ").upper().strip()
        while cont not in "SN":
            cont = input("Opção inválida. Deseja continuar? [S/N] ").upper().strip()
        if cont == "N":
            break

    print(f"{len(nums)} números foram digitados.")
    nums.sort(reverse=True)
    print(f"A lista em ordem decrescente: {nums}")
    if 5 in nums:
        print("O valor 5 está na lista.")
    else:
        print("O valor 5 não está na lista.")

def ex82():
    '''
    Crie um programa que leia vários números
    Depois crie 2 listas que vão conter os pares e ímpares
    Ao final mostre as 3 listas
    '''
    nums = list()
    pares = list()
    impares = list()
    while True:
        nums.append(int(input("Digite um valor: ")))
        cont = input("Deseja continuar? [S/N] ").upper().strip()
        while cont not in "SN":
            cont = input("Opção inválida. Deseja continuar? [S/N] ").upper().strip()
        if cont == "N":
            break
    for n in nums:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    print(f"Completa: {nums}\nPares: {pares}\nÍmpares: {impares}")

def ex83(): #ESQUECI DE USAR LISTA
    '''
    Crie um programa que o usuário digite uma expressão que use parenteses.
    Seu app deverá analisar se a expressão passada está com os parenteses abertos e fechados na ordem correta
    '''
    par = 0
    par2 = 0
    expr = input("Digite uma expressão usando parênteses: ")
    for c, letra in enumerate(expr):
        if letra == "(":
            par += 1
        if letra == ")":
            par2 += 1
    if par != par2:
        print("Expressão inválida.")
    else:
        print("Expressão válida.")

def ex83Prof():
    expr = input("Digite a expressão: ")
    pilha = []
    for simb in expr:
        if simb == "(":
            pilha.append("(")
        elif simb == ")":
            if len(pilha) > 0:
                pilha.pop()
            else:
                pilha.append(")")
                break
    if len(pilha) == 0:
        print("Sua expressão é válida.")
    else:
        print("Sua expressão é inválida.")

def ex84():
    '''
    Faça um programa que leia nome e peso de várias pessoas guardando em lista
    A) Quantas pessoas foram cadastradas
    B) Qual o maior peso e quem são os mais pesados
    C) QUal o menor peso e quem são
    '''
    pessoas = list()
    cont = 0
    maior = menor = 0.0
    while True:
        indiv = [input("Nome: "), float(input("Peso: "))]
        pessoas.append(indiv)
        cont += 1
        continuar = input("Deseja continuar? [S/N] ").upper().strip()
        while continuar not in "SN":
            continuar = input("Opção inválida. Deseja continuar? [S/N] ").upper().strip()
        if continuar == "N":
            break
    print(len(pessoas))

    for c in range(0, len(pessoas)):
        if c == 0:
            maior = menor = pessoas[c][1]
        else:
            if pessoas[c][1] >= maior:
                maior = pessoas[c][1]
            if pessoas[c][1] <= menor:
                menor = pessoas[c][1]

    print("=-" * 30)
    print(f"Ao todo você cadastrou {cont} pessoas.")
    print(f"O maior peso foi {maior:.2f}kg. Peso de ", end="")
    for c in range(0, len(pessoas)):
        if pessoas[c][1] == maior:
            print(pessoas[c][0], end="... ")
    print()
    print(f"O menor peso foi {menor:.2f}kg. Peso de ", end="")
    for c in range(0, len(pessoas)):
        if pessoas[c][1] == menor:
            print(pessoas[c][0], end="... ")

def ex84Prof():
    temp = []
    princ = []
    mai = men = 0
    while True:
        temp.append(input("Nome: "))
        temp.append(float(input("Peso: ")))
        if len(princ) == 0:
            mai = men = temp[1]
        else:
            if temp[1] > mai:
                mai = temp[1]
            if temp[1] < men:
                men = temp[1]
        princ.append(temp[:])
        temp.clear()
        resp = input("Quer continuar? [S/N] ")
        if resp in "Nn":
            break
    print("=-"*30)
    print(f"Ao todo, você cadastrou {len(princ)} pessoas.")
    print(f"O maior peso foi de {mai}Kg. Peso de ", end="")
    for p in princ:
        if p[1] == mai:
            print(f"[{p[0]}] ", end="")
    print()
    print(f"O menor peso foi de {men}Kg. Peso de ", end="")
    for p in princ:
        if p[1] == men:
            print(f"[{p[0]}] ", end="")

def ex85():
    '''
    Crie um programa que o usuário digite 7 valores e cadastre em 1 lista, separando pares e ímpares usando 1 lista
    Mostrar a 1 lista em ordem crescente
    '''
    nums = [[],[]]
    for c in range(1, 8):
        n = int(input(f"Digite o {c}º valor: "))
        if n % 2 == 0:
            nums[0].append(n)
        else:
            nums[1].append(n)
    nums[0].sort()
    nums[1].sort()
    print("Pares: ", nums[0])
    print("Ímpares: ", nums[1])

def ex86Prof():
    '''
    Crie uma matriz 3x3 e preencha com input
    Mostre a matriz formatada
    '''
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for l in range(0, 3):
        for c in range(0, 3):
            matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
    print("=-" * 30)
    for l in range(0, 3):
        for c in range(0, 3):
            print(f"[{matriz[l][c]:^5}]", end="")
        print()
    print("=-" * 30)

    return matriz

def ex87():
    matriz = ex86Prof()

    somaPares = somaTerC = maiSegL = 0
    for l in range(0, 3):
        for c in range(0, 3):
            if matriz[l][c] % 2 == 0:
                somaPares += matriz[l][c]
            if c == 2:
                somaTerC += matriz[l][c]
            if l == 1:
                if matriz[l][c] > maiSegL:
                    maiSegL = matriz[l][c]
    print(f"A soma dos valores pares é {somaPares}.")
    print(f"A soma dos valores da terceira coluna é {somaTerC}.")
    print(f"O maior valor da segunda linha é {maiSegL}.")

def ex88():
    '''
    MEGA SENA
    O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números de 1 a 60 para cada jogo, cadastrando em uma lista composta
    Mostre em ordem crescente
    '''
    from random import randint

    jogos = list()
    temp = list()

    print("-" * 30)
    print(f"{'JOGO NA MEGA SENA':^30}")
    print("-" * 30)
    aux = int(input("Quantos jogos você quer que eu sorteie? "))
    print("-=" * 3, f" SORTEANDO {aux} JOGOS ", "-=" * 3)
    for x in range(1, aux + 1):
        print(f"JOGO {x}: ", end="")
        for y in range(0,6):
            temp.append(randint(1,60))
        jogos.append(temp[:])
        print(jogos[x - 1])
        temp.clear()
    print("-=" * 5, "< BOA SORTE >", "-=" * 5)


def ex88Prof():
    from random import randint
    from time import sleep

    lista = list()
    jogos = list()
    print("-" * 30)
    print("      JOGA NA MEGA SENA")
    print("-" * 30)
    quant = int(input("Quantos jogos você quer que eu sorteie? "))
    tot = 1
    while tot <= quant:
        cont = 0
        while True:
            num = randint(1, 60)
            if num not in lista:
                lista.append(num)
                cont += 1
            if cont >= 6:
                break
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        tot += 1
    print("-=" * 3, f" SORTEANDO {quant} JOGOS ", "-=" * 3)
    for i, l in enumerate(jogos):
        print(f"Jogo {i + 1}: {l}")
        sleep(1)
    print("-=" * 5, "< BOA SORTE >", "-=" * 5)

def ex89():
    '''
    Programa leia nome e 2 notas de vários alunos e guarde em 1 lista
    Mostre a média de cada aluno e pergunta ao usuário se quer mostrar as notas de cada aluno individualmente
    '''
    lista = []
    aluno = ["", 0, 0, 0]
    while True:
        aluno[0] = input("Nome: ")
        aluno[1] = float(input("Nota 1: "))
        aluno[2] = float(input("Nota 2: "))
        aluno[3] = (aluno[1] + aluno[2]) / 2
        lista.append(aluno[:])
        cont = input("Quer continuar? [S/N] ").strip().upper()
        while cont not in "SN":
            cont = input("Opção inválida. Quer continuar? [S/N] ").strip().upper()
        if cont in "N":
            break
    print("-=" * 50)
    print(f"{'No.':<4}{'NOME':<10}{'MÉDIA':>8}")
    print("-" * 40)
    for c, x in enumerate(lista):
        print(f"{c:<4}{lista[c][0]:<10}{lista[c][3]:>8.1f}")
    aux = 0
    while True:
        print("-" * 40)
        aux = int(input("Mostrar notas de qual aluno? (999 interrompe) "))
        if aux == 999:
            break
        if aux <= len(lista) - 1:
            print(f"Notas de {lista[aux][0]} são {lista[aux][1]} e {lista[aux][2]}.")

def ex89Prof():
    ficha = list()
    while True:
        nome = input("Nome: ")
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        media = (nota1 + nota2)/2
        ficha.append([nome, [nota1, nota2], media])
        resp = input("Quer continuar? [S/N] ")
        if resp in "Nn":
            break
    print("-=" * 30)
    print(f"{'No.':<4}{'NOME':<10}{'MÉDIA':>8}")
    print('-' * 26)
    for i, a in enumerate(ficha):
        print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
    while True:
        print('-' * 35)
        opc = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
        if opc == 999:
            print("FINALIZANDO...")
            break
        if opc <= len(ficha) - 1:
            print(f"Notas de {ficha[opc][0]} são {ficha[opc][1]}")
    print("<<< VOLTE SEMPRE >>>")

def ex90():
    '''
    Faça um programa que leia o nome e a média de um aluno, guardando também a situação num dicionário
    Mostre
    '''
    aluno = {"nome": input("Nome: "), "média": float(input("Média: "))}
    if aluno["média"] >= 6:
        aluno["situação"] = "Aprovado"
    elif 4 <= aluno["média"] < 6:
        aluno["situação"] = "Recuperação"
    else:
        aluno["situação"] = "Reprovado"
    print("-=" * 50)
    for k, v in aluno.items():
        print(f"- {k.title()} é {v}")
