#Task 1

checking = "yes"
while checking == "yes":
    user_input = input("What is your age?")
    if int(user_input) >= 18: 
        print("You are elligible to vote")
    else: 
        print("You are not elligible to vote")
    checking = input("Do you want to check another age?")
    user_input2= input
    checking = user_input2



# #Task 2

list1=[-4, 0, 8, -9, 2]
for x in list1: 
        if x > 0: ("Value is positive")
        elif x < 0: ("Value is negative")
        else: ("Value is 0")

# #Task 3
inventory = ["coal", "gold", "silver", "diamond", "obsidian"]
for block in inventory: 
    print(f"Found {block}")

    if block == "gold": 
        print("Do you want to sell this?")
    elif block == "coal": 
        print("Do you want to start a fire?")
    elif block == "diamond": 
        print("Congraduations! You found the Jackpot!")


#Bonus Challenge 
    
checking = True
while checking: 
    user_input = input("What is your age or type 'stop' to exit")
    if user_input == "stop": 
        checking = False
    elif int(user_input) >= 18:
        print("You are elligible to vote.")
    else: 
        print("You are not elligible to vote")
    user_input2 = input("Do you want to check another age?")
    if (user_input2 != 'Yes') and (user_input2 != 'yes'):
        checking = False

