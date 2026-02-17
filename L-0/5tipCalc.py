def main():
    def fun1(totalamt, per):
        per = per/100
        tipp = totalamt * per
        return tipp
    
    totalamt = input("What was your total bill, in dollars?")
    totalamt = float(totalamt.replace("$" , ""))
    per = input("What is the tip%??")
    per = float(per.replace("%" , ""))
    tip = fun1(totalamt, per)
    print(tip , "is the amount of tip provided by you")
    
main()