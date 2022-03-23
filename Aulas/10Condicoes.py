nome = str(input("Digite nome: "))
if nome == "Gabriel":
    print("Belo nome.")
else:
    print("Nome feio.")
print(f"Bom dia, {nome}.")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2)/2
print(f"A média foi {m}. ", end='')
print("Passou de ano!" if m >= 6 else "Reprovado.")