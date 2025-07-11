#Step 1
cookbook = []

#Step 2

def create(*recipe): 
    cookbook.extend(recipe)
    print(f"Recipe {recipe} has been added to the cookbook.")

#Step 3 

def read (index):
    if index < len(cookbook):
        item = cookbook[index]
    else:
        print("The index is invalid.")
    return item 

#Step 4
def update(index,recipe): 
    if index <len(cookbook):
        cookbook[index] = recipe 
        print(f"{recipe} has been updated to the cookbook.")
    else: 
        print("The index is invalid.")
create("Pizza")
create("Noodles","Fried Durian", "Dumplings", "Rice", "Salmon")
update(2,"Sushi")
print(cookbook)

#Step 5
def destroy(index): 
   if index <len(cookbook):
        remove = cookbook.pop(index) 
        print(f"{remove} has been removed.")
   else: 
       print("The index is in invalid.")

destroy(2)

#Step 6
def list_all_recipes ():
    for recipe in cookbook: 
        print(recipe)
    
list_all_recipes()

#Step 7
def main():
    while True:
        print("\nCookbook Recipes")
        print("1. Add a Recipe")
        print("2. Read a Recipe")
        print("3. Update a Recipe")
        print("4. Delete a Recipe")
        print("5. Display all Recipes")
        print("6. Exit")


        choice = input("Choose an option (1-6): ")


        if choice == "1":
            recipe = input("Enter the name of the recipe: ")
            create(recipe)
        elif choice == "2":
            index = input("Enter the index of the recipe to read: ")
            index = int(index)
            read(index)
        elif choice == "3":
            index = input("Enter the index of the recipe to update: ")
            recipe = input("Enter the name of the recipe you want to update it with: ")
            index = int(index)
            update(index, recipe)
        elif choice == "4":
            index = input("Enter the index of the recipe to delete: ")
            index = int(index)
            destroy(index)
        elif choice == "5":
            list_all_recipes()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


main()

