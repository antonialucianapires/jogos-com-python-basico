print("##################################")
print("Bem vinde ao jogo de Adivinhação! 🚀")
print("##################################")

numero_secreto = 42

chute_string = input("digite o seu número: ")

print("Você digitou ", chute_string)

chute = int(chute_string)

acertou = chute == numero_secreto
chute_maior = chute > numero_secreto
chute_menor = chute < numero_secreto

if acertou:
    print("Você acertou!")
else:
    if chute_maior:
        print("Você errou! O seu chute foi maior do que o número secreto.")
    elif chute_menor:
        print("Você errou! O seu chute foi menor do que o número secreto.")

print("##################################")
print("Fim de jogo... Até a próxima!")
print("##################################")