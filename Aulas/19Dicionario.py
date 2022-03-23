pessoas = {"Nome": "Gabriel", "Sexo": "M", "Idade": 24}

def p01():
    print(f"O {pessoas['Nome']} tem {pessoas['Idade']} anos.")
    print(pessoas.keys())
    print(pessoas.values())
    print(pessoas.items())

def p02():
    for k, v in pessoas.items():
        print(k, v)
        print()
    del pessoas["Sexo"]
    pessoas["Nome"] = "João"
    pessoas["Peso"] = 5.0
    for k, v in pessoas.items():
        print(k, v)

brasil = []
estado1 = {"UF": "Rio de Janeiro", "Sigla": "RJ"}
estado2 = {"UF": "São Paulo", "Sigla": "SP"}

def p03():
    brasil.append(estado1)
    brasil.append(estado2)

    print(brasil)
    print(brasil[0]["UF"])
    print(brasil[1]["Sigla"])

estado = dict()

def p04():
    for c in range(0,3):
        estado["UF"] = input("Unidade Federativa: ").title().strip()
        estado["Sigla"] = input("Sigla: ").upper().strip()
        brasil.append(estado.copy())
    for c, x in enumerate(brasil):
        print(brasil[c]["Sigla"])
    for e in brasil:
        for k, v in e.items():
            print(f"O campo {k} tem valor {v}.")
        for v in e.values():
            print(v, end= " ")
        print()
p04()
