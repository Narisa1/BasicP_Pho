x = input("Uresname :")
y = input("Password :")

if x == "admin":
    if y == "admin123":
        print("You are admin")
    else:
        print("wrong")
elif x == "user":
    if y == "user123":
        print("Your are user")
    else:
        print("wrong")
else :
    print("Not found")


#-----------------------------------------------

name = str(input("อยากเป็นอะไรจ๊ะ"))
word = ""

if name == "ตะแน่ว":
    word += name + " บางนา "
    print(word)
elif name == "ตะแน่ว1":
    word += name + "เดอะมอลบางกะปิ "
    print(word)
elif name == "tung tung ":
    word = name + " Tararetarara "
elif name == "ตะแน่ว2":
    word += name + " สุขสวัสดิ์ "
    print(word)
else:
    print("not found")

#------------------------
