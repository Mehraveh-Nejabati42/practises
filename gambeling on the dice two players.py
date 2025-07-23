import random,time
print("welcome to the gambeling game")      #game explenation
print("u have 5 dices and before rolling them u should geuss the total sum of ur dices")
print("if u roll 6 u will get a prize dice")
print("both players ready? lets do this")
user1=int(input("player one enter the score u think u would get:")) #player ones choice
step=5
total1=0
i=1
while step>0:
    dice=random.randint(1,6)
    print("dice",i,"=",dice)
    total1+= dice
    i+=1
    time.sleep(1)
    if dice==6:
        print("u have rolled 6, u have a prize dice!")
        time.sleep(1)
        continue
    step-=1
print("player ones total rolls=",total1)
time.sleep(1)
if total1<user1:
    score1=0
elif total1>=user1:
    score1=user1*5+(total1-user1)
print("player one's score=",score1)  #player ones score

time.sleep(1)
user2=int(input("player two enter the score u think u would get:"))  #player twos choice
step=5
total2=0
i=1
while step>0:
    dice=random.randint(1,6)
    print("dice",i,"=",dice)
    total2+= dice
    i+=1
    time.sleep(1)
    if dice==6:
        print("u have rolled 6, u have a prize dice!")
        time.sleep(1)
        continue
    step-=1
print("player two's total rolls=",total2)
time.sleep(1)
if total2<user2:
    score2=0
elif total2>=user2:
    score2=user2*5+(total2-user2)
time.sleep(1)
print("player two's score=",score2)    #player second plsyers score
time.sleep(1)

  #find the winner
if score1>score2:
    print("player one wins!")
elif score2>score1:
    print("player two wins!")
elif score1==score2:
    print("its a tie!")