monster = 100
w1 = 60
w2 = 20
w3 = 30


gamestart = True

while gamestart:
    print("จะต่อสู้หรือจะหนี")
    print("จะสู้ 1")
    print("หนีแล้ว 2")
    x = int(input("เลือกมา :"))
    if (x == 1):
        print("ป่ะเล่นต่อ")
        hit = int(input("จะตีกี่รอบจ๊ะ :"))
        for i in range(hit):
            print("w1 = ",w1)
            print("w2 = ",w2)
            print("w3 = ",w3)
            print("monster healt :",monster)
            print("เหลือโอกาสตีอยู่ :",hit - 1)
            y = input("เลือกอาวุธไหนจ๊ะ :")
            print("คุณเลือกอาวุธ",y)
            if y == w1:
                monster -= w1
                if monster < 0:
                    print("ตีแรงเกินฮีลมา 20")
                
            
        





    elif (x == 2):
        print("จบเกมจร้า")
    break