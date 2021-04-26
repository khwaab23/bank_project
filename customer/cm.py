def customer_main(data,indx,c,d,s):
    while True:
        print("\n1. for Credit ")
        print("2. for Debit")
        print("3. for Show Data")
        print("4. for Exit ")
        aa=int(input("Press a key :"))
        if aa==1:
            data=c.cr_bl(data,indx)
        elif aa==2:
            data=d.dr_bl(data,indx)
        elif aa==3:
            s.sw_bl(data,indx)
        elif aa==4:
            break
        else:
            print("Wrong input")
    return data
        
