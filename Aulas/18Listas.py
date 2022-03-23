def p01():
    dados = ['djklajs', 12, 'dsklajda', 'djskdjs', 2,313,31]
    print(dados)
    dedos = dados[:]
    print(dedos)
    didos = []
    didos.append(dedos)
    dedos[0] = 1
    print(didos)
    dodos = [["sj",12],['jks',12]]
    print(dodos[0][1])

def p02():
    teste = list()
    teste.append("Gabriel")
    teste.append(24)
    galera = list()
    galera.append(teste[:])
    teste[0] = "João"
    teste[1] = 3
    galera.append(teste[:])
    teste.clear()
    print(teste)
    print(galera)

p02()