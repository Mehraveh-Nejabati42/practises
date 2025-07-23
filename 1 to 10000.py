import random
random_number=random.randint(1,10000)
a=int(input('enter the number u think i picked:'))
s=0
while True:
    if random_number==a:
        print('u guessed correctly! the number was', random_number)
        print('it took u', s, 'guesses!')
        break
    elif random_number!=a:
        print('wrong')
        if random_number>a:
            print('the number i chose is more than',a)
            a=int(input('guess another number:'))
            s+=1
        elif random_number<a:
            print('the number i chose is less than',a)
            a=int(input('guess another number:'))
            s+=1
        