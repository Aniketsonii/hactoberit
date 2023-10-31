class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class RoleHierarchy:
    def __init__(self):
        self.head = None

    def PrintList(self):
        if self.head is None:
            print("List is Empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data, ">>", end=" ")
                n = n.ref

    def AddStart(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def AddEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def AddAfter(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("Role is not present in List")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def DeleteByValue(self, x):
        if self.head is None:
            print("Can't delete List is empty!")
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("Role is not present!")
        else:
            n.ref = n.ref.ref


def AddUser(x):

    arr = []
    for i in range(x):
        name = input("Enter User Name: ")
        role = input("Enter role: ")
        arr.append(str(name+" - "+role))
    return arr

def DelUser(x):
    if x in arr:
        arr.remove(x)
        print("Deleted User ",x)
    else:
        print("Enter Correct Role")
        
def DisplayUser(arr):
    for i in arr:
        print(i)

LinkedList = RoleHierarchy()

Root_Role = input("Enter root role name: ")
LinkedList.AddStart(Root_Role)
while True:
    print("\nOperations\n  1. Add Sub Role\n  2. Display Roles\n  3. Delete Role\n  4. Add User\n  5. Delete User\n  6. Display Users\n  7. Quit\n")
    
    OP = int(input("Operation to be performed : "))
    if OP == 7:
        break
    elif OP == 1:
        Role_Name = input("Enter sub role name : ")
        Reporting_Role = input("Enter reporting to role name : ")
        LinkedList.AddEnd(Role_Name)
    elif OP == 2:
        LinkedList.PrintList()
        print()
    elif OP == 3:
        Del_Role = input("Enter the Role to be Deleted : ")
        Transfer_role = input("Enter the Role to be Transferred : ")
        LinkedList.DeleteByValue(Del_Role)
    elif OP == 4:
        No_Of_User = int(input("How many Users Do you want to add : "))
        arr = AddUser(No_Of_User)
    elif OP == 5:
        Del_User = input("Enter User to be Deleted with Role in 'name - role' format")
        DelUser(Del_User)
    elif OP == 6:
        DisplayUser(arr)
    else:
        print("Enter Correct Operation Number")
