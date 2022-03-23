def ex21():
    import pygame
    pygame.init()
    print("init")
    pygame.mixer.music.load('ex021.mp3')
    print("Music.load")
    pygame.mixer.music.play()
    print("music play")
    pygame.event.wait()
    print("wait")

def ex22():
    var = input("Digite um nome completo: ")
    print(f"Maiúsculas: {var.upper()}\nMinúsculas: {var.lower()}")
    var = var.split()
    print(f"Nº de letras: {len(''.join(var))}\nNº de letras do 1º nome: {len(var[0])}")

def ex22Prof():
    nome = input("Digite um nome: ").strip()
    print(f"Maiúscula: {nome.upper()}\nMinúsculas: {nome.lower()}\n"
          f"Total letras: {len(nome) - nome.count(' ')}\nLetras 1º nome: {nome.find(' ')}")

def ex23():
    var = input("Digite um número de 0 a 9999: ")
    print("Unidade: {3}\nDezena: {2}\nCentena: {1}\nMilhar: {0}" .format(var[0],var[1],var[2],var[3]))

def ex23Prof():
    num = int(input("Informe um número: "))
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10
    print(f"Unidade: {u}\nDezena: {d}\nCentena: {c}\nMilhar: {m}")

def ex24():
    var = input("Digite o nome de uma cidade: ").upper().split()
    var[0] = var[0].find("SANTO")
    if var[0] == 0:
        print("Começa com SANTO.")
    elif var[0] == -1:
        print("Não começa com SANTO.")

def ex24Prof():
    cid = input("Nome da cidade: ").strip()
    print(cid[:5].upper() == "SANTO")

def ex25():
    nome = input(f"Digite o nome a ser procurado: ").strip().capitalize()
    nao = f"Não tem {nome} no nome."
    aux = True

    while aux:
        var = input("Digite nome completo: ").title().split()

        for i, j in enumerate(var):
            if var[i].find(nome) == 0:
                if j == nome:
                    print(f"Tem {j} no nome.")
                    aux = False
                    return
        print(nao)

def ex25Prof():
    nome = input("Qual é seu nome completo? ").strip()
    print(f"Seu nome tem Silva? {'silva' in nome.lower()}")

def ex26():
    var = input("Digite uma frase: ").strip()
    print(f'Tem {var.count("A")} "A" na frase.')
    print(f'O primeiro "A" é o caractere nº {var.find("A")}.')
    print(f'O último "A" é o caractere nº {var.rfind("A")}')

def ex26Prof():
    frase = input("Digite uma frase: ").upper().strip()
    print(f"A aparece {frase.count('A')}\nA primeira vez que A aparece é {frase.find('A') + 1}\nA última vez que A aparece é {frase.rfind('A')+1}")

def ex27():
    var = input("Digite nome completo: ").strip().split()
    print(f"Primeiro nome: {var[0]}\nÚltimo nome: {var[len(var) - 1]}")

def ex28():
    from random import randint
    import time
    x = 1
    while x > 0:
        ia = randint(0, 5)
        print("-=-" * 5 + " PROCESSANDO " + "-=-" * 5)
        time.sleep(3)
        n = int(input("Chute um número de 0 a 5: "))
        print(f"O número sorteado foi {ia}. ", end='')
        if ia == n:
            print("Parabéns você acertou!")
        else:
            print("Você errou, tente de novo.")
        x = int(input("Aperte 1 para tentar de novo ou 0 para sair: "))

def ex29():
    x = int(input("Digite a velocidade do carro: "))
    y = x - 80
    if x > 80:
        print(f"Está muito rápido, sua multa é de R${7 * y}.")
    else:
        print("Sem multa.")

def ex30():
    x = int(input("Digite um número: "))
    y = x % 2
    if y == 0:
        print(f"{x} é par.")
    else:
        print(f"{x} é ímpar.")
