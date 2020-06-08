k=int(input("Enter the rows"))
str=""
strrev=""
for i in range(k,0,-1):
    if(i>1):
        str=str+("* "*(i)).center(2*k+1)+"\n"
    if(i==1):
        strrev=strrev+("* "*(i)).center(2*k+1)
        
print(str+strrev+str[::-1])
