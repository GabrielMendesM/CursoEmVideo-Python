from ex115.lib.interface import *
from ex115.lib.entrada import *
from ex115.lib.arquivo import *
from time import sleep

arq = "exercicio.txt"
apagarDado(arq, "gabriel")
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    opcoes = ["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do Sistema"]
    resposta = menu(opcoes)
    if resposta == 1:
        lerArquivo(arq)
        sleep(1)
        input(f"\n{cores(letra=35)}PRESSIONE ENTER PARA CONTINUAR{cores()}")

    elif resposta == 2:
        cabecalho("NOVO CADASTRO", cor=cores(1,32))
        nome = leiaNome("Nome: ")
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)
        input(f"\n{cores(letra=35)}PRESSIONE ENTER PARA CONTINUAR{cores()}")

    elif resposta == 3:
        cabecalho("Saindo...", cor=cores(1,32))
        sleep(2)
        break
    else:
        print(f"{cores(letra=31)}ERRO! DIGITE UMA OPÇÂO VÁLIDA{cores()}")
        sleep(1)
