x = int(input("enter x:"))
y = int(input("enter y:"))
if x > 0 and y > 0 :
    print ("the dot is in the first quadrant")
elif x < 0 and y > 0 :
    print ("the dot is in the second quadrant")
elif x < 0 and y < 0 :
    print ("the dot is in the third quadrant")
elif x > 0 and y > 0 :
    print ("the dot is in the fourth quadrant")
elif x == 0 :
    print ("the dot is on the y axis")
elif y == 0 :
    print ("the dot is on the x axis")
elif x == 0 and y == 0 :
    print ("the dot is in the middle")
    