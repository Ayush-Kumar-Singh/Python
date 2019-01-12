a = str(input("Enter the file name you want to create a file with: "))

try:
    f = open(a)
    print("File Exists")
    d = str(input("Do you want to read, write or append the file: "))
    q = "read" or "Read"
    w = "write" or "Write"
    e = "append" or "Append"
    if(d == q):
        f = open(str(a),"r")
        print(f.read())
    elif(d == w):
        f = open(a,"w")
        b = input("Enter the text you want in the file : ")
        f.write(b)
    elif(d == e):
        f = open(a,"a")
        b = input("Enter the text you want in the file : ")
        f.write("\n" + b)
    f.close()
except IOError as e:
    f = open(a,"w")
    print("as the file does not exist we have created a new file",a,"for you")
    b = input("Enter the text you want in the file : ")
    f.write(b)
    f.close()
    





