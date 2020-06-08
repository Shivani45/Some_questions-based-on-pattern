#hollow sq
n=int(input("Enter the side of a sqaure"))
for i in range(0,n):
    if i==0 or i==n-1:
        print("*"*n)
    else:
        print("*"+(n-2)*" "+"*")
#hollow rectangle
col=int(input("Enter the columns"))
row=int(input("Enter the rows"))
for i in range(0,row):
    if(i==0 or i==row-1):
        print("*"*col)
    else:
        print("*"+" "*(col-2)+"*")
