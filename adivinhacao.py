print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************", end=" \n\n")

numero_secreto = 53

chute_str = input("Digite seu numero secreto\n")

print("você digitou", chute_str)

chute = int(chute_str)

if(chute == numero_secreto):
    print("Certo!!!")
else:
    print("voce errou! o certo é", chute)

print("Fim do jogo")
