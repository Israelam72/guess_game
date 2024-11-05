from utils import start_game

def main():
    print("Bem vindo ao jogo de adivinhar!")
    print("Escolha a dificuldade para adivinhar o número que o computador escolhe de 0 a 100")
    command()

def command():
    print("1 - Fácil: 10 tentativas\n2 - Normal: 7 tentativas\n3 - Dificíl: 5 tentativas")

    try:
        while True:
            dificuldade = int(input("Escolha: "))
            if dificuldade not in [1, 2, 3]:
                print("Número não valido, escolha 1, 2 ou 3")
            elif dificuldade == 1:
                print("Dificuldade facil escolhida, você tem 10 tentativas")
                tentativas = 10
                break
            elif dificuldade == 2:
                print("Dificuldade normal escolhida, você tem 7 tentativas")
                tentativas = 7
                break
            elif dificuldade == 3:
                print("Dificuldade dificil escolhida, você tem 5 tentativas")
                tentativas = 5
                break
            else:
                print("Input não valido, tente novamente")
        start_game.start_game(tentativas)
    except ValueError:
        print("Escolha não valida, escolha 1, 2 ou 3")
        command()
if __name__ == '__main__':
    main()

