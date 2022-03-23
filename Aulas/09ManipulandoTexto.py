frase = "Frase de exemplo com 34 caracteres"
frase2 = "   Frase strip   "

def Fatiamento():
    print(f"{frase[4]}\n{frase[3:12]}\n{frase[:8]}\n{frase[12:]}\n{frase[4::2]}")

def Analise():
    print(f"{len(frase)}\n{frase.count('o')}\n{frase.count('e',6,18)}\n{frase.find('34')}\n{frase.find('Não existe')}\n{'N existe' in frase}")

def Transformacao():
    print(f"{frase.replace('Frase', 'Trocado')}\n{frase.upper()}\n{frase.capitalize()}\n{frase.title()}")
    print(f"{frase2.strip()}\n{frase2.rstrip()}\n{frase2.lstrip()}")

def Divisao_Join():
    print(f"{frase.split()}")
    print(f"{'-'.join(frase)}")

def _Aula09():
    #Outra forma de escrever em várias linhas
    print("""dnaiosdjasidj
sadoijsadioj
asdoiajsdiohasd
    asdoiahsdkashd
asdioahsdahduasd
asodhasudh""")
    frase3 = "dhaiosdh dhasdh dajsdioaj"
    print(frase3)
    print(frase.upper().count("E"))
    print(len(frase.strip()))
    frase3 = frase3.title()
    print(frase3)
    print("exemplo" in frase)
    print(f"{frase.find('34')}\n{frase.find('suadjksa')}")
    frase3 = frase3.split()
    print(f"{frase3[1]}\n{frase3[1][0]}")

_Aula09()
