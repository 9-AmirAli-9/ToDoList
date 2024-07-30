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
                print(f'{(count+1)}. (D) {todoitem[count]}')
            else :
                print(f"{str(count+1)}. () {todoitem[count]}")
            count = count +1
            
    def MarkAsDone(self):
        mnum=int(input('which item do you want mark as done: '))
        mnum=mnum-1
        tododone[mnum]=True
        
    def EditItem(self):
        enum=int(input('which item do you want to edit: '))
        enum = enum-1
        todoitem[enum]=input('enter new description: ')
        
    def DeleteItem(self):
        dnum=int(input('which item do you want to delete: '))
        dnum=dnum-1
        todoitem.pop(dnum)
        
print("---to do list---")
choice=0
while (choice !='6'):
    print('1. Add ToDo Item')
    print('2. Display ToDo List')
    print('3. Mark Item as Done')
    print('4. Edit ToDo Item')
    print('5. Delete ToDo Item')
    print('6. Exit')
    choice=input('Enter your choice: ')
    
    if choice=='1' :
        name=input('enter your item description: ')
        todolist1=ToDoList()
        todolist1.AddItem(name)
    elif choice=='2':
        todolist1.Display()
    elif choice=='3':
        todolist1.MarkAsDone()
    elif choice=='4':
        todolist1.EditItem()
    elif choice=='5':
        todolist1.DeleteItem()
    elif choice=='6':
        print('6')

