pass_=int(input("enter the password:"))
if pass_<8:
    print("weak password")
elif pass_>=8 and pass_<12:
    print("medium password")
else:
    print("strong password")