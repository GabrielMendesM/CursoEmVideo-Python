nome = input("Qual o seu nome? ")
if nome == "Gabriel":
    print("Belo nome. ")
elif nome == "Cadu" or nome == "Gustavo":
    print("Nome popular. ")
elif nome in "Carol Bia Werk João":
    print("3")
else:
    print("Nome feio. ")
print(f"Tenha um bom dia, {nome}!")