def updata(data):
    while True:
        ac=int(input("\nPlease Enter Your Account Number :"))
        if ac in data[4]:
            ind=data[4].index(ac)
            while True:
                a=int(input("1. for Name ,2. for Mobile ,3. for Password ,4. for Exit:"))
                if a==1:
                    data[3][ind]=input("Enter New Name :")
                elif a==2:
                    data[6][ind]=int(input("Enter New Mobile Number :"))
                elif a==3:
                    data[7][ind]=input("Enter New Password:")
                else:
                    break         
        else:
            print("Sorry Wrong Account Number")
        op=int(input("Press 1 for Update Other Customer Data or Exit :"))
        if op!=1:
            break
    return data



    
