#Case 1
x = 10
y = 5
result = x / y
print("Result:", result)

#encounter runtime zero divisor, fixed by dividing 5

#Case 2 
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
   print(numbers[i])
         
#encounter format error, '(' was never closed, fixed with closed brackets
#2nd encounter runtime error list index out of range, deleted index position +1 from i+1

#Case 3

def calculate_area(radius):
   area = 3.14 * radius ** 2
   return area
 
radius = 5
print(calculate_area(radius))

#Format error no colons

#Case 4

def is_even(number):
   if number % 2 == 0:
       return True
   else: 
       return False
 
print(is_even(4))
print(is_even(7))

#format issue > needed colons after 0 and else

#Case 5
for i in range(5):
   print(i)

#format issue needed colons after 5

#Case 6 
def greet(name):
   return "Hello, " + name
 
print(greet("Alice"))

#name wasn't given an instruction, added + between hello and name

#Case 7 
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number

print("Sum of numbers:", sum)

#indentation error, added space by tab sum+=number

#Case 8 
def factorial(n):
   if n == 0:
       return 1
   else: 
       return n * factorial(n-1)
 
print(factorial(5))

#goes on forever to infinity because its 5*6*7..., factorial is 1*2*3*4*5 or 5*4*3*2*1 so it should be n-1 instead of n+1

#Case 9
name = input("Enter your name: ")
if name == "Alice" or name == "Bob":
   print("Hello, " + name)
else:
   print("Hello, stranger!")


# else statement doesn't work properly , bob is always true so else statement never shows up, added name == "Bob"

# Case 10 
def divide_numbers(x, y):
   result = x / y
   return result
 
num1 = 10
num2 = 2
print(divide_numbers(num1, num2))

#zerodivision error, you can't divide by 0, changed to 2 

