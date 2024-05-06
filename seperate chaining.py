"""li=list(map(int,input().split()))
m=int(input())
v=[]
for i in range(m):
    v.append([i,[]])
for i in li:
    n=((2*i)+3)%10
    if n<m:
        v[n][1].append(i)
for i in v:
    print(i)"""

#seperate chaining in linear probing

"""class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

a = list(map(int, input().split()))
m = int(input())
s = [LinkedList() for i in range(m)]

for i in a:
    b = (2 * i) % m
    if b < m:
        s[b].append(i)

for i, linked_list in enumerate(s):
    print(f"List {i}: ", end="")
    linked_list.display()"""

9363314889