#Guessing Game : Jayla, Louis, Maite, Maliha, Selina

#Step 3
import random 


def generate_random_number(): 

    return random.randint(1,100)

def get_user_guess(): 
    while True: 
        try: 
            user_input = int(input("Guess a number from 1 to 100 "))
            if 1<= (user_input) <= 100: 
                return user_input
            else: 
                print("Enter a valid number between 1 and 100 ")
        
        except ValueError: 
            print("Please enter an valid integer ")


#Step 4 

def play_guessing_game():
    print("Guess a number between 1 and 100 and see if you guessed it right ")
    secret_number = generate_random_number()  

    while True: 
        guess = get_user_guess()
        
        if guess < secret_number: 
            print ("Too low. ")

        elif guess > secret_number: 
            print ("Too high. ")

        else:
            print ("Congrats, you got it. ")
            break

#Step 5

def game_loop(): 
    while True: 
        play_guessing_game()

        user_input = input("Do you want to try again ").lower()
        if user_input == "yes": 
            play_guessing_game()
        else: 
            print("Thank you for playing.")
            break
    
if __name__ == "__main__": 
    game_loop()
