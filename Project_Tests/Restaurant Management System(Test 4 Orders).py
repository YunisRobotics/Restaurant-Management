orders = open("Orders.txt", "r")
if(orders.readable()):
    print(orders.read())
else:
    print("Can't open file")

orders.close()
