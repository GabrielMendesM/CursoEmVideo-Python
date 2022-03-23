def ex91():
    '''
    crie um programa onde 4 jogadores tem um dado. Guarde num dicionário. No final mostre em ordem,
    o vencedor é quem tirou o maior número
    '''
    from random import randint

    jogador = dict()
    print("Valores sorteados:")
    for x in range(1,5):
        jogador[f"Jogador{x}"] = randint(1,6)
    for k, v in jogador.items():
        print(f"{k} tirou {v} no dado.")
    print("-=" * 30)
    print("  == RANKING DOS JOGADORES ==")
    for c, k in enumerate(sorted(jogador, key=jogador.get, reverse=True)):
        print(f"   {c + 1}º lugar: {k} com {jogador[k]}")

def ex91Prof():
    from random import randint
    from time import sleep
    from operator import itemgetter

    jogo = {"jogador1": randint(1,6),
            "jogador2": randint(1,6),
            "jogador3": randint(1,6),
            "jogador4": randint(1,6)}
    ranking = dict()
    print("Valores sorteados:")
    for k, v in jogo.items():
        print(f"{k} tirou {v} no dado.")
        sleep(1)
    ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
    print("-=" * 30)
    print("  == RANKING DOS JOGADORES ==")
    for i, v in enumerate(ranking):
        print(f"   {i + 1}º lugar: {v[0]} com {v[1]}")

def ex92():
    '''
    Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
     em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano
     de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
    '''
    from datetime import date
    pessoa = dict()
    pessoa["nome"] = input("Nome: ")
    ano = int(input("Ano de nascimento: "))
    pessoa["idade"] = date.today().year - ano
    pessoa["ctps"] = int(input("Carteira de trabalho (0 não tem): "))
    if pessoa["ctps"] != 0:
        pessoa["contratação"] = int(input("Ano de contratação: "))
        pessoa["salário"] = float(input("Salário: "))
        pessoa["aposentadoria"] = (pessoa["contratação"] + 35) - ano
    print("-=" * 30)
    for k, v in pessoa.items():
        print(f" - {k} tem o valor {v}.")

def ex93():
    '''
    Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do
    jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
    No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
    '''
    jogador = dict()
    jogador["nome"] = input("Nome do jogador: ").strip().title()
    partidas = int(input(f"Partidas de {jogador['nome']}: "))
    gol = []
    for x in range(1, partidas + 1):
        gol.append(int(input(f"   Gols na {x}ª partida: ")))
    jogador["gols"] = gol[:]
    jogador["total"] = sum(gol)
    print("-=" * 30)
    print(jogador)
    print("-=" * 30)
    for k, v in jogador.items():
        print(f"O campo {k} tem o valor {v}.")
    print("-=" * 30)
    print(f"O jogador {jogador['nome']} jogou {partidas} partidas.")
    for i, v in enumerate(jogador["gols"]):
        print(f"   => Na {i + 1}ª partida, fez {v} gols.")
    print(f"Foi um total de {jogador['total']} gols.")

def ex94():
    '''
    Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados
    de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
    A) Quantas pessoas foram cadastradas
    B) A média de idade
    C) Uma lista com as mulheres
    D) Uma lista de pessoas com idade acima da média
    '''
    pessoa = dict()
    lista = list()
    while True:
        pessoa["nome"] = input("Nome: ").strip().title()
        pessoa["sexo"] = input("Sexo: [F/M] ").upper().strip()
        while pessoa["sexo"] not in "FM":
            pessoa["sexo"] = input("Opção inválida. Sexo: [F/M] ").upper().strip()
        pessoa["idade"] = int(input("Idade: "))
        lista.append(pessoa.copy())
        cont = input("Continuar? [S/N] ").upper().strip()
        while cont not in "SN":
            cont = input("Opção inválida. Continuar? [S/N] ").upper().strip()
        if cont == "N":
            break
    print("-=" * 30)
    print(f"{len(lista)} pessoas foram cadastradas.")
    soma = 0
    media = 0
    for c, x in enumerate(lista):
        soma += x["idade"]
        media = soma/(c+1)
    print(f"A média entre as idades é {media:.2f}")
    mulheres = []
    for x in lista:
        if x["sexo"] == "F":
            mulheres.append(x["nome"])
    print(f"As mulheres são {mulheres}")
    maior = []
    for x in lista:
        if x["idade"] > media:
            maior.append(x["nome"])
    print(f"As pessoas com idade maior que a média são {maior}")

