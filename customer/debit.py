def dr_bl(data,indx):
    bl=int(input("Enter Ammount for Debit :"))
    if bl<=data[5][indx]:
        data[5][indx]-=bl
        data[2]-=bl
        print("Your Current Balance :",data[5][indx])
    else:
        print("Not Efficient Balance ")
    return data

    
