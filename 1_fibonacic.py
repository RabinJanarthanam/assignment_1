num=int(input("enter the number:"))
n1,n2=1,1
print("fibonacci series:",n1,n2,end=" ")
for i in range(2,num):
    n3=n2+n1
    n1=n2
    n2=n3
    print(n3,end=" ")
print()
