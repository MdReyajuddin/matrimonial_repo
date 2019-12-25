import pickle
class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def display(self):
        print(self.eno,"\t",self.ename,"\t",self.esal,"\t",self.eaddr)

with open("emp.dat","wb") as f:
    e=Employee(100,'reyaj',1000,'bangalore')
    pickle.dump(e,f)
    print('pickle complete..')
with open("emp.dat","rb") as f:
    obj=pickle.load(f)
    print('Employee Info After Unpickling..')
    obj.display()