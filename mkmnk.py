import pickle
f=open("accountno and pin.txt", "rb")
rec=pickle.load(f)
lastno=rec[-1][0]
newno=lastno+1
print(lastno,newno)
