from random import randint

esc = int(input("Digite 1 para Pedra, 2 para Papel ou 3 para Tesoura: "))
adv = randint(1,3)
print(esc, adv)

while esc == adv:
    print(f"Jogador escolheu {esc} e Adversário escolheu {adv}")