import random , time
print ("welcome to california hotel")
age = int(input("please enter ur age:"))
one_night = 6000000
every_person_services =  500000
if age >= 18 :
    adults = int(input("how many adults do u want to check in?:"))
    teens = int(input("how many teens?:"))
    childs = int(input("and how many childs?:"))
    total_people = adults + teens 
    if total_people > 7 :
        print ("sorry we can't check in more then 7 people in one room")
    elif total_people >= 1 :
        nights = int(input("and how many nights r u going to stay at our hotel?:"))
        total_cost = nights * one_night + adults * every_person_services + teens * every_person_services
        if childs >= 1 :
            child_services = str(input("is ur child gonna use the hotel services?"))
            if child_services == "yes" :
                total_cost += every_person_services * childs
        print ("that will cost" , total_cost)
        time.sleep (1)
        room = random.randint (1,250)
        print("ur room number is" , room)
        print("here's the key, enjoy!")
        
    else :
        print ("u have to at least be one person")
else :
    print ("u haven't reached the legal age yet!")
    