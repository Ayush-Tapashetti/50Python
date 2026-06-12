"""cal = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]





while True:
    try:
        a = input("Date:").replace("/"," ")
        p,q,r = a.split(" ",2)
        if p in cal:
            for i in range(len(cal)):
                if cal[i]==p:
                    d=i+1
            print(r,"-",d,"-",q[0],sep="")                        

        elif int(q)<=31 and int(p)<=12:
            print(r,"-",p,"-",q,"-")
        break    

    except ValueError:
        pass        
"""

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    d = input("Date: ").strip()
    try:
        if "/" in d:
            m, da, y = d.split("/")
            if 1 <= int(m) <= 12 and 1 <= int(da) <= 31:
                print(f"{int(y)}-{int(m):02}-{int(da):02}")
                break

        elif "," in d:
            p = d.split(" ")
            if len(p) == 3:
                m_name, da_str, y = p
                if m_name in months:
                    da = da_str.replace(",", "")
                    m_index = m.index(m_name) + 1
                    if 1 <= int(da) <= 31:
                        print(f"{int(y)}-{m_index:02}-{int(da):02}")
                        break
    except:
        pass 
            
        