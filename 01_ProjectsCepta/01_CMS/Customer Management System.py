'''

#Program For Customer Management System(CMS)

Using List

'''

Customer_Name = ()
Customer_Detail = ()
Customer_Number = ()
Customer_Age = ()
Customer_City = ()

List_Name = []
List_ID = []
List_Number = []
List_Age = []
List_City = []

# Record initialization
List_ID = ["000001", "000002","000003"]
List_Name = ["Sudhanshu", "Hitanshu","Suman"]
List_Number = ["8800588188", "9871976219" , "7838380048"]
List_Age = [35, 25,63]
List_City = ["delhi", "agra", "delhi"]



while True:
    print()
    print("Press 1 to Add New Customer")
    print("Press 2 to Delete Customer")
    print("Press 3 to Search Customer")
    print("Press 4 to Modify Customer")
    print("Press 5 to Display All Customer")
    print("Press 6 to Exit")

    CMS = input("Enter Your Choice: ")
    if CMS == '1':

        while True:
            Customer_Name = (input("Enter Customer Name : "))
            if Customer_Name.isalpha():
                break
            else:
                print("Input valid name...")

        while True:
            Customer_ID = input("Enter Customer ID (Maximum 6 digits only) : ")
            break

            if Customer_ID.isdigit() and len(Customer_ID) <= 6:
                Customer_ID = int(Customer_ID)
                break
            else:
                print("Input valid ID")

        while True:
            Customer_Number = input("Enter Customer Mobile Number(10 Digits) : ")
            if Customer_Number.isdigit() and len(Customer_Number) == 10:
                break
            else:
                print("Input valid Number")

        while True:
            Customer_Age = (input("Enter Customer Age : "))
            if Customer_Age.isdigit():
                break
            else:
                print("Input valid age")

        while True:
            Customer_City = (input("Enter Customer City : "))
            if Customer_City.isalpha():
                break
            else:
                print("Input valid city")

        List_Name.append(Customer_Name.lower())
        List_ID.append(Customer_ID)
        List_Number.append(Customer_Number)
        List_Age.append(Customer_Age)
        List_City.append(Customer_City)
        print("Customer Successfully Added")


#To Delete a Customer
    elif CMS == '2':
        Customer_Detail = input("Enter Customer Detail to Delete:")

        # Check for correct Customer ID
        if Customer_Detail.isdigit() and len(Customer_Detail) <= 6:
            # Question : why code crashes here when customer id isn't present in list. How to prevent that?
            try:
                index_ = List_ID.index(Customer_Detail)
                List_ID.pop(index_)
                List_Name.pop(index_)
                List_Number.pop(index_)
                List_Age.pop(index_)
                List_City.pop(index_)
                print("Customer Successfully Deleted")
            except ValueError:
                print("Not a valid Customer ID.")


        # Check for correct Customer Number
        if Customer_Detail.isdigit() and len(Customer_Detail) == 10:
            try:
                index = List_Number.index(Customer_Detail)
                List_ID.pop(index)
                List_Name.pop(index)
                List_Number.pop(index)
                List_Age.pop(index)
                List_City.pop(index)
                print("Customer Successfully Deleted")
            except ValueError:
                print("Not a valid Customer Number.")


        # Check for correct Customer Name
        # if Customer_Detail.isalpha():
        #     try:
        #         index = List_Name.index(Customer_Detail.lower())
        #         List_ID.pop(index)
        #         List_Name.pop(index)
        #         List_Number.pop(index)
        #         List_Age.pop(index)
        #         List_City.pop(index)
        #         print("Customer Successfully Deleted")
        #
        #     except ValueError:
        #         print("Not a valid Customer Name.")
        #

#TO Search a Customer
    elif CMS == '3':
        Customer_ID = (input("Enter Customer ID"))

        index = List_ID.index(Customer_ID)
        if index == -1:
            print("Not a valid Customer ID.")
        else:
            print("CustomerID", List_ID[index])
            print("Customer Name", List_Name[index])
            print("CustomerNumber", List_Number[index])
            print("CustomerAge", List_Age[index])
            print("CustomerCity", List_City[index])


#To Modify the Customer Management System
    elif CMS == '4':
        Customer_ID =(input("Enter Customer ID"))
        try:
            index_ = List_ID.index(Customer_ID)
            Customer_Name = (input("Enter Customer Name"))
            Customer_Number = int(input("Enter Customer Number"))
            Customer_Age = int(input("Enter Customer Age"))
            Customer_City = (input("Enter Customer City"))
            List_Name[index_] = Customer_Name
            List_Number[index_] = Customer_Number
            List_Age[index_] = Customer_Age
            List_City[index_] = Customer_City
            print("Customer successfully updated!!")
        except ValueError:
            print("Not a valid Customer ID.")


#To Display All Customers
    elif CMS == '5':
        for i in range (len(List_ID)):
            print("Customer ID",List_ID[i],"Customer Name",List_Name[i],"Customer Number",List_Number[i],"Customer Age",
                  List_Age[i],"Customer City",List_City[i])

#To Exit a Customer Management System
    elif CMS == '6':
        exit()
#If Customer chose a wrong option
    else:
        print("You have selected a wrong option, please try again!!!")