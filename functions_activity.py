menu = {
    "Pizza": 2.99, 
    "Burger": 3.99, 
    "Hot dog": 1.99, 
    "Cheese": 0.59, 
    "Ice cream": 1.49, 
    "Churro": 0.79, 
    "Soda": 0.89}

def total_price(item1, item2): 
   Price1 = menu[item1]
   Price2 = menu[item2]
   return Price1 +Price2

def price_difference(item1,item2): 
   Price1 = menu[item1]
   Price2 = menu[item2]
   return Price1 + Price2
   
def inflation(item_name,multiplier): #pizza, 0.10
   updated_menu = menu.copy() #copied menu and named updated menu
   if item_name in updated_menu: #if pizza in copied menu
        old_price = updated_menu[item_name] # old price = menu[pizza] aka 2.99
        inflation_amount = old_price * multiplier #inflation amount = menu[pizza] or 2.99 * 0.10 = 0.299
        updated_menu[item_name]= old_price + inflation_amount # updated price of pizza= old price 2.99+ 0.299 = 3.289
   return updated_menu #returning the whole menu from the updates of the if commands

def deflation (item_name, divider): # hotdog, 0.10 
    updated_menu = menu.copy() #copies menu 
    if item_name in updated_menu: #if hotdog in updated menu set up changes in updated menu
       old_price = updated_menu[item_name]  
       updated_menu[item_name] = old_price / divider
    return updated_menu

print(deflation("Pizza",2))   

