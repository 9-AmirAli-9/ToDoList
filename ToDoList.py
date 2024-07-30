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
        num=int(input('what item: '))
        num=num-1
        tododone[num]=True
        
    def EditItem(self):
        num=int(input('what item you want to edit: '))
        num = num-1
        todoitem[num]=input('enter new describe: ')
        
    def DeletItem(self):
        num=int(input('what item: '))
        num=num-1
        todoitem.pop(num)
        
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
        i1=ToDoList()
        i1.AddItem(name)
    elif x=='2':
        i1.Display()
    elif x=='3':
        i1.MarkAsDone()
    elif x=='4':
        i1.EditItem()
    elif x=='5':
        i1.DeletItem()
    elif x=='6':
        print('6')

