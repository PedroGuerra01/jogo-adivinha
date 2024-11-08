
valor_CERTO = 7


while True:
    try:

        numero = float(
            input("Para começar o jogo, digite um número entre 1 a 10: "))

        # Verifica se o número está correto
        if numero > valor_CERTO:
            print("SE FODEU! O número é maior. Tente novamente.")
        elif numero < valor_CERTO:
            print("SE FODEU! O número é menor. Tente novamente.")
        else:
            print("PARABÉNS VOCÊ VENCEU!")
            break  # Encerra o laço, pois o número está correto
    except ValueError:
        print("Erro: Para recomeçar digite um novo numero:")
