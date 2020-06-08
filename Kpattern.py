#k-shaped pattern
n=int(input("Enter the number of rows"))
str=""
strrev=""
for i in range(n//2+1,0,-1):
    if(i>1):
        str=str+"*"+" "*(i)+"*"+"\n"
    if(i==1):
        strrev=strrev+"*"+" "*(i)+"*"
print(str+strrev+str[::-1])
    
