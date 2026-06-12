def abc(i,j):
    if i<=0 and j<=0: return
    print("Say Hi")
    abc(i-1,j-1)

abc(6,7)