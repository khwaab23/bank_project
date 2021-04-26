
def deltedata(data):
    while True:
        ac=int(input("\nPlease Enter Your Account Number :"))
        if ac in data[4]:
            ind=data[4].index(ac)
            del data[3][ind]
            del data[4][ind]
            del data[6][ind]
            del data[7][ind]
            data[2]=data[2]-data[5][ind]
            del data[5][ind]        
        else:
            print("Sorry Wrong Account Number")
        op=int(input("Press 1 for Delete Other Customer Data or Exit :"))
        if op!=1:
            break
    return data



    

    
