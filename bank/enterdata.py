
def Bank(data):
    while True:
        Customer_name=input("\n\nEnter Customer Name :")
        data[3].append(Customer_name)
        Customer_M=int(input("Enter Customer Mobile :"))
        data[6].append(Customer_M)
        Customer_Password=input("Enter Customer Password :")
        data[7].append(Customer_Password)
        Customer_Account_Number=int(input("Enter Customer Account Number :"))
        data[4].append(Customer_Account_Number)
        Customer_Balance=int(input("Enter Balance :"))
        data[5].append(Customer_Balance)
        data[2]+=Customer_Balance
        ch=input("\nDo you Want Enter Next Customer Data press y/Y :")
        if ch!="Y" and ch!="y":
            break
    return data
