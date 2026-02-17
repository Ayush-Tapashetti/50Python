def main():

    def fun2(Ans):
        if Ans == "42" or Ans == "forty-two" or Ans == "forty two":
            print("Yes")
        else: print("No")     

    Sol = input("What is the answer to the Great Question, the Universe of Everything??")
    Sol = Sol.lower()
    fun2(Sol)

main()