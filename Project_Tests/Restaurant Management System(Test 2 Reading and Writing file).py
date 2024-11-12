meal = input("Please, enter the name of meal -> ")
cost = input("Please, enter the cost of meal -> ")
int_cost = int(cost)
if(meal != "" and meal.isdigit() == False and (int_cost > 0 and int_cost <= 100)):
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
