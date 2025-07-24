#def sum(a,b):
    #result = a+b
    #return result

#num1 = int(input("ตัวเลขที่ 1:"))
#num2 = int(input("ตัวเลขที่ 2:"))

#result = sum(num1,num2)

#sum(result)


def add(num1,num2): #เรียกใช้ฟังก์ชัน
    result = num1 + num2
    return result 
 
def minus(num1,num2):
    result = num1 - num2
    return result

def mutiple(num1,num2):
    result = num1 * num2
    return result

def divide(num1,num2):
    result = num1 / num2
    return result

def is_even(num):
    result = num %2
    if result== 0:
        return("even")
    else:
        return("เลขคี่")

    
def main():
    num1 = int(input("กรอกเลขตัวที่ 1:"))
    num2 = int(input("กรอกตัวเลขที่ 2:"))
    print("+ - * /  คุณจะเลือกก")
    print("[1] +")
    print("[2] -")
    print("[3] *")
    print("[4] %")
    operation = input("เจ้าจะเลือก:")
    if (operation == "1"):
        result = add(num1,num2)
        print("ผลรวมจาการบวก:",result)
    elif (operation == "2"):
        result = minus(num1,num2)
        print("ผลจากการลบ :",result)
    elif(operation == "3"):
        result = mutiple(num1,num2)
        print("ผลจากการคูณ:",result)
    elif(operation == "4"):
        result = divide(num1,num2)
        print("ผลจากการหาร :",result)
  
    print(is_even(result))

main()