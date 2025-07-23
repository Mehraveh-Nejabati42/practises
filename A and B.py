import random
sum1=0
sum2=0
i1=1
i=1
dice2=0
while sum1<100 or sum2<100:
    player1=input("player A press space to roll the dice:")
    if player1==" ":
        dice1=random.randint(1,6)
    print("dice=",dice1)
    for i1 in range(1,101):
        print(i1,"   " ,end=" ")
        if i1%10==0:
                print()
        if sum1+dice1>100:
            continue
        elif i1==dice1:
            print("A", end=" ")
            sum1+=dice1
        elif i==dice2:
            print("B", end=" ")
            sum2+=dice2
            
    player2=input("player B press space to roll the dice:")
    if player2==" ":
        dice2=random.randint(1,6)
    print("dice=",dice2)
    for i in range(1,101):
        print(i,"   " ,end=" ")
        if i%10==0:
                print()
        if sum2+dice2>100:
            print("its a bigger number")
            continue
        elif i==dice2:
            print("B", end=" ")
            sum2+=dice2
        elif i1==dice1:
            print("A", end=" ")
            sum1+=dice1
