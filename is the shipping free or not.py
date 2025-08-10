cost = int(input("how much did ur purchases cost?:"))
weight = int(input("how much did ur purchases weigh? (kg):"))
if cost > 1000000 and weight < 5 :
    print ("we will send ur shopping for free")
    print ("the total price would be" , cost )
else :
    print ("u have to pay for shipping")
    cost += 50000
    print ("the total price would be" , cost )