#ATM management system
print("welcome to my bank ATM")
chance=3
balance=500
while chance >0:
    pin=int(input("please enter your pin\n"))

    if pin == 1234:
        print("you enter your pin correctly")
        print("press 1 for your balance enquiry")
        print("press 2 to make a withdrawal ")
        print("press 3 to pay in")
        print("press 4 to remove your card")
        option=int(input("What you like to choose:\n"))
        while option!={1,2,3,4}:
            if option==1:
                print(f"your balance is:{balance}")
                break
            elif option==2:
                witd=int(input("enter your withdrawal amount:\n"))
                balance=balance-witd
                break
            elif option==3:
                pay_in=int(input("Enter the amount you want to pay in:\n"))
                balance=balance+pay_in
                break
            elif option==4:
                print("your card is removing")
                print("thank you")
                break
            else:
                print("you have entered a wrong input:")
                break
    else:
        print("you have entered a wrong pin,please try again")
        print(f"you have {chance} left")
