#lab 5 Selina Xue

#cat function
def cat_greeting(word): 
    print(f'Cat says {word}')
cat_greeting("meow")

#superhero power function 
def generate_superhero_power():
    name = "John"
    power = "flying"
    print(f"{name}'s power is {power}")
generate_superhero_power()

#step 3
def generate_superhero_power1():
    power = "Flying"
    return power
print(generate_superhero_power1())

#step 4
def generate_superhero_power2(user_name,super_power):
    message = user_name + " has the power of " + super_power + "!"
    return message 
print(generate_superhero_power2("Liana", "time traveling"))

#step 5
def cat_greetings_loop(greeting):
    for x in range(0,5): #or just 5
        print(f'The cats says {greeting} ')
    
cat_greetings_loop("meow")

#or greetings = ["meow," "pur", "ya"]
#for i in greetings 
#print("The cats says", i) list every list items 


#step 6

def generate_multiple_powers(powers): 
    for x in powers:
        print(x)

powers_list = ["Flying", "Time Traveling", "Super Strength", "Telekinesis"]
generate_multiple_powers(powers_list)
