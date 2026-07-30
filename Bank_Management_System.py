#__________________________________
#Bank Management System
#Created By :Shaheena
#Language:Python
#Project No.:2
#__________________________________
accounts=[]
def save_accounts():
    with open("accounts.txt","w") as file:
        for account in accounts:
            file.write(f"{account["Account Number"],account['Name'],account['Pin'],account['Balance']}\n")

while True:
    print("\n______________Bank Management System_________________")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")
    print("________________________________________________________")

    choice=input("Enter your choice:")
    if choice=="1":
        account_number=int(input("Enter the account number:"))
        name=input("Enter the name:")
        pin=int(input("Create a 4-digit pin:"))
        balance=float(input("Enter the balance:"))
        account={
            "Account Number":account_number,
            "Name":name,
            "Pin":pin,
            "Balance":float(balance)
        }
        accounts.append(account)
        save_accounts()
        print("Account Created Successfully!")
    elif choice=="2":
        login_acc_number=int(input("Enter your account number:"))
        login_name=input("Enter your name:")
        login_pin=int(input("Enter your pin:"))
        found=False
        for account in accounts:
            if account["Account Number"]==login_acc_number and account["Name"].lower()==login_name.lower() and account["Pin"]==login_pin:
                print("\n Login Successful!")
                print("Welcome",account["Name"],"!")
                while True:
                    print("\n_______Bank Menu_______")
                    print("1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdrawl")
                    print("4. Transfer Money")
                    print("5. Change pin")
                    print("6. View Account Details")
                    print("7. Delete Account")
                    print("8. Logout")
                    bank_choice=input("Enter your choice:")
                    if bank_choice=="1":
                        print("Current Balance:Rs.",account["Balance"])
                    elif bank_choice=="2":
                        amount=float(input("Enter the amount to deposit:"))
                        previous_amount=account["Balance"]
                        if amount>0:
                            account["Balance"]+=amount
                            save_accounts()
                            print("Transaction Successful!")
                            print("Previous Balance:",previous_amount)
                            print("Deposited:",amount)
                            print("Current Balance:Rs.",account["Balance"])
                        else:
                            print("Invalid Amount!")
                    elif bank_choice=="3":
                        amount=float(input("Enter the amount to withdraw:"))
                        if amount<=0:
                            print("Invalid Amount!")
                        elif amount<=account["Balance"]:
                            previous_amount=account["Balance"]
                            account["Balance"]-=amount
                            save_accounts()
                            print("Withdrawl Successful!")
                            print("Previous Balance:",previous_amount)
                            print("Withdrawl Amount:",amount)
                            print("Current Balance:Rs.",account["Balance"])
                        else:
                            print("Insufficient Balance")
                    elif bank_choice=="4":
                        receiver_account_number=int(input("Enter the receivers account number:"))
                        amount=float(input("Enter the amount to transfer:"))
                        found=False
                        for receiver in accounts:
                           if receiver_account_number==receiver["Account Number"]:
                               if amount>0 and amount<=account["Balance"]:
                                   account["Balance"]-=amount
                                   receiver["Balance"]+=amount
                                   save_accounts()
                                   print("Transfer Successful!")
                                   print("Your New Balance:",account["Balance"])
                                   found=True
                                   break
                               else:
                                   print("Invalid Amount or Insufficient Balance!")
                                   found=True
                                   break
                        if not found:
                            print("Receiver Not Found!")
                    elif bank_choice=="5":
                        old_pin=int(input("Enter your old pin:"))
                        if old_pin==account["Pin"]:
                            new_pin=input("Enter New pin:")
                            account["Pin"]=new_pin
                            save_accounts()
                            print("PIN changed successfully!")
                        else:
                            print("Invalid Pin")
                    elif bank_choice=="6":
                        print("\n_____________Account Details___________")
                        print("Account Number:",account["Account Number"])
                        print("Name          :",account["Name"])
                        print("Balance       :",account["Balance"])
                    elif bank_choice=="7":
                        confirm=input("Type YES to delete your account:")
                        if confirm.upper()=="YES":
                            accounts.remove(account)
                            save_accounts()
                            print("Account Deleted Successfully!")
                            break
                    elif bank_choice=="8":
                        print("Logged out Successfully!")
                        break
                found=True
                break
        if found==False:
            print("Invalid Account Number or Name or Pin!")
    elif choice=="3":
        print("Thanks for using Bank Management System")
        break
    
