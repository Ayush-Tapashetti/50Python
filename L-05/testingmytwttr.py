def main():
    a= input("Gimme input")
    print(shorten(a))




def shorten(word="Invalid input good sir"):
    b="AEIOUaeiou"
    p=[]

    for i in range(len(word)):
        if word[i] in b:
            pass
        else:
            p.append(word[i])
    p=str(p)
    return p





if __name__=="__main__":
    main()    