def ex94Prof():
    pessoa = dict()
    galera = list()
    soma = media = 0
    while True:
        pessoa.clear()
        pessoa["nome"] = input("Nome: ")
        while True:
            pessoa["sexo"] = input("Sexo: [M/F] ").upper()[0]
            if pessoa["sexo"] in "MF":
                break
            print("ERRO! Por favor, digite apenas M ou F.")
        pessoa["idade"] = int(input("Idade: "))
        soma += pessoa["idade"]
        galera.append(pessoa.copy())
        while True:
            resp = input("Quer continuar? [S/N] ").upper()[0]
            if resp in "SN":
                break
            print("ERRO! Responda S ou N.")
        if resp == "N":
            break
    print("-=" * 30)
    print(f"A) Ao todo temos {len(galera)} pessoas cadastradas.")
    media = soma / len(galera)
    print(f"B) A média de idade é de {media:5.2f} anos.")
    print("C) As mulheres cadastradas foram ", end="")
    for p in galera:
        if p["sexo"] in "Ff":
            print(f"{p['nome']} ", end="")
    print()
    print("D) Lista das pessoas que estão acima da média: ")
    for p in galera:
        if p["idade"] >= media:
            print("    ", end="")
            for k, v in p.items():
                print(f"{k} = {v}; ", end="")
            print()
    print("<< ENCERRADO >>")

def ex95():
    '''
    Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
    visualização de detalhes do aproveitamento de cada jogador.
    '''
    jogador = dict()
    lista = list()
    while True:
        jogador["nome"] = input("Nome do jogador: ").strip().title()
        partidas = int(input(f"Partidas de {jogador['nome']}: "))
        gol = []
        for x in range(1, partidas + 1):
            gol.append(int(input(f"   Gols na {x}ª partida: ")))
        jogador["gols"] = gol[:]
        jogador["total"] = sum(gol)
        lista.append(jogador.copy())
        while True:
            resp = input("Quer continuar? [S/N] ").upper()[0]
            if resp in "SN":
                break
            print("ERRO! Responda S ou N.")
        if resp == "N":
            break
    print("-=" * 30)
    print(f"{'cod':<4}", end="")
    for i in jogador.keys():
        print(f"{str(i).upper():<20}", end="")
    print()
    print("-" * 50)
    for i, a in enumerate(lista):
        print(f"{i:>3}", end=" ")
        for v in a.values():
            print(f"{str(v):<20}", end="")
        print()
    print("-" * 50)
    dados = 0
    while True:
        dados = int(input("Mostrar dados de qual jogador? (999 para parar) "))
        if dados == 999:
            break
        elif dados <= len(lista) - 1:
            print(f" -- LEVANTAMENTO DO JOGADOR {lista[dados]['nome'].upper()}:")
            for i, v in enumerate(lista[dados]["gols"]):
                print(f"   => Na {i + 1}ª partida, fez {v} gols.")
        else:
            print(f"ERRO! Não existe jogador com código {dados}.")
        print("-" * 50)
    print("<< VOLTE SEMPRE >>")

ex95()

def ex96():
    '''
    Faça um programa que tenha uma função chamada área(),
     que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
    '''
    def area(largura, comprimento):
        res = largura * comprimento
        print(f"A área de um terreno {largura:.1f}x{comprimento:.1f} é de {res}m².")
    print(" Controle de Terrenos ")
    print('-' * 20)
    lar = float(input("LARGURA (m): "))
    com = float(input("COMPRIMENTO (m): "))
    area(lar, com)

