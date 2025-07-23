import random
s=['خط','شير']
c='اره'
print('به بازيه شير يا خط خوش امديد!')
user_choice=str(input('شير يا خط؟:'))
computer_choice=random.choice(s)
while c=='اره':
    if user_choice not in s:
        print('اشتباه وارد کرده ايد فقط شير يا خط')
        user_choice=str(input('شير يا خط؟:'))
        computer_choice=random.choice(s)
    elif user_choice==computer_choice:
        print('درسته!', computer_choice, 'اومد')
        c=str(input('مي خواهي دوباره بازي کنيم؟:'))
        if c=='اره':
             print('باشه')
             user_choice=str(input('شير يا خط؟:'))
             computer_choice=random.choice(s)
             continue
        else:
            print('باشه')
            break
    elif user_choice!=computer_choice:
        print('اشتباه',computer_choice, 'بود!')
        c=str(input('مي خواهي دوباره بازي کنيم؟:'))
        if c=='اره':
             print('باشه')
             user_choice=str(input('شير يا خط؟:'))
             computer_choice=random.choice(s)
             continue
        else:
            print('باشه')
            break