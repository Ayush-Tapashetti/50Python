Greet = input("Bless me with a greeting,good sir/madam")
Greet = Greet.strip().lower()
  
if Greet.startswith("hello"):
        print("$0")
elif Greet.startswith("h"):
        print("$20")
else:
        print("$100")
