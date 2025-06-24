#Lab 3 Seina Xue

#Task 1 Working with Strings

food = 'Salmon Sushi'
print(food[0:3])
print(food[-3:])

#Not inclusive for negatives

first_last = food[0] + food [-1]
print(first_last)
food_list = food.split()
print(food_list)
joined_food = ' '.join(food_list)
print(joined_food)

#Task 2: Working with Lists

number_list = [1, 234, 42, 654, 389, -298, -4]
number_list.append(-89)
print(number_list)
number_list.insert(3,500)
print(number_list)
number_list.pop()
print(number_list)
number_list.remove(234)
print(number_list)



print("The first 3 int",number_list[0:3])
#Goes up to 3 position but doesnt include 3rd position alike <, >, open/close circle number line
print("The last 3 int", number_list[-3:])
#Negative starts from -1 goes down to -4 doesnt include -4 integer value either 
# [-1:-4] or [-3:]. [x:y] isn't inclusive but [x:] is

# Task 3 Working with Dictionaries

books = {"E.M Forster": "A Room with a View", 
        "Kurt Vonnegut": "Slaughterhouse-Five",
        "Margaret Atwood": "Handmaids's Tale",
        "Franz Kafka": "The Metamorphosis"}

print(books.keys())
print(books.values())
print(books.get("Franz Kafka"))
books.pop("Margaret Atwood")
print(books)
del books ["E.M Forster"]
print(books)






