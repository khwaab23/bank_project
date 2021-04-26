
def DisplayBank(data):
    while True:
        ac=int(input("\nPlease Enter Your Account Number :"))
        if ac in data[4]:
            ind=data[4].index(ac)
            print("\nYour Name :",data[3][ind])
            print("Your Account Number :",data[4][ind])
            print("Your Balance :",data[5][ind])
            print("Your Mobile Number :",data[6][ind])            
        else:
            print("Sorry Wrong Account Number")
        op=int(input("Press 1 for Display Other Customer Data or Exit :"))
        if op!=1:
            break
    return data



    

    
