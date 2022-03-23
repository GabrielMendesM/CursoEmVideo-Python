def leiaDinheiro(txt):
    aux = True
    n = 0
    while aux:
        n = input(txt).strip()
        if n.isnumeric():
            n = float(n)
            aux = False
        else:
            for l in n:
                if l in "." or l in ",":
                    if n.replace(".", "").replace(",", "").isnumeric():
                        n = n.replace(",", ".")
                        n = float(n)
                        aux = False
        if type(n) != float:
            print(f'{cores(0,31,47)}ERRO! "{n}" é um preço inválido!{cores()}')
    return n

def leiaInt(tex):
    while True:
        try:
            return int(input(tex))
        except:
            print("\033[0;31mERRO! Digite um número inteiro válido.\033[m")

def leiaFloat(tex):
    while True:
        try:
            n = float(input(tex).replace(",","."))
        except (TypeError, ValueError):
            print("\033[0;31mERRO! Digite um número inteiro válido.\033[m")
            continue
        except(KeyboardInterrupt):
            print("Entrada de dados interrompida pelo usuário")
            break
        else:
            return n

def cores(estiloId=0, corId=0, fundoId=0):
    return f"\033[{str(estiloId)};{str(corId)};{str(fundoId)}m"
