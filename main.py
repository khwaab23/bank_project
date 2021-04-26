from bank import bankmain as bm
from bank import enterdata as ea
from bank import update as ud
from bank import delete as dd
from bank import showdata_bank as sb
from customer import credit as c
from customer import debit as d
from customer import showdata as s
from customer import cm

print("WELCOME")
Bank_ID="S"
Bank_Password="S"
Bank_Balance=0
CN=[]
CA=[]
CB=[]
CM=[]
CP=[]
check_variable=0 #no of customers
data=[Bank_ID,Bank_Password,Bank_Balance,CN,CA,CB,CM,CP,check_variable]
while True:
    op=int(input("\nPress 1 for Bank and 2 for Customer and 3 for Exit :"))
    if op==1:
        a=input("\n\nEnter UserName :")
        b=input("Enter Password :")
        if a==Bank_ID and b==Bank_Password:
            data=bm.bank_main(data,ea,ud,dd,sb,bm)
        else:
            print("Invalid Input")
    elif op==2:
        if data[8]==0:
            print("Sorry Bank not have any Data ")
        else:
            uid=int(input("Please Enter Your Account Number :"))
            upp=input("Please Enter Your Account PIN    :")
            indx=data[4].index(uid)
            indd=data[7].index(upp)
            if ( (data[4][indx]==uid) ):
                if (data[7][indd]==upp):
                    data=cm.customer_main(data,indx,c,d,s)
                else:
                    print("Sorry Wrong Password") 
            else:
                print("Sorry Wrong ID ") 
    elif op==3:
        break
    else:
        print("Wrong input ")
print("\n\nTHANKS For VISIT")
