#prgrm to input bank details
import pickle
record=[]

while True:
    
    account_no=int(input("enter account number"))
   
    pin=int(input("enter PIN"))
    
    data1=[account_no,pin]
    record.append(data1)
    c=input("any  more bank ids  (Y/N) ? : " )
    
    if c.upper() == 'N': break

f=open("accountno and pin.txt","wb")
pickle.dump(record,f)
print("record added")
f.close()
          
        
