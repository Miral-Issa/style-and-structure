import time

def print_pause(string, delay):
    print(string)
    time.sleep(delay)

def intro():
    print_pause("You have just arrived at your new job!",2)
    print_pause("You are in the elevator.",2)

def valid_input(string, choices,list):
    print_pause(string,2)
    for choice in choices:
        print_pause(choice,0.5)
    
    user_choice = input()
    if user_choice.isnumeric():
        user_choice = int(user_choice)
    else:
        return "invalid"

    for option in list:
        if option == user_choice:
            return option
    return "invalid"

def first_floor(items):
    if "ID card" in items:
        print_pause("The clerk greets you, but she has already given you your ID card,"
                    " so there is nothing more to do here now.",2)
    else:
        items.append("ID card")
        print_pause("The clerk greets you and gives you your ID card.",2)

def second_floor(items):
    if "handbook" in items:
        print_pause("The HR folks are busy at their desks.",2)
        print_pause("There doesn't seem to be much to do here.",2)
    elif "ID card" in items:
        items.append("handbook")
        print_pause("The head of HR greets you.",2)
        print_pause("He looks at your ID card and then gives you a copy of the employee handbook.",2)
    else:
        print_pause("He has something for you, but says he can't" 
                    " give it to you until you go get your ID card.",2)

def third_floor(items):
    if "ID card" in items:
        print_pause("You use your ID card to open the door.",2)
        print_pause("Your program manager greets you and tells you that you need" 
                    " to have a copy of the employee handbook in order to start work.",2) 
        if "handbook" in items:
            print_pause("Fortunately, you got that from HR!",2)
            print_pause("Congratulatons! You are ready to start" 
                        " your new job as vice president of engineering!",2)
            return "finished"
        else:
            print_pause("They scowl when they see that you don't have it," 
                        " and send you back to the elevator.",2)
    else:
        print_pause("Unfortunately, the door is locked and you can't get in.",2)
        print_pause("It looks like you need some kind of key card to open the door.",2)
        print_pause("You head back to the elevator.",2)

    return "unfinished"

def arrive_to_floor(choice,items):
    floor = ""
    floor_name = ""
    if choice == 1:
        floor = 'first'
        floor_name = 'Lobby'
        floor_greeting(floor,floor_name)
        first_floor(items)

    elif choice == 2:
        floor = 'second'
        floor_name = 'Human resources'
        floor_greeting(floor,floor_name)
        second_floor(items)

    elif choice == 3:
        floor = 'third'
        floor_name = 'Engineering department'
        floor_greeting(floor,floor_name)
        return third_floor(items)
    
    print_pause(f'Where would you like to go next?',2)
    return "unfinished"

def floor_greeting(floor, floor_name):
    print_pause(f'You push the button for the {floor} floor.',2)
    print_pause(f'After a few moments, you find yourself in the {floor_name}.',2)
    
        
def in_elevator(items):
    user_choice = valid_input("Please enter the number for the floor you would like to visit:"
                              ,["1. Lobby","2. Human resources","3. Engineering department"] 
                              ,[1,2,3])
    is_finished = ""
    if user_choice != "invalid":
        is_finished = arrive_to_floor(user_choice,items)
    
    if is_finished == "unfinished":
        in_elevator(items)
    
def elevator():
    items = []
    intro()
    in_elevator(items)

elevator()
    