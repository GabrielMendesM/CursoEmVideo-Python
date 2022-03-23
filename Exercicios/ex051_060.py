def ex51():
    prim = int(input("Digite o primeiro termo: "))
    raz = int(input("Digite a razão: "))
    prog = [prim]
    res = ''
    for x in range(0, 10):
        prog.append(prog[x] + raz)
        if x != 0:
            res += ',' + str(prog[x])
    print(f"PA[10] = {prim}{res}.")

def ex51Prof():
    primeiro = int(input("Primeiro termo: "))
    razao = int(input("Razão: "))
    decimo = primeiro + (10 - 1) * razao
    for c in range(primeiro, decimo + razao, razao):
        print(c, end=' → ')
    print("ACABOU.")

def ex52():
    n = int(input("Digite o número: "))
    prim = ''
    for x in range(1,n + 1):
        if n % x == 0 and x != 1 and x != n:
            prim = "Não é primo."
            break
        else:
            prim = "É primo."
    print(prim)

def ex52Prof():
    num = int(input("Digite um número: "))
    tot = 0
    for c in range(1,num + 1):
        if num % c == 0:
            print("\033[34m", end='')
            tot += 1
        else:
            print("\033[31m", end='')
        print(f"{c} ", end='')
    print(f"\n\033[mO número {num} foi divisível {tot} vezes.")
    if tot == 2:
        print("E por isso ele é PRIMO.")
    else:
        print("E por isso ele não é PRIMO.")

def ex53():
    x = input("Digite uma frase: ").strip().split()
    x = ''.join(x)
    z = ''
    print(x)
    for y in range(len(x) - 1, -1,-1):
        z += x[y]
    print(z)
    if z == x:
        print("É palíndromo.")
    else:
        print("Não é palíndromo.")

def ex53Prof():
    frase = input("Digite uma fase: ").strip().upper()
    palavras = frase.split()
    junto = ''.join(palavras)
    inverso = junto[::-1]
    print(f"O inverso de {junto} é {inverso}.")
    if inverso == junto:
        print("É palíndromo.")
    else:
        print("Não é palíndromo.")

def ex54():
    from datetime import date
    x = []
    idade = 0
    maior = 0
    for y in range(0,7):
        x.append(date(int(input("Digite seu ano de nascimento: ")),int(input("Digite o mês: ")), int(input("Digite o dia: "))))
        if x[y].month <= date.today().month and x[y].day <= date.today().day:
            idade = date.today().year - x[y].year
        else:
            idade = date.today().year - x[y].year - 1
        if idade >= 18: maior += 1
    print(f"{maior} são maiores de idade.")

def ex54Prof():
    from datetime import date
    atual = date.today().year
    totmaior = 0
    totmenor = 0
    for pess in range(1,8):
        nasc = int(input(f"Em que ano a pessoa {pess} nasceu? "))
        idade = atual - nasc
        if idade >= 18:
            totmaior += 1
        else:
            totmenor += 1
    print(f"Ao todo tivemos {totmaior} pessoas maiores de idade.")
    print(f"E também tivemos {totmenor} pessoas menores de idade.")

def ex55():
    maior = 0
    menor = 1000000000
    for x in range(0,5):
        y = int(input("Digite o peso: "))
        if y > maior:
            maior = y
        elif y < menor:
            menor = y
    print(f"O mais pesado é {maior}kg e o menor é {menor}kg.")

def ex55Prof():
    maior = 0
    menor = 0
    for p in range(1,6):
        peso = float(input(f"Digite o peso da pessoa {p}: "))
        if p == 1:
            maior = peso
            menor = peso
        else:
            if peso > maior:
                maior = peso
            if peso < menor:
                menor = peso
    print(f"O maior peso lido foi de {maior:.2f}Kg.")
    print(f"O menor peso lido foi de {menor:.2f}Kg.")

def ex56():
    nome = ''
    idade = 0
    sexo = ''
    mediaIdade = 0
    velho = 0
    homemVelho = ''
    mulheresMenos = 0

    for x in range(0,4):
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        sexo = input("Digite F para feminino ou M para masculino: ").upper()
        mediaIdade += idade
        if sexo == 'F' and idade < 20:
            mulheresMenos += 1
        if sexo == 'M':
            if idade > velho:
                velho = idade
                homemVelho = nome
    print(f"A média das idades é igual a {mediaIdade/4:.0f}")
    if velho > 0:
        print(f"O nome do homem mais velho é {homemVelho}")
    else:
        print(f"Não há homens.")
    if mulheresMenos > 0:
        print(f"{mulheresMenos} mulheres têm menos de 20 anos.")
    else:
        print(f"Não há mulheres com menos de 20 anos.")

