def main():
    var1 = input("What tiem is it now??")
    if 7.0<=convert(var1)<=8.0:
        print("Breakfast time!!")
    elif 12.0<=convert(var1)<=13.0:
        print("Lunch Time!!")
    elif 18.0<=convert(var1)<=19.0:
        print("Dinner time!!!")
    else: print("No meal during this HOUR!!")        


def convert(time):
    hrs, minu = time.split(":")
    minu = float(minu)
    hrs = float(hrs)
    minu = minu/60
    return hrs+minu

if __name__ == "__main__":
    main()
