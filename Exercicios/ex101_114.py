def ex101():
    '''
    Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano
     de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto
      NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
    '''
    from datetime import datetime
    def voto(ano=datetime.today().year):
        idade = datetime.today().year - ano
        print(f"Com {idade} anos: VOTO ", end="")
        if idade < 16:
            print("NEGADO.")
        elif 65 > idade > 17:
            print("OBRIGATÓRIO.")
        else:
            print("OPCIONAL.")

    print("-" * 30)
    nasc = int(input("Em que ano você nasceu? "))
    voto(nasc)

def ex102():
    '''
    Crie um programa que tenha uma função fatorial() que receba dois
     parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será
      um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
    '''
    def fatorial(num=1, show=False):
        '''
        -> Calcula o Fatorial de um número.
        :param num: O número a ser calculado
        :param show: Mostrar ou não a conta
        :return: O valor do Fatorial de um número n
        '''
        f = 1
        for c in range(num, 0, -1):
            f *= c
            if show == True:
                print(c, end="")
                if c > 1:
                    print(end=" x ")
                else:
                    print(end=" = ")
        return f

    print("-" * 30)
    print(fatorial(5, True))
    help(fatorial)

def ex103():
    '''
    Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de
     um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
      mesmo que algum dado não tenha sido informado corretamente.
    '''
    def ficha(n="<desconhecido>", g=0):
        print(f"O jogador {n} fez {g} gol(s) no campeonato.")

    nome = input("Nome do jogador: ").strip().title()
    gols = input("Número de Gols: ")
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    if nome == "" or not nome.replace(" ", "").isalpha():
        ficha(g=gols)
    else:
        ficha(nome, gols)
ex103()

def ex104():
    '''
    Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input()
     do Python, só que fazendo a validação para aceitar apenas um valor numérico.
    Ex: n = leiaInt('Digite um n: ')
    '''
    def leiaInt(tex):
        while True:
            res = input(tex)
            if res.isnumeric():
                return int(res)
            print("\033[0;31mERRO! Digite um número inteiro válido.\033[m")
    print("-" * 30)
    n = leiaInt("Digite um número: ")
    print(f"Você digitou o número {n}.")

def ex104Prof():
    def leiaInt(msg):
        ok = False
        valor = 0
        while True:
            n = str(input(msg))
            if n.isnumeric():
                valor = int(n)
                ok = True
            else:
                print("\033[0;31mERRO! Digite um número inteiro válido.\033[m")
            if ok:
                break
        return valor

    n = leiaInt("Digite um número: ")
    print(f"Você acabou de digitar o número {n}.")

def ex105():
    '''
    Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
     e vai retornar um dicionário com as seguintes informações:

    - Quantidade de notas
    - A maior nota
    - A menor nota
    - A média da turma
    - A situação (opcional)

    Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
    '''
    def notas(*n, sit=False):
        """
        -> Analisa notas e situações de vários alunos.
        :param n: uma ou mais notas dos alunos
        :param sit: mostrar ou não a situação
        :return:
        """
        turma = dict()
        turma["total"] = len(n)
        turma["maior"] = max(n)
        turma["menor"] = min(n)
        turma["média"] = sum(n)/len(n)
        if sit == True:
            if turma["média"] >= 8:
                turma["situação"] = "BOA"
            elif 8 > turma["média"] >= 6:
                turma["situação"] = "RAZOÁVEL"
            elif 6 > turma["média"] >= 4:
                turma["situação"] = "ABAIXO DA MÉDIA"
            else:
                turma["situação"] = "RUIM"
        return turma
    resp = notas(0, 0, 8, 10, sit=True)
    print(resp)
    # help(notas)

