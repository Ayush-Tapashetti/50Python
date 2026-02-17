"""     123         1234
        456         5678
        789         9101112"""

n = int(input("Give me some number"))


for i in range(n):
    i=i+n
    for j in range(n):
        print(i+j+1,end=" ")
        j=j+n
    print("") 
