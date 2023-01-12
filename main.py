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
        time.sleep(1.5)
        
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
        time.sleep(1.5)
        
        #Empate
        if user_option == computer_option:
            print("\nEmpate!\n")
            time.sleep(1.5)
        
        #Victorias
        elif user_option == "piedra":
            if computer_option == "tijera":
                print("\nPiedra gana a Tijera\n")
                print("Ganaste un punto\n")
                user_wins += 1
                time.sleep(1.5)
            else:
                print("\nPapel gana a Piedra\n")
                print("La PC gana un punto\n")
                computer_wins += 1
                time.sleep(1.5)
        
        elif user_option == "papel":
            if computer_option == "piedra":
                print("\nPapel gana a Piedra\n")
                print("Ganaste un punto\n")
                user_wins += 1
                time.sleep(1.5)
            else:
                print("\nTijera gana a Papel\n")
                print("La PC gana un punto\n")
                computer_wins += 1
                time.sleep(1.5)
        
        elif user_option == "tijera":
            if computer_option == "papel":
                print("\nTijera gana a Papel\n")
                print("Ganaste un punto\n")
                user_wins += 1
                time.sleep(1.5)
            else:
                print("\nPiedra gana a Tijera\n")
                print("La PC gana un punto\n")
                computer_wins += 1
                time.sleep(1.5)
        
        #Ganadores
        if computer_wins == 2:
            print("El ganador es la PC!!!\n")
            time.sleep(1)
            break
        
        if user_wins == 2:
            print("Felicidades Ganaste!!!\n")
            time.sleep(1)
            break

if __name__ == '__main__':
    main()