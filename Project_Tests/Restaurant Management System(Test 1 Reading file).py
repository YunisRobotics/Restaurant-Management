menus = open("Menu.txt", "r")
if(menus.readable()):
    print(menus.read())
    menus.seek(0)  #Move the file pointer back to the beginning
    info = menus.readlines()
else:
    print("Can't open file")

menus.close()
first_line = info[-1]
print(first_line[0:3])


