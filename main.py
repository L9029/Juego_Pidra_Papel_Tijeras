import random
import time

def main():
    options_selection = ('piedra', 'papel', 'tijera', "1", "2", "3")
    computer_options = ('piedra', 'papel', 'tijera')

    computer_wins = 0
    user_wins = 0
    
    rounds = 1
    
    while True:
        
        #Rounds actuales 
        print('*' * 20)
        print("""       ROUND {}""".format(rounds))
        print('*' * 20)
        
        #Puntaje del jugador y de la computadora
        counters = """\nComputer wins: {} * User wins: {}\n""".format(computer_wins, user_wins)
        print(counters)
        
        #Menu de opciones del usuario y input
        user_option = input("""1)Piedra \n\n2)Papel \n\n3)tijera \n\nElige: """)
        user_option = user_option.lower()
        
        rounds += 1
        
        #Validacion de la eleccion del usuario
        if not user_option in options_selection:
            print("\nLa opcion no es valida, por favor intentelo nuevamente\n")
            #Delay
            time.sleep(3)
            continue
        
        #Selección de la pc.
        computer_option = random.choice(computer_options)
        
        #Corrección de opcion del jugador
        if user_option == "1":
            user_option = "piedra"
            
        elif user_option == "2":
            user_option = "papel"
            
        elif user_option == "3":
            user_option = "tijera"
            
        else:
            pass
        
        #Opciones del jugador y la pc
        print("\nOpción del jugador => ", user_option)
        print("\nOpción del pc => ", computer_option)
        
        break

if __name__ == '__main__':
    main()