def ex56Prof():
    somaidade = 0
    mediaidade = 0
    maioridadehomem = 0
    nomevelho = 0
    totmulher20 = 0
    for p in range(1,5):
        print(f"----- {p}ª PESSOA -----")
        nome = input("Nome: ").strip()
        idade = int(input("Idade: "))
        sexo = input("Sexo (M/F): ")
        somaidade += idade
        if p == 1 and sexo in "Mm":
            maioridadehomem = idade
            nomevelho = nome
        if sexo in "Mm" and idade > maioridadehomem:
            maioridadehomem = idade
            nomevelho = nome
        if sexo in "Ff" and idade < 20:
            totmulher20 += 1
    mediaidade = somaidade/4
    print(f"A média de idade do grupo é igual a {mediaidade}.")
    print(f"O homem mais velho tem {maioridadehomem} e se chama {nomevelho}.")
    print(f"Ao todo são {totmulher20} mulheres com menos de 20 anos.")

def ex57():
    x = ""
    while x != "M" and x != "F":
        x = input("Digite M ou F: ").upper()
    print("FOI")

def ex57Prof():
    sexo = str(input("Informe o seu sexo: [M/F] ")).strip().upper()[0]
    while sexo not in 'MmFf':
        sexo = str(input("Dados inválidos. Por favor, informe seu sexo: [M/F]")).strip().upper()
    print(f"Sexo {sexo} registrado com sucesso.")

def ex58():
    from random import randint
    import time

    ganhou = False
    while not ganhou:
        print("-=-" * 5 + " PROCESSANDO " + "-=-" * 5)
        ia = randint(0, 5)
        n = int(input("Chute um número de 0 a 5: "))
        time.sleep(3)
        print(f"O número sorteado foi {ia}. ", end='')
        if ia == n:
            print("Parabéns você acertou!")
            ganhou = True
        else:
            print("Você errou, tente de novo.")

def ex58Prof():
    from random import randint
    computador = randint(0,10)
    print("Adivinhe o número de 0 a 10.")
    acertou = False
    palpites = 0
    while not acertou:
        jogador = int(input("Digite o seu palpite: "))
        palpites += 1
        if jogador == computador:
            acertou = True
        else:
            if jogador < computador:
                print("Mais... Tente novamente.")
            elif jogador > computador:
                print("Menos... Tente novamente.")
    print(f"Acertou com {palpites} tentativas. Parabéns.")

def ex59():
    sair = False
    while sair == False:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        oper = int(input("Digite o código da operação:\n[1] somar\n[2]multiplicar\n[3]mostrar o maior\n[4]começar de novo\n[5]sair\n"))
        if oper == 1:
            print(f"{n1} + {n2} = {n1 + n2}")
        if oper == 2:
            print(f"{n1} x {n2} = {n1 * n2}")
        if oper == 3:
            if n1 > n2:
                n3 = str(n1)
            elif n2 > n1:
                n3 = str(n2)
            else:
                n3 = "São iguais"
            print(f"{n3} é o maior entre {n1} e {n2}")
        if oper == 4:
            pass
        if oper == 5:
            sair = True

def ex59Prof():
    n1 = int(input("Primeiro valor: "))
    n2 = int(input("Segundo valor: "))
    opcao = 0
    while opcao != 5:
        print("[1] somar\n[2] multiplicar\n[3] mostrar o maior\n[4] começar de novo\n[5] sair")
        opcao = int(input(">>>>> Qual a sua opção? "))
        if opcao == 1:
            soma = n1 + n2
            print(f"A soma entre {n1} + {n2} é {soma}")
        elif opcao == 2:
            produto = n1 * n2
            print(f"A multiplicação de {n1} x {n2} é {produto}")
        elif opcao == 3:
            if n1 > n2:
                maior = n1
            else:
                maior = n2
            print(f"Entre {n1} e {n2}, o maior valor é {maior}")
        elif opcao == 4:
            print("Informe os números novamente.")
            n1 = int(input("Primeiro valor: "))
            n2 = int(input("Segundo valor: "))
        elif opcao == 5:
            print("Finalizando...")
        else:
            print("Opção inválida. Tente novamente.")
        print("=-=" * 10)
    print("Fim do programa!")

def ex60():
    x = int(input("Digite um número: "))
    y = x
    print(f"{x}! = ", end='')
    while x > 1:
        print(f"{x}*",end='')
        x -= 1
        y *= x
    print(f"1 = {y}")

def ex60Prof():
    n = int(input("Digite um número para calcular seu fatorial: "))
    c = n
    f = 1
    print(f"Calculando {n}! = ", end='')
    while c > 0:
        print(f"{c}", end='')
        print(" x " if c > 1 else " = ", end='')
        f *= c
        c -= 1
    print(f"{f}")
