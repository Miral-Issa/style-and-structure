import time

def type_delay(string):
    print(string)
    time.sleep(1)

def valid_choice(string, list):
    user_choice = input(string).lower()

    for option in list:
        if option in user_choice:
            return option
    return "invalid"

def intro():
    type_delay("Hello! I am Bob, the Breakfast Bot.")
    type_delay("Today we have two breakfasts available.")
    type_delay("The first is waffles with strawberries and whipped cream.")
    type_delay("The second is sweet potato pancakes with butter and syrup.")
 
def take_order():
    while True:
        #rder = input("Please place your order. Would you like waffles or pancakes?\n")
        #order =order.lower()
        order = valid_choice("Please place your order. Would you like waffles or pancakes?\n",
                             ['waffles','pancakes'])
        
        if order == 'waffles':
            type_delay("Waffles it is!")
            #return "waffles"
            break

        elif order == 'pancakes':
            type_delay("Pancakes it is!")
            #return "pancakes"
            break
        
        else:
            type_delay("Sorry, I don't understand.")
    
    type_delay("Your order will be ready shortly.")
    order_again()

def order_again():
    choice = valid_choice("Would you like to place another order? Please say 'yes' or 'no'.\n",
                 ['yes','no'])
    
    if choice == 'yes':
        type_delay("Very good, I'm happy to take another order.")
        take_order()
    elif choice == 'no':
        type_delay("OK, goodbye!")
    else:
        type_delay("sorry, I don't understand.")

def order_breakfast():
    intro()
    take_order()
    order_again()

order_breakfast()