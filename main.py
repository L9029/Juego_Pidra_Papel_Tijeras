import random
import time

def main():
    options = ('piedra', 'papel', 'tijera', "1", "2", "3")

    computer_wins = 0
    user_wins = 0
    
    rounds = 1
    
    while True:
        
        print('*' * 20)
        print("""       ROUND {}""".format(rounds))
        print('*' * 20)
        
        counters = """\nComputer wins: {} * User wins: {}\n""".format(computer_wins, user_wins)
        print(counters)
        
        user_option = input("""1)Piedra \n\n2)Papel \n\n3)tijera \n\nElige: """)
        user_option = user_option.lower()
        
        rounds += 1
        
        if not user_option in options:
            print("La opcion no es valida, por favor intentelo nuevamente")
            time.sleep(3)
            continue
        
        break

if __name__ == '__main__':
    main()