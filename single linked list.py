# linear data structure


class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self, head, temp):
        self.head = None
        self.temp = None

    def create(self):
        size = int(input("enter the size : "))
        for i in range(size):
            data = int(input("enter the element : "))
            newnode = node(data)
            newnode.next = None

            if self.head == None:
                self.head = newnode
                self.temp = newnode
            else:
                self.temp.next = newnode
                self.temp = newnode

    def display(self):
        self.temp = self.head
        while self.temp != None:
            print(self.temp.data, end=" ")
            self.temp = self.temp.next

    def insertfront(self):
        data = int(input("enter the element to be updated : "))
        newnode = node(data)
        newnode.next = None
        if self.head == None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def insertend(self):
        data = int(input("enter the element to be updated : "))
        newnode = node(data)
        newnode.next = None
        if self.head == None:
            self.head = newnode
        else:
            while self.temp.next != None:
                self.temp = self.temp.next
            self.temp.next = newnode
            self.temp = newnode

    def insertmiddle(self):
        pos = int(input("enter position : "))
        data = int(input("Enter thr element to be added in middle : "))
        newnode = node(data)
        i = 1
        self.temp = self.head
        while i < pos:
            self.temp = self.temp.next
            i = i + 1
        newnode.next = self.temp.next
        self.temp.next = newnode

    def deletefront(self):
        self.temp = self.head
        self.head = self.head.next
        del self.temp

    def deleteend(self):
        self.temp = self.head
        prev = None
        while self.temp.next != None:
            prev = self.temp
            self.temp = self.temp.next
        if self.temp == self.head:
            self.head = None
        else:
            prev.next = None
        del self.temp

    def deletemiddle(self):
        self.temp = self.head
        pos = int(input("Enter the position to be deleted at middle : "))
        i = 1
        nextnode = None
        while i < pos:
            self.temp = self.temp.next
            i += 1
        nextnode = self.temp.next
        self.temp.next = nextnode.next
        del nextnode

    def count(self):
        self.temp = self.head
        count=0
        while self.temp!=None:
            count+=1
            self.temp=self.temp.next


obj = linkedlist(None, None)
obj.create()
obj.deletemiddle()
obj.display()
"""

"""class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
        self.temp=None
    def create(self,data):

            newnode=node(data)
            newnode.next=None
            if self.head==None:
                self.head=newnode
                self.temp=newnode
            else:
                self.temp.next=newnode
                self.temp=newnode

    def consecutive(self):
        cou=0
        v=[]
        self.temp=self.head
        while self.temp!=None:

            v1=self.temp.data
            v.append(v1)
            self.temp = self.temp.next
        for i in range(0,len(v)-1,2):

            if v[i]+1==v[i+1] or v[i]-1==v[i+1]:
                print("Yes")
            else:
                print("no")

        print(v)



    def display(self):
        self.temp=self.head
        while self.temp!=None:
            print(self.temp.data,end=" ")
            self.temp=self.temp.next

obj=sll()
n=[4,5,-2,-3,11,10,5,6,20]
for i in n:
    obj.create(i)
obj.consecutive()
obj.display()"""


