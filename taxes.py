salary = int(input("how much salary do u get per month?:"))
m = str(input("are u married?:"))
if salary > 50000 :
    tax_percent = 0.20
elif 30000 < salary <= 50000 :
    tax_percent = 0.15
elif 10000 < salary <= 30000 :
    tax_percent = 0.10
else:
    tax_percent = 0
if m == "yes" :
    tax_percent -=0.02

paiment = salary * tax_percent

print ("ur tax will be" , paiment , "dollars")