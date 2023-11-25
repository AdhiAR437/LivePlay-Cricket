a={"name":"A",
   "amount":1500,

}

def verifypin(pin):
    if(pin==123):
        return True
    return False
def withdraw():
    rr = int(input("enter amount"))
    a["amount"] = a["amount"] - rr

pin=int(input("enter pin"))
if(verifypin(pin)):
    while(1):
        print("choose task")
        print("1 to show balance\n")
        print("2 to deposit ")
        print("3 to withdrawal")
        print("4 exit")
        ttt=int(input())
        if(ttt==1):
            print(a["amount"])
        elif(ttt==2):
            rr=int(input("enter amount"))
            a["amount"]=a["amount"]+rr
        elif(ttt==3):
            withdraw()
        elif(ttt==4):
            break
        else:
            print("Invalid task number")


