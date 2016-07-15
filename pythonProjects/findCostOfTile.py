width = float(input("Width of floor: "))
length = float(input("Length of floor: "))
cost = float(input("Cost of Tile: "))

print ("Cost to tile a %.2f x %.2f floor is: $%.2f" % (width, length, width * length * cost))