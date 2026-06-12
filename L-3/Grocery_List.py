list={}

while True:
    try:
        a =input().strip().upper()
        if a in list:
            list[a]+=1
        else:
            list[a]=1    

    except EOFError :
        print()
        for item in sorted(list.keys()):
            print(f"{list[item]} {item}")
        break