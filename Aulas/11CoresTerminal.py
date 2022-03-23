'''
0 none
1 bold
4 underline
7 negative
30 a 37 letra
40 a 47 fundo
'''

def Selec():
    estilo = input("Código de estilo: ")
    cor = input("Código de cor: ")
    fundo = input("Código de fundo: ")
    return Cores(estilo,cor,fundo)

def Cores(estiloId, corId, fundoId):
    return f"\033[{str(estiloId)};{str(corId)};{str(fundoId)}m"

def Aula():
    texto = input("Digite algo:\n")
    print(f"{Selec()}{texto}{Cores(0,0,0)}")
    print(f"{Cores(7,0,47)}{texto}\n{Cores(0,5,0)}{texto}{Selec()}")

frase = 'curso de python'

print(frase[:4])
