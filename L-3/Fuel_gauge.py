while True:
    try:
        x=input("What's the fraction??")
        a,b=x.split("/")
        a=int(a)
        b=int(b)
        c=(a/b)*100
        if c>1 and c<99:
            print(c,"%")
        elif c<=1:
            print("E")
        else:
            print("F")

    except ValueError or ZeroDivisionError:
        pass
    else:
        break                