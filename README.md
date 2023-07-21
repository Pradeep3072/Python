python_basic
#print given number one by one

num = int(input("enter input: ")) while(num>0): digit = num % 10 num = num // 10 print(digit)

#reverse a string withot steping string="pages" new_string="" for i in range(len(string)-1,-1,-1): new_string+=string[i] print(new_string)

#find given number is perfect number or not n=3 div=0 for i in range (1,n): if (n%i == 0 ): div+=i if (div==n): print("perfect number")

else : print("not a perfect number") #common divisors of two different number n1=18 n2=9 if (n1>n2): endpoint=n1 else: endpoint=n2 for i in range (2,endpoint): if((n1%i == 0) and (n2%i == 0)): print (i)

Number patterns
rows = int(input("Enter the number of rows: "))
for i in range(1, rows+1):
for j in range(1, i + 1):
print(j, end=' ')
print("")

rows = int(input("Enter the number of rows: "))
for i in range(1, rows+1):
for j in range(1, i + 1):
print(i, end=' ')
print("") #patterns n=int(input("Enter the number of rows: ")) for i in range(0,n): for j in range(n-i): print("",end=' ') print( ) #pattern (I) n=int(input()) for i in range(n): for j in range(n): if ((i==0) or (i==n-1)): print("",end=" ") elif (n//2 == j): print("*",end=" ") else: print(" ",end=" ") print()

#pattern(A)

n=int(input()) for i in range(n): for j in range(n-2): if i==0 and (j==0 or j==(n-2-1)): print(" ",end=" ")

        elif j==0 or j==(n-2-1):
            print("*",end=" ")
        
        elif i==0 or i==(n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
 print()
#multiplication of two numbers without multiplication operator n1=int(input()) n2=int(input()) prod=0 for i in range(1,n1+1): prod+=n2 print(prod)

#fibnocci series def fibnocci_series(num):

a=0
b=1
c=0

for i in range(0,num+1):
   print(c)
   c=a+b
   b=a
   a=c
fibnocci_series(6) #count of strings strings=seed for string in strings: strings.count(string) print(string,strings.count(string),sep="",end=' ')

output:seed s1 e2 e2 d1

#split line into words string=input() for i in string: if i==' ': print() else: print(i,end="")

#sum of cosecutive numbers till given number n=int(input()) def sum_n_num(num1): if num1==0: return 0 return num1 + sum_n_num(num1-1) print(sum_n_num(n))

#factorial of number num1=int(input()) def fact(num1): if num1<=1 : return 1

return num1 * fact(num1-1) print(fact(num1))

#square of number num1=int(input()) def square_num(num1): if num1==1: return 1 return num1 * num1 print(square_num(num1))

#sorting list without sort method n=list(input()) for i in range(0,len(n)): for j in range(i,len(n)): if n[i]>n[j]: temp=n[i] n[i]=n[j] n[j]=temp print(n)
