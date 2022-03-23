def moeda(n, moeda="R$"):
    return f"{moeda}{n:.2f}".replace(".", ",")

def metade(n=0, formato=False):
    res = n / 2
    return res if not formato else moeda(res)

def dobro(n=0, formato=False):
    res = n * 2
    return res if not formato else moeda(res)

def aumentar(n=0, porc=0, formato=False):
    res = n + (n * porc / 100)
    return res if not formato else moeda(res)

def diminuir(n=0, porc=0, formato=False):
    res = n - (n * porc / 100)
    return res if not formato else moeda(res)

def resumo(preco=0, aum=0, dim=0, formato=True):
    print("-" * 30)
    print("RESUMO DO VALOR".center(30))
    print("-" * 30)
    print(f"Preço analisado:   \t{moeda(preco)}")
    print(f"Dobro do preço:    \t{dobro(preco, formato)}")
    print(f"Metade do preço:   \t{metade(preco, formato)}")
    print(f"{aum:}% de aumento:  \t{aumentar(preco, aum, formato)}")
    print(f"{dim}% de redução:   \t{diminuir(preco, dim, formato)}")
    print("_" * 30)