def ex106():
    '''
    Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando
     e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
      Importante: use cores.
    '''
    from time import sleep

    def cores(estiloId, corId, fundoId):
        return f"\033[{str(estiloId)};{str(corId)};{str(fundoId)}m"

    def ajudaPyHelp():
        print(f"{cores(1, 97, 43)}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("   SISTEMA DE AJUDA PyHELP")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        while True:
            ajuda = input(f"{cores(0, 0, 0)}Função ou Biblioteca > ")
            if ajuda.upper() == "FIM":
                print(f"{cores(1, 97, 41)}~~~~~~~~~~~~~~")
                print(f"   ATÉ LOGO")
                print("~~~~~~~~~~~~~~")
                break
            else:
                print(f"{cores(1, 97, 46)}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "~" * len(ajuda))
                print(f"   Acessando o manual do comando '{ajuda}'")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "~" * len(ajuda))
                sleep(2)
                print(cores(0, 0, 47))
                help(ajuda)
                print(f"{cores(1, 97, 43)}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("   SISTEMA DE AJUDA PyHELP")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    ajudaPyHelp()

def ex106Prof():
    from time import sleep

    c = ("\033[m",
         "\033[0;30;41m",
         "\033[0;30;42m",
         "\033[0;30;43m",
         "\033[0;30;44m")

    def ajuda(com):
        titulo(f"Acessando o manual do comando \"{com}\"", 3)
        print(c[4], end="")
        help(com)
        print(c[0], end="")
        sleep(2)

    def titulo(msg, cor=0):
        tam = len(msg) + 4
        print(c[cor], end="")
        print("~" * tam)
        print(f"  {msg}")
        print("~" * tam)
        print(c[0], end="")
        sleep(1)

    comando = ""
    while True:
        titulo("SISTEMA DE AJUDA PyHELP", 1)
        comando = str(input("Função ou Biblioteca > "))
        if comando.upper() == "FIM":
            break
        else:
            ajuda(comando)
    titulo("ATÉ LOGO!", 2)

def ex107():
    '''
    Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro()
     e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
    '''
    from ex107_108_109_110_111.modulos import moeda

    n = float(input("Digite o preço: R$"))
    porc = 10
    print(f"A metade de R${n:.2f} é R${moeda.metade(n):.2f}")
    print(f"O dobro de R${n:.2f} é R${moeda.dobro(n):.2f}")
    print(f"Aumentando {porc:}%, temos R${moeda.aumentar(n, porc):.2f}")
    print(f"Diminuindo {porc:}%, temos R${moeda.diminuir(n, porc):.2f}")

def ex108():
    '''
    Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga
     mostrar os números como um valor monetário formatado.
    '''
    from ex107_108_109_110_111.modulos import moeda

    n = float(input("Digite o preço: R$"))
    porc = 10
    print(f"A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}")
    print(f"O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}")
    print(f"Aumentando {porc:}%, temos {moeda.moeda(moeda.aumentar(n, porc))}")
    print(f"Diminuindo {porc:}%, temos {moeda.moeda(moeda.diminuir(n, porc))}")

def ex109():
    '''
    Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
     informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
      desenvolvida no desafio 108.
    '''
    from ex107_108_109_110_111.modulos import moeda

    n = float(input("Digite o preço: R$"))
    porc = 10
    print(f"A metade de {moeda.moeda(n)} é {moeda.metade(n, True)}")
    print(f"O dobro de {moeda.moeda(n)} é {moeda.dobro(n, True)}")
    print(f"Aumentando {porc:}%, temos {moeda.aumentar(n, porc, True)}")
    print(f"Diminuindo {porc:}%, temos {moeda.diminuir(n, porc, True)}")

def ex110():
    '''
    Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que
     mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
    '''
    from ex107_108_109_110_111.modulos import moeda

    n = float(input("Digite o preço: R$"))
    aum = int(input("Digite o percentual de aumento: "))
    dec = int(input("Digite o percentual de decréscimo: "))
    moeda.resumo(n, aum, dec)

def ex111():
    '''
    Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
     Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote
      e mantenha tudo funcionando.
    '''
    from ex107_108_109_110_111.modulos import moeda

    ex110()

def ex112():
    '''
    Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função
     chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de
      dados para aceitar apenas valores que seja monetários.
    '''
    from ex107_108_109_110_111.modulos import moeda
    from ex107_108_109_110_111.modulos import dados

    p = dados.leiaDinheiro("Digite o preço: R$")
    moeda.resumo(p, 35, 22)

def ex113():
    '''
    Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação
     de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
    '''
    from ex107_108_109_110_111.modulos import dados

    x = dados.leiaInt("Digite um número inteiro: ")
    y = dados.leiaFloat("Digite um número real: ")
    print(f"O valor inteiro digitado foi {x} e o real foi {str(y).replace('.',',')}")

def ex114():
    '''
    Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
    '''
    import urllib
    import urllib.request

    try:
        site = urllib.request.urlopen("http://www.pudim.com.br")
    except urllib.error.URLError as erro:
        print(erro.__class__)
        print("DEU ERRO")
    else:
        print("OK")
        print(site.read())
