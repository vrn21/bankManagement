import pickle
import mysql.connector as mc
db=mc.connect(host="localhost",user="root",passwd="killmonger21!",database="bank") #connecting pythond and SQL
cursor=db.cursor()


def login(accountnoo,pinn):   #prgrm to login into the bank server
    f1 = open("accountno and pin.txt", "rb")
    rec1 = pickle.load(f1)
    abo="y"
    while abo=="y":
          for i in rec1:
              if i[0]==accountnoo:
                  if i[1]==pinn:
                      print("Welcome to XYZ Banking Solutions")
                      print("\n")
                      abo="n"
                  else:
                      print("Sorry your Account number and PIN does not match")
                      abo=input("Do you want try logging again:(y/n)")
                      if abo.lower()=="n":
                          abo="n"
    print("\n")
    f1.close()
    
def checkbalance(accno): #function to check balance in a bank account
    cursor=db.cursor()
    cursor.execute("SELECT ACCOUNTBALANCE FROM bankmain WHERE ACCOUNTNO={}". format(accno))
    results=cursor.fetchall()
    print(results)

def diplayaccount(accno): #function to view all the account details
    cursor=db.cursor()
    cursor.execute("SELECT * FROM bankmain WHERE ACCOUNTNO={}" . format(accno))
    results = cursor.fetchall()
    print(results)

def updateacc(accno): #function to update any of the account details
    cursor = db.cursor()
    cursor.execute("SELECT * FROM bankmain WHERE ACCOUNTNO={}". format (accno))
    results = cursor.fetchall()
    print(results)
    updation=input("Which column would you like to update?(Name,Phone number or Address) :")
    upvalue=input("What would you like to be the correction: ")

    if updation.lower()=="name":
        cursor.execute("UPDATE bankmain SET NAME='{0}' WHERE ACCOUNTNO={1}". format (upvalue, accno))
        print("Congratulations your ",updation," has been changed to ",upvalue)
        cursor.execute("SELECT * FROM bankmain WHERE ACCOUNTNO={}". format (accno))
        results=cursor.fetchall()
        print(results)


    if updation.lower()=="phone number":
        cursor.execute("UPDATE bankmain SET PHONENO={0} WHERE ACCOUNTNO={1}". format(upvalue,accno))
        print("Congratulations your ", updation, " has been changed to ", upvalue)
        cursor.execute("SELECT * FROM bankmain WHERE ACCOUNTNO={}". format(accno))
        results=cursor.fetchall()
        print(results)

    if updation.lower() == "address":
        cursor.execute("UPDATE bankmain SET ADDRESS='{0}' WHERE ACCOUNTNO={1}". format(upvalue,accno))
        print("Congratulations your ", updation, " has been changed to ", upvalue)
        cursor.execute("SELECT * FROM bankmain WHERE ACCOUNTNO={}". format(accno))
        results=cursor.fetchall()
        print(results)
    
def withdraw(accno): #function to withdraw money from acccount
    c="y"
    cursor = db.cursor()
    while c=="y":
        wdwlamnt = int(input("Enter amount to be withdrawed"))
        if wdwlamnt<=50000:
            cursor.execute("SELECT ACCOUNTBALANCE FROM bankmain WHERE ACCOUNTNO={}". format (accno))
            results = cursor.fetchall()
            print("Before withdrawal you had ",results[0][0])
            if results[0][0] < wdwlamnt:
                print("Sorry you do not have enough money to withdraw.")
                print("The current balance in your account is ", results[0])
            else:
                cursor.execute("UPDATE bankmain SET ACCOUNTBALANCE={}". format(results[0][0]-wdwlamnt))
                db.commit()
                cursor.execute("SELECT ACCOUNTBALANCE FROM bankmain WHERE ACCOUNTNO={}". format (accno))
                results=cursor.fetchall()

                print("Congratulations on your withdawel your current balance is ",results[0][0])
                c="n"
        else:
            print("Sorry you cannot withdraw more than 50,000 at a time")
            
