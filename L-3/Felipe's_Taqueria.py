total=float(0)
taqira={
"Baja Taco": 4.25,
"Burrito": 7.50,
"Bowl": 8.50,
"Nachos": 11.00,
"Quesadilla": 8.50,
"Super Burrito": 8.50,
"Super Quesadilla": 9.50,
"Taco": 3.00,
"Tortilla Salad": 8.00
}
while True:
    try:
        a = input("Item:").title()

        if a in taqira:
            total+=taqira[a]
            print("Total:", total)
    except EOFError :
        break
    else:
        pass
                