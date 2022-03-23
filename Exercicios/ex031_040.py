def ex31():
    dist = int(input("Digite distância da viagem (Km): "))
    preco = dist * 0.5 if dist <= 200 else dist * 0.45
    print("A viagem vai custar R${:.2f}" .format(preco))

def ex32():
    ano = int(input("Digite um ano: "))
    x = ano % 4
    y = ano % 400
    z = ano % 100
    sim = f"O ano de {ano} é bissexto."
    nao = f"O ano de {ano} não é bissexto."
    if x == 0:
        if z == 0:
            print(nao)
        else:
            print(sim)
    else:
        if y == 0:
            print(sim)
        else:
            print(nao)

def ex32Prof():
    import datetime
    ano = int(input("Digite um ano (0 para ano atual): "))
    if ano == 0:
        ano = datetime.date.today().year
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")

def ex33():
    x = int(input("Digite um número: "))
    y = int(input("Digite um número: "))
    z = int(input("Digite um número: "))
    if x > y and x > z:
        print(f"{x} é o maior número. E ", end='')
    elif y > x and y > z:
        print(f"{y} é o maior número. E ", end='')
    elif z > x and z > y:
        print(f"{z} é o maior número. E ", end='')
    if x < y and x < z:
        print(f"{x} é o menor.")
    elif y < x and y < z:
        print(f"{y} é o menor.")
    if z < x and z < y:
        print(f"{z} é o menor.")

def ex34():
    x = float(input("Digite o salário: "))
    if x >= 1250:
        print(f"Ganhou 10% de aumento, o salário agora é R${x + x * 0.1:.2f}")
    else:
        print(f"Ganhou 15% de aumento, o salário agora é R${x + x * 0.15:.2f}")

def ex35():
    x = float(input("Digite o comprimento da reta 1: "))
    y = float(input("Digite o comprimento da reta 2: "))
    z = float(input("Digite o comprimento da reta 3: "))
    if x + y > z and x + z > y and y + z > x:
        print("Formou um triângulo.",end='')
    else:
        print("Não formou um triângulo.")

def ex36():
    n = float(input("Digite o valor da casa: "))
    sal = float(input("Digite o valor do salário: "))
    ano = int(input("Digite quantos anos pagar: "))
    pres = n/(ano*12)
    if pres <= sal * 0.3:
        print("Você pagará R${:.2f} por mês." .format(pres))
    else:
        print("Mais de 30%.")

def ex37():
    x = int(input("Digite um número inteiro: "))
    y = int(input("Escolha base de conversão (1-binário, 2-octal, 3-hexadecimal): "))
    print(f"O valor decimal de {x}, ",end='')
    if y == 1:
        print(f"em binário, é ",end='')
        z = bin(x)
    elif y == 2:
        print(f"em octal, é ",end='')
        z = oct(x)
    elif y == 3:
        print(f"em hexadecimal, é ",end='')
        z = hex(x)
    print(z,".")

def ex38():
    x = int(input("Número inteiro 1: "))
    y = int(input("Número inteiro 2: "))
    if x > y:
        print(f"{x} é maior que {y}.")
    elif x < y:
        print(f"{y} é maior que {x}.")
    else:
        print(f"{x} e {y} são iguais.")

def ex39():
    import datetime

    x = int(input("Digite o ano de nascimento: "))
    y = datetime.date.today().year - x
    if y < 18:
        print(f"Falta(m) {18 - y} ano(s) para o alistamento.")
    elif y == 18:
        print("Precisa se alistar esse ano.")
    else:
        print(f"Sua data de alistamento foi há {y - 18} ano(s).")

def ex40():
    x =  float(input("Digite a primeira nota: "))
    y = float(input("Digite a segunda nota: "))
    m = (x+y)/2
    print("Média foi {:.2f}. ".format(m),end='')
    if m < 4:
        print(f"Reprovado.")
    elif m >= 4 and m < 6:
        print(f"Recuperação.")
    else:
        print(f"Aprovado.")
