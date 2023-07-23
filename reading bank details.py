import pickle
f=open("accountno and pin.txt", "rb")
stud_rec=pickle.load(f)
for R in stud_rec:
    
    
    print(R)

f.close()    
