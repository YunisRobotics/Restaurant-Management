import re
check = True
total_cost = 0
fullname = input("Can you enter your name and surname: ")
while(check):
    print("Please enter the ID of meal that you want:")
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
