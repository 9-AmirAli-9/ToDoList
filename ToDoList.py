todoitem=[]
tododone=[]

class ToDoList:
    def AddItem(self,name):
        self.name=name
        todoitem.append(self.name)
        tododone.append(False)
        
    def Display(self):
        count=0
        for item in todoitem:
            if tododone[count]==True:
                print((count+1),'.''(D)',todoitem[count])
            else :
                print((count+1),'.''()',todoitem[count])
            count = count +1
            
    def MarkAsDone(self):
        mnum=int(input('what item: '))
        mnum=mnum-1
        tododone[mnum]=True
        
    def EditItem(self):
        enum=int(input('what item you want to edit: '))
        enum = enum-1
        todoitem[enum]=input('enter new describe: ')
        
    def DeletItem(self):
        dnum=int(input('what item: '))
        dnum=dnum-1
        todoitem.pop(dnum)
        
print("---to do list---")
x=0
while (x !='6'):
    print('1. Add ToDo Item')
    print('2. Display ToDo List')
    print('3. Mark Item as Done')
    print('4. Edit ToDo Item')
    print('5. Delet ToDo Item')
    print('6. Exit')
    x=input('Enter your choice: ')
    
    if x=='1' :
        name=input('enter your item description: ')
        todolist1=ToDoList()
        todolist1.AddItem(name)
    elif x=='2':
        todolist1.Display()
    elif x=='3':
        todolist1.MarkAsDone()
    elif x=='4':
        todolist1.EditItem()
    elif x=='5':
        todolist1.DeletItem()
    elif x=='6':
        print('6')

