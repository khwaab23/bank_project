def cr_bl(data,indx):
    bl=int(input("Enter Ammount for Credit :"))
    if bl>=1:
        data[5][indx]+=bl
        data[2]+=bl
        print("Your Current Balance :",data[5][indx])
    else:
        print("Please Enter Ammount in +ve Value ")
    return data

    
