import sys #We add this module, because, sometimes we need to use exit for closing our program
import re #We add this module, because, we can use regular expression
class Restaurant:
    def Menu(self):  #This function reads all menus from Menu.txt file
        menus = open("Menu.txt", "r")
        if(menus.readable()):
            print(menus.read())
        else:
            print("Can't read file")

        menus.close()


    def Add_Menu(self):  #This function add menu to the Menu.txt file
        meal = input("Please, enter the name of meal -> ")
        cost = input("Please, enter the cost of meal -> ")
        check_cost = float(cost)
        if(meal != "" and meal.isdigit() == False and (check_cost > 0 and check_cost <= 100)):
            menus = open("Menu.txt", "r")
            if(menus.readable()):
                info = menus.readlines()
                menus.close()
                first_line = info[-1]
                menus = open("Menu.txt", "a")
                menus.write("\n" + str(int(first_line[0:3])+1) + ": '" + meal + "' -> '" + cost + "$'")
                menus.close()
            else:
                print("Can't open file")

        elif(meal == ""):
            print("Sorry, you enter nothing to the name of meal")
            
        elif(meal.isdigit() == True):
            print("Sorry, You entered number to the name of meal")

        else:
            print("Sorry, You entered wrong input to the cost of meal")


    def New_Order(self):  #This function enter new order to the Orders.txt file
        check = True
        total_cost = 0
        fullname = input("Can you enter your name and surname: ")
        while(check):
            print("Please enter the ID number of meal that you want:")
            menus = open("Menu.txt","r")
            if(menus.readable()):
                info = menus.readlines()
                menus.close()
                print("".join(info))
                user_id = input("ID -> ")
                true = 0
                i = 0
                pattern = r"(\d+): '([^']*)' -> '([^']*)\$'"
                for id in info:
                    if(id[0:3] == user_id):
                        true += 1
                        match = re.match(pattern, id)
                        if match:
                            meal_id = match.group(1) #Captures the ID of meal
                            meal_name = match.group(2) #Captures the name of meal
                            meal_cost = float(match.group(3)) #Captures the cost of meal

                        else:
                            print("Sorry, there is issue on system")

                if(true > 0):
                    input_slice = input("How many " + meal_name + " would you want -> ")
                    if(int(input_slice) >= 1 and int(input_slice) <= 30):
                        meal_cost2 = int(input_slice) * meal_cost
                        total_cost += meal_cost2
                        print("It costs -> " + str(meal_cost2) + "$")
                        check2 = True
                        while(check2):
                            user_again = input("Would you order another?(yes/no)")
                            if(user_again == "Yes" or user_again == "yes" or user_again == "YES" or user_again == "Y" or user_again == "y"):
                                check = True
                                check2 = False
                            elif(user_again == "No" or user_again == "no" or user_again == "NO" or user_again == "N" or user_again == "n"):
                                check = False
                                check2 = False
                                print("Here is the total cost -> " + str(total_cost) + "$")
                                print("Have a good day:)")
                                orders = open("Orders.txt", "a")
                                orders.write("\nCustomer name: '" + fullname + "'  Total_Pay: '" + str(total_cost) + "$'")
                                orders.close()
                            else:
                                check2 = True
                                print("Sorry, you enter wrong input")
                else:
                    print("You enter wrong")
            else:
                print("Sorry, there is issue on system")

    def Order(self):  #This function reads all orders from Orders.txt file
        orders = open("Orders.txt", "r")
        if(orders.readable()):
            total_cost = 0
            info = orders.readlines()
            orders.close()
            print("".join(info))
            pattern = r"Customer name: '[^']*'  Total_Pay: '([^']*)\$'"
            i = 0
            for id in info:
                match = re.match(pattern, id)
                if match:
                    meal_cost = match.group(1) #Captures the cost of meal
                    total_cost += float(meal_cost)
                    i += 1

                else:
                    print("Sorry, there is issue on system")

            print("Total_spend: " + str(total_cost) + "$   Avg_spend: " + str(round((total_cost/i), 2)) + "$") 
        else:
            print("Can't read file")


restaurant = Restaurant()
print("Welcome to the Restaurant Management System")
print("Please, enter choice that you want(1-5): ")
check = True
while(check):
    print("1.View menus")
    print("2.Add menu")
    print("3.New order")
    print("4.View all orders")
    print("5.Exit")
    user_input = input()
    if(user_input == "1"):
        restaurant.Menu() #View menus
    elif(user_input == "2"):
        restaurant.Add_Menu() #Add menu
    elif(user_input == "3"):
        restaurant.New_Order() #New order
    elif(user_input == "4"):
        restaurant.Order() #View orders
    elif(user_input == "5"):
        print("System closed") #Exiting Program
        sys.exit(0)
    else:
        print("Wrong input, Try again:(")
