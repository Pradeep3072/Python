def hash_function1(key,tsize):
    return((2*key)+3)%tsize
def hash_function2(key,tsize):
    return (key+1)%tsize
def insert_double_hashing(hash_table,key,table_size):
    index=hash_function1(key,table_size)
    step=hash_function2(key,table_size)
    while hash_table[index] is not None:
        index=(index+step)%table_size
    hash_table[index]=key
table_size=int(input("enter the table size : "))
n=int(input("enter the number of elements : "))
arr=[]
for _ in range(n):
    arr.append(int(input()))
hash_table=None*table_size
for key in arr:
    insert_double_hashing(hash_table,key,table_size)
print("**********DOUBLE HASHING***********")
for i in range(table_size):
    print("{}:{}".format(i,hash_table[i] if hash_table[i] is not None else "None"))
