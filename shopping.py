price=int(input("enter the price:"))
if price>=5000000 and price<15000000:
    t=price*0.05
    print("u got 5% off, that will be", t)
elif price>=15000000:
    r=price*0.10
    print("u got 10% off, that will be", r)
else:
    print("that will be", price)
    