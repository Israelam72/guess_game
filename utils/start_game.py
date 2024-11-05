from random import randint

jogada_pc = randint(0, 100)
def start_game(tentativas):
    i = 0
    while i < tentativas:
        try:
            escolha = int(input("Escolha: "))
            if escolha > 100 or escolha < 0:
                print("Por favor, escolha um valor entre 0 e 100")
            elif escolha > jogada_pc:
                print("Sua escolha é maior que o número, tente novamente")
                i += 1
            elif escolha < jogada_pc:
                print("Sua escolha é menor que o número, tente novamente")
                i += 1
            else:
                print(f"VOCÊ GANHOU!! O número {escolha} é a jogada do PC, você ganhou com {i} tentativas")
                break
        except ValueError:
            print("Jogada invalida, escolha um valor entre 0 e 100")
            start_game(tentativas)
