import random
sum1=0
sum2=0
while sum1<100 or sum2<100:
    pa=str(input("press space to roll the dice player A:")) #player A's turn
    dice_a=random.randint(1,6)
    print("dice=",dice_a)
    sum1+=dice_a
    if pa==" ":
        for i in range(1,101):
            if sum1==i:
                print("A",end="")
            if sum2==i:
                print("B",end="")
            print(i,end="    ")
            if i%10==0:
                print()

    pb=str(input("press space to roll the dice player B:"))  #player B's turn
    dice_b=random.randint(1,6)
    print("dice=",dice_b)
    sum2+=dice_b
    if pb==" ":
        for j in range(1,101):
            if sum2==j:
                print("B",end="")
            if sum1==j:
                print("A",end="")
            print(j,end="    ")
            if j%10==0:
                print()
        