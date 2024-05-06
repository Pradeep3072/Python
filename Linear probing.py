def hash_table(l, arr):
    for i in l:
        location=(2*i+3)%10
        if arr[location]==-1:
            arr[location]=i
        else:
            for j in range(len(arr)):
                location=(i+j)%10
                if arr[location] == -1:
                    arr[location] = i
                    break
def display(arr):
    for i in range(len(arr)):
        if arr[i]==-1:
            print(f"[{i}]=")
        else:
            print(f"[{i}]={arr[i]}")


n = int(input("Enter no. of elements: "))
l = list(map(int, input("Enter Elements: ").split()))
arr = [-1] * 10
hash_table(l, arr)
display(arr)