def ex97():
    '''
   Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
    como parâmetro e mostre uma mensagem com tamanho adaptável.

    Ex:
    escreva('Olá, Mundo!')
    Saída:
    ~~~~~~~~~
     Olá, Mundo!
    ~~~~~~~~~
    '''
    def escreva(tex):
        tam = len(tex) + 4
        print("~" * tam)
        print(f"  {tex}")
        print("~" * tam)
    escreva("Olá Mundo!")
    escreva("Não vou mais te perdoar, você foi longe demais.")
    escreva("1.2.3")

def ex98():
    '''
    Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
     fim e passo. Seu programa tem que realizar três contagens através da função criada:

    a) de 1 até 10, de 1 em 1
    b) de 10 até 0, de 2 em 2
    c) uma contagem personalizada
    '''
    from time import sleep

    def contador(inicio, fim, passo):
        print("-=" * 30)
        if passo < 0:
            passo *= -1
        print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
        sleep(1)
        if fim <= inicio:
            for x in range(inicio, fim - 1, -passo):
                print(x, end=" ")
                sleep(0.3)
        else:
            for x in range(inicio, fim + 1, passo):
                print(x, end=" ")
                sleep(0.3)
        print("FIM!")
    contador(1, 10, 1)
    contador(10, 0, 2)
    print("-=" * 30)
    print("Agora é sua vez de personalizar a contagem!")
    ini = int(input("Início: "))
    fi = int(input("Fim: "))
    pas = int(input("Passo: "))
    contador(ini, fi, pas)

def ex98Prof():
    from time import sleep

    def contador(i, f, p):
        print("-=" * 20)
        cont = i
        if p < 0:
            p *= -1
        if p == 0:
            p = 1
        print(f"Contagem de {i} até {f} de {p} em {p}")
        sleep(2)
        if i < f:
            while cont <= f:
                print(f"{cont} ", end="", flush=True)
                sleep(0.5)
                cont += p
        else:
            while cont >= f:
                print(f"{cont} ", end="", flush=True)
                sleep(0.5)
                cont -= p
        print("FIM!")
        sleep(0.5)
    contador(1, 10, 1)
    contador(10, 0, 2)
    print("-=" * 20)
    print("Agora é sua vez de personalizar a contagem!")
    ini = int(input("Início: "))
    fim = int(input("Fim:    "))
    pas = int(input("Passo:  "))
    contador(ini, fim, pas)

def ex99():
    '''
    Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com
     valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
    '''
    from time import sleep

    def maior(*num):
        mai = 0
        print("-=" * 30)
        print("Analisando os valores passados...")
        sleep(1)
        for c, n in enumerate(num):
            print(n, end=" ")
            sleep(0.3)
            if c == 0:
                mai = n
            else:
                if n > num[c - 1]:
                    mai = n
        sleep(0.5)
        print(f"Foram informados {len(num)} valores ao todo.")
        sleep(0.5)
        print(f"O maior valor informado foi {mai}.")
        sleep(0.5)
    maior(2, 9, 4, 5, 7, 1)
    maior(4, 7, 0)
    maior(1, 2)
    maior(6)
    maior()

def ex100():
    '''
    Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e
     somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a
      segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
    '''
    from random import randint

    def sorteia():
        lista = []
        print("Sorteando 5 valores da lista: ", end="")
        for x in range(0, 5):
            lista.append(randint(0, 10))
            print(lista[x], end=" ")
        print("PRONTO!")
        return lista

    def somaPar(lst):
        s = 0
        for n in lst:
            if n % 2 == 0:
                s += n
        print(f"Somando os valores pares de {lst}, temos {s}")
    somaPar(sorteia())

def ex100Prof():
    from random import randint
    from time import sleep

    def sorteia(lista):
        print("Sorteando 5 valores da lista: ", end="")
        for cont in range(0, 5):
            n = randint(1,10)
            lista.append(n)
            print(f"{n} ", end="", flush=True)
            sleep(0.3)
        print("PRONTO!")

    def somaPar(lista):
        soma = 0
        for valor in lista:
            if valor % 2 == 0:
                soma += valor
        print(f"Somando os valores pares de {lista}, temos {soma}")

    numeros = list()
    sorteia(numeros)
    somaPar(numeros)
    
ex100Prof()