def deposit(accno): #function to deposit money to account
    c="y"
    cursor=db.cursor()
    while c=="y":
        depamnt=int(input("Enter amount to be deposited :"))
        cursor.execute("SELECT ACCOUNTBALANCE FROM bankmain WHERE ACCOUNTNO={}". format(accno))
        results = cursor.fetchall()
        print("Before withdrawal you had ",results[0][0])
        if depamnt<=50000:
            cursor.execute("UPDATE bankmain SET ACCOUNTBALANCE={0} WHERE ACCOUNTNO={1}". format(results[0][0]+depamnt,accno))
            db.commit()
            cursor.execute("SELECT ACCOUNTBALANCE FROM bankmain WHERE ACCOUNTNO={}". format(accno))
            results = cursor.fetchall()
            print("Congratulations on your Deposit your new account balance is ",results[0][0])
            c="n"
        else:
            print("Sorry you can only deposit a maximum of 50,000 at a time")

def transfer(accno): #function to transfer money to another bank account
    c="y"
    fo=0
    while c=="y":
        tranto=int(input("Enter account number of bank account to which you would like to transfer money: "))
        f=open("accountno and pin.txt","rb")
        rec=pickle.load(f)
        cursor = db.cursor()
        for r in rec:
            if r[0]==tranto:
                fo=1
                c1="y"
                while c1=="y":
                    tranamnt = int(input("Enter amount to be transfered"))
                    if tranamnt<=500000:
                        cursor.execute("SELECT ACCOUNTBALANCE FROM bankmain WHERE ACCOUNTNO={}". format (accno))
                        results=cursor.fetchall()
                        result=results[0][0]
                        print("Your balance before transfering is ",result)
                        cursor.execute("UPDATE bankmain SET ACCOUNTBALANCE={0} WHERE ACCOUNTNO={1}" . format (result + tranamnt, accno))
                        cursor.execute("SELECT ACCOUNTBALANCE FROM bankmain WHERE ACCOUNTNO={}" . format(tranto))
                        results = cursor.fetchall()
                        cursor.execute("UPDATE bankmain SET ACCOUNTBALANCE={0} WHERE ACCOUNTNO={1}" . format(result + tranamnt, tranto))
                        print("You have succesfully transfered money from ",accno,"to",tranto," an amount of ",tranamnt)
                        cursor.execute("SELECT ACCOUNTBALANCE FROM bankmain WHERE ACCOUNTNO={}". format (accno))
                        results=cursor.fetchall()
                        result=results[0][0]
                        print("Your balance After transfering is ",result)
                        c1="n"
                        c="n"
                    else:
                        print("Sorry you can transfer a  maximum of 5 Lakhs at a time")
            

def changepin(accno):#check
    c = "y "
    fn= open("accountno and pin.txt", "ab+")
    rec=pickle.load(fn)
    while c == "y":
        newpin = int(input("Enter your new PIN: "))
        
        print("\n")
        renewpin = int(input("Enter your PIN once more"))
        print("\n")
        if newpin == renewpin:
            print("Two PINS match!")
            c2 = "n"
            print("\n")
            for i in rec:
                if accno==i[0]:
                    i[1]=newpin
                    print("Congratulations your new PIN is",newpin)
                    fn.close()
        else:
            print("Sorry the two PINS dont match.Please try again.")
            
def closeaccount(accno):
    conf=input("Are you sure you want to delete your acount (Yes/No)")
    if conf.lower()=='yes':
        try:
            print("Money already in your account succesfully withdrawn.")
            cursor.execute("DELETE FROM  bankmain WHERE ACCOUNTNO={}". format(accountno))
            db.commit()
            print("Account deleted Succesfully")
        except:
            db.rollback()
        db.close()


        
    

welcomenote='''-               Welcome to 
                                           __   ____     ________
                                           \ \ / /\ \   / /___  /
                                            \ V /  \ \_/ /   / / 
                                             > <    \   /   / /  
                                            / . \    | |   / /__ 
                                           /_/ \_\   |_|  /_____|
                                                                   Banking solutions PVT LTD.                                                   -
'''
print("---------------------------------------------------------------------------------------------------------------")
print(welcomenote)

