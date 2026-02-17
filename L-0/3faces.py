def main():
    C1 = input()
    result = convert(C1)
    print(result)

def convert(text):
        text = text.replace(":)" , "Heppy heppy heppy")
        text = text.replace(":(" , "Sed sed sed")
        return text
        
main()