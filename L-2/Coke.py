amt_due = 50

while amt_due > 0:
    print("Amount due : " , amt_due)
    coin = int(input("Insert Coin"))
    if coin in [25,10,5]:
        amt_due-= coin


chg_owd = abs(amt_due)
print("Change owed:" , chg_owd)    