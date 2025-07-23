#sum = 0
#n = 3

#for i in range(n):
 #   sum += i+2

#print(sum)

#for i in range(20):
#    if i % 2 == 0:
#        print("Even number:",i)

#number = int(input("กรอกตัวเลข:"))

#for i in range(12):
    #print(number,"*", i+1,":", number*(i+1),"")

#i = 0 
#while i < 5:
 #   print("hello")
 #   i += 1
 #   if i == 4:
  #      break

start = True
while start:
    print("เลือกข้อความที่จะเล่น")
    print("ข้อที่ [1] โจทย์แรก")
    print("ข้อที่ [2] โจทย์สอง")
    x = int(input("กรุณากรอกเลข:"))
    if (x == 1):
        print("ทำโจทย์ที่ 1")
    elif (x == 2):
        print("ทำโจทย์ที่ 2")
    else :
        print("not")
    start = False