a0=input("Would you like to login to our database using your Account number and PIN or Create a new account (login/create an account: ")
if a0.lower()=="login":
    accountno = int(input("Enter your Account number"))
    pin = int(input("Enter your PIN"))
    login(accountno,pin)
if a0.lower()=="create an account":
    f1 = open("accountno and pin.txt","ab+")
    nam = input("Enter Account Holders name.: ")
    print("\n")
    dob = input("Enter Account Holder's Date of birth (YYYY-MM-DD) : ")
    print("\n")
    Gen = input("Enter Gender of Account holder (M/F): ")
    print("\n")
    age =int(input("Enter Account holder's age."))
    print("\n")
    aadharno = input("Enter Account holder's  12 digit Aadhar number")
    print("\n")
    phoneno = input("Enter Account holder's Phone number.")
    print("\n")
    address = input("Enter account holder's Adddress")
    print("\n")
    bankbranch = "Kunnamkulam"
    print("\n")
    pin=int(input("Enter a 4 digit PIN for your Bank Account"))
    pin1=int(input("Enter your pin once more"))
    c2="y"
    while c2=="y":
        if pin == pin1:
            print("Two PINs matching!")
            c2="n"
        else:
            print("Sorry the PINS you typed are not matching try again!")
    ab1 = True
    while ab1 == True:
        balance = int(input(
            "Enter how much money you want to deposit.The maximum amount you can only deposit maximum 50,000 per day"))
        print("\n")
        if balance > 50000:
            print("Sorry you cant deposit that much money at once.You can only deposit maximum 50,000 per day")
        else:
            ab1 = False
    fn= open("accountno and pin.txt", "ab+")#here somewhere
    rec=pickle.load(fn)
    lastaccountno=rec[-1][0]
    newaccountno=lastaccountno+1
    l1=[newaccountno,pin]
    pickle.dump(l1,f1)
    cursor=db.cursor()
    query="INSERT INTO bankmain VALUES ({0},'{1}','{2}','{3}',{4},'{5}','{6}','{7}','{8}',{9})". format(newaccountno,nam,dob,Gen,age,aadharno,phoneno,address,bankbranch,balance)
    cursor.execute(query)
    db.commit()
    cursor.execute("SELECT * FROM bankmain WHERE ACCOUNTNO=%s")%(newaccountno)
    print("Congratulations on creating your Bank account!  :")
    results=cursor.fetchall()
    print(results)
    fn.close()
    
    


print("\n")
curser=db.cursor()
cursor.execute("SELECT * FROM bankmain WHERE ACCOUNTNO={}". format(accountno))
results1=cursor.fetchall()
name=results1[0][1]
dob=results1[0][2]
gender=results1[0][3]
age=results1[0][4]
aadharno=results1[0][5]
phoneno=results1[0][6]
address=results1[0][7]
bankbranchh=results1[0][8]
accbalance=results1[0][9]

c0="y"
while c0=="y":
    print("1.Check your balance")
    print("2.Display your account details")
    print("3.Update any of your account details")
    print("4.Withdraw money")
    print("5.Deposit money")
    print("6.Transfer money")
    print("7.Change my PIN")
    print("8.Close this account")
    print("9.Exit")
    print("\n")
    choice=int(input("Which of these functions would you like to do today! :"))
    if choice==1:
        checkbalance(accountno)
        print("\n")
    if choice==2:
        diplayaccount(accountno)
        print("\n")
    if choice==3:
        updateacc(accountno)
        print("\n")
    if choice==4:
        withdraw(accountno)
        print("\n")
    if choice==5:
        deposit(accountno)
        print("\n")
    if choice==6:
        transfer(accountno)
        print("\n")
    if choice==7:
        changepin(accountno)
        print("\n")
    if choice==8:
        closeaccount(accountno)
        print("\n")
    if choice==9:
        q=input("Are you sure you want to exit.(yes/no):")
        if q.lower()=="yes":
            c0="n"
            print("Thank you for visiting us. Please do come again. : )")
        else:
            c0="y"
