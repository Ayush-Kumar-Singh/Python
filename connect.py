#player 1 = "+"
#player 2 = "-"

print("Welcome To Connect 4")
print("This your Board")

a = ["0" , "0" , "0", "0"]
b = ["0" , "0" , "0", "0"]
c = ["0" , "0" , "0", "0"]
d = ["0" , "0" , "0", "0"]

print(a)
print(b)
print(c)
print(d)

while(True):
    print("Player 1 turn")
    column = int(input("Enter The Column Number"))
    h = 1
    i = 2
    j = 3
    k = 4
    if(column == h):
        s = "0"
        j = "+" or "-"
        if(d[0] == s):
            d[0] = "+"
        elif(c[0] == s):
            c[0] = "+"
        elif(b[0] == s):
            b[0] = "+"
        elif(a[0] == s):
            a[0] = "+"
        elif(a[0] == j):
            print("column full")
    elif(column == i):
        s = "0"
        j = "+" or "-"
        if(d[1] == s):
            d[1] = "+"
        elif(c[1] == s):
            c[1] = "+"
        elif(b[1] == s):
            b[1] = "+"
        elif(a[1] == s):
            a[1] = "+"
        elif(a[1] == j):
            print("column full")
    elif(column == j):
        s = "0"
        j = "+" or "-"
        if(d[2] == s):
            d[2] = "+"
        elif(c[2] == s):
            c[2] = "+"
        elif(b[2] == s):
            b[2] = "+"
        elif(a[2] == s):
            a[2] = "+"
        elif(a[2] == j):
            print("column full")
    elif(column == k):
        s = "0"
        j = "+" or "-"
        if(d[3] == s):
            d[3] = "+"
        elif(c[3] == s):
            c[3] = "+"
        elif(b[3] == s):
            b[3] = "+"
        elif(a[3] == s):
            a[3] = "+"
        elif(a[3] == j):
            print("column full")
    print("Player 2 turn")
    column = int(input("Enter The Column Number"))
    h = 1
    i = 2
    j = 3
    k = 4
    if(column == h):
        s = "0"
        j = "+" or "-"
        if(d[0] == s):
            d[0] = "-"
        elif(c[0] == s):
            c[0] = "-"
        elif(b[0] == s):
            b[0] = "-"
        elif(a[0] == s):
            a[0] = "-"
        elif(a[0] == j):
            print("column full")
    elif(column == i):
        s = "0"
        j = "+" or "-"
        if(d[1] == s):
            d[1] = "-"
        elif(c[1] == s):
            c[1] = "-"
        elif(b[1] == s):
            b[1] = "-"
        elif(a[1] == s):
            a[1] = "-"
        elif(a[1] == j):
            print("column full")
    elif(column == j):
        s = "0"
        j = "+" or "-"
        if(d[2] == s):
            d[2] = "-"
        elif(c[2] == s):
            c[2] = "-"
        elif(b[2] == s):
            b[2] = "-"
        elif(a[2] == s):
            a[2] = "-"
        elif(a[2] == j):
            print("column full")
    elif(column == k):
        s = "0"
        j = "+" or "-"
        if(d[3] == s):
            d[3] = "-"
        elif(c[3] == s):
            c[3] = "-"
        elif(b[3] == s):
            b[3] = "-"
        elif(a[3] == s):
            a[3] = "-"
        elif(a[0] == j):
            print("column full")
        
    print(a)
    print(b)
    print(c)
    print(d)
        
        


