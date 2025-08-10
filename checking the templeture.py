t=int(input("دماي مورد نظر خود را بر حسب سانتي گراد بنويسيد:"))
if t<1:
    print("يخبندان")
elif t>=1 and t<9:
    print("سرماي شديد")
elif t>=9 and t<16:
    print("هواي سرد")
elif t>=16 and t<23:
    print("هواي مطلوب")
elif t>=23 and t<30:
    print("هواي گرم")
else:
    print("گرماي شديد")
