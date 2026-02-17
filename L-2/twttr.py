"""When texting or tweeting, it’s not uncommon to shorten words to save time or space,
as by omitting vowels, much like Twitter was originally called twttr. 
In a file called twttr.py, implement a program that prompts the user for a str of
text and then outputs that same text but with all vowels (A, E, I, O, and U) 
omitted, whether inputted in uppercase or lowercase"""

a = input("Give me some input ")
n = len(a)
p=0

while p<n:
    if a[p] == 'a':
       a =  a.replace("a", "")
    elif a[p] == "e":
        a = a.replace("e", "")
    elif a[p] == "i":
        a = a.replace("i", "")
    elif a[p] == "o":
        a = a.replace("o", "")  
    elif a[p] == "u":
        a = a.replace("u", "")    
    else:  p=p+1

print(a)