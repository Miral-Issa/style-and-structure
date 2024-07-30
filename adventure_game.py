import time
import random


def print_delay(string, delay):
    print(string)
    time.sleep(delay)


def valid_choice(string, choices):
    print_delay(string, 2)

    for choice in choices:
        print_delay(choice, 0.5)

    user_choice = input().lower()
    if user_choice.isnumeric() is False:
        return -1
    else:
        user_choice = int(user_choice)
    valid_choices = range(len(choices))
    for n in valid_choices:
        if n+1 == user_choice:
            return n+1
    return -1


def intro():
    print_delay("it's a beautiful spring day today.", 2)
    print_delay("you want to make a pie for your family", 2)
    print_delay("you get your recipe book out and go to the pie section", 2)

    pie_type = random.choice(["Apple", "Peach", "Mango", "Pear"])
    pie_crust = random.choice(["Flaky", "Tender", "Cream Cheese"])
    print_delay(f"you decided to make {pie_type}"
                f" pie with {pie_crust} crust", 2)


def check_ingrediants(items, baking_time):
    print_delay("you went checking your kitchen for "
                "the ingrediants you'll need to make your pie", 2.3)
    if "bad filling" in items:
        print_delay("you already made the filling with what"
                    " ingrediants you could find", 2)
        print_delay("no use in buying what was missing now", 2)
    elif "all ingrediants" in items:
        print_delay("all ingrediants you need are already ready"
                    " on the kitchen table", 2)
    else:
        items.append("all ingrediants")
        print_delay("you found some ingrediants were missing", 2.5)
        print_delay("so you went for the nearby supermarket and"
                    " bought what's missing", 2)
        print_delay("you're sure now that you have everything you need", 2)
    making_pie(items, baking_time)


def make_crust(items, baking_time):
    if "ready crust" in items or "burned crust" in items:
        print_delay("your crust is ready", 1)
    elif "uncooked crust" in items:
        if time.time() - baking_time >= 15:
            if time.time() - baking_time >= random.randint(30,40):
                items.append("burned crust")
                print_delay("you waited for too long and the"
                            " crust is burned now!!", 2)
            else:
                items.append("ready crust")
                print_delay("the crust finished baking and is"
                            " smelling really good", 2)
        else:
            print_delay("the crust didn't finish baking yet,"
                        " you need to wait", 2)
            wait_for = 15 - (time.time() - baking_time)
            print_delay(f"you need to wait for {wait_for:.0f} more seconds", 2)
    else:
        if "all ingrediants" in items:
            print_delay("you made the crust using the"
                        "ingrediantes you prepared", 2)
        else:
            print_delay("the crust doesn't need that much ingrediantes,"
                        " and furtunatlyyou have everything you"
                        " need in your kitchen", 3)
            print_delay("you made the crust using the ingrediates"
                        "you found in your kitchen", 2)
        items.append("uncooked crust")
        print_delay("you put the crust in the oven to bake it", 2)
        print_delay("you decided to use the time to make something else"
                    " instead of waitting till the crust is baked", 3)
        baking_time = time.time()

    making_pie(items, baking_time)


def make_the_filling(items, baking_time):
    if "good filling" in items or "bad filling" in items:
        print_delay("you already made the filling", 2)
    elif "all ingrediants" in items:
        items.append("good filling")
        print_delay("you made the filling using the"
                    " ingrediantes you prepared", 2)
        print_delay("it smell really good, and you're"
                    " sure it's going to be so tasty", 2)
        print_delay("you get excited to tast the pie", 2)
    else:
        items.append("bad filling")
        print_delay("while preparing the filling you found"
                    " that you are missing some ingrediantes", 2)
        print_delay("you made the filling with what you"
                    " could find in your kitchen", 4)
        print_delay("you're not sure that the filling will tast good....", 3)

    making_pie(items, baking_time)


def backing_the_pie(items, baking_time):
    if "ready crust" in items:
        if "good filling" in items:
            print_delay("with a golden crust and tasty filling,"
                        " everyone loved your pie", 2)
            print_delay("they all thanked you for this delicious pie", 2)
            print_delay("and asked you to make them a pie again tomorrow", 2)
            play_again()
        elif "bad filling" in items:
            print_delay("your crust was a success,"
                        " but the filling was another story", 2)
            print_delay("your family thanked you for your effort,"
                        " but commented badly on the filling", 3)
            play_again()
        else:
            print_delay("you need to prepare the filling first", 2)
            making_pie(items, baking_time)

    elif "burned crust" in items:
        if "good filling" in items:
            print_delay("the filling was really tasty."
                        " a shame it was baked in a burned crust", 2)
            print_delay("your family tried to eat yor pie, "
                        " but the burned crust wont cut", 3)
            print_delay("they still thanked you for the filling", 2)
            play_again()
        elif "bad filling" in items:
            print_delay("this pie was a complete disaster", 2)
            print_delay("a burned crust filled with a"
                        " terribly made filling", 3)
            print_delay("your family still thanked you for your effort"
                        " but adviced you to take on another hoby", 3)
            play_again()
        else:
            print_delay("you need to prepare the filling first", 2)
            making_pie(items, baking_time)
    elif "uncooked crust" in items:
        print_delay("the crust isn't ready yet", 2)
        making_pie(items, baking_time)
    else:
        print_delay("you need to make the crust first", 2)
        making_pie(items, baking_time)


def making_pie(items, baking_time):
    choices = ["1. check if you have all ingrediants", "2. make the crust",
               "3. make the filling", "4. bake the pie"]
    user_choice = valid_choice("what should you do now?", choices)

    while user_choice == -1:
        print_delay("please enter the number of the"
                    " choice you want to make", 2)
        user_choice = valid_choice("what should you do first?", choices)
    if user_choice == 1:
        check_ingrediants(items, baking_time)
    elif user_choice == 2:
        make_crust(items, baking_time)
    elif user_choice == 3:
        make_the_filling(items, baking_time)
    else:
        backing_the_pie(items, baking_time)


def play_again():
    user_choice = valid_choice("do you want to play again?",
                               ["1. yes", "2. no"])

    while user_choice == -1:
        print_delay("please enter the number of the"
                    " choice you want to make", 2)
        user_choice = valid_choice("do you want to play again?",
                                   ["1. yes", "2. no"])
    if user_choice == 1:
        pie_game()
    else:
        print_delay("**Game ended**", 2)


def pie_game():
    items = []
    baking_time = 0
    intro()
    making_pie(items, baking_time)


pie_game()
