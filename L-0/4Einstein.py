def main():
    def calc(m):
        c = 300000
        E = m * c * c
        return E

    mass = int(input("What is the mass of the given object??"))
    Calcu = calc(mass)
    print(Calcu , "is the equvivalent number of mass in Joules")

main()