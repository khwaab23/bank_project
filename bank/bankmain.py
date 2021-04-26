def bank_main(data,ea,ud,dd,sb,bm):
    while True:
        a=int(input("\n\nPlease Enter 1 for Bank Deatails and 2 for Customers and 3 for Exit :"))
        if a==1:
            print("\nBank Id :",data[0])
            print("Bank Password :",data[1])
            print("Bank Balance :",data[2])
        elif a==2:
            print("\n1. for Enter Data")
            print("2. for Update Data")
            print("3. for Delete Data")
            print("4. for Show Data")
            aa=int(input("Press a key :"))
            if aa !=1:
                if data[8]!=0:
                    if aa==2:
                        data=ud.updata(data)
                    elif aa==3:
                        data=dd.deltedata(data)
                    elif aa==4:
                        data=sb.DisplayBank(data)
                    else:
                        print("Invalid Input")  
                else:
                    print("\nPlease Enter Data First ")
            elif aa==1:
                data[8]+=1
                data=ea.Bank(data)
        elif a==3:
            break
        else: 
            print("\nWrong input")
    return data
      
    
