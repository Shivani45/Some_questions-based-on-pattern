#for full pyramid(double rows)
k=int(input("Enter the number"))
str=""
strrev=""
for i in range(0,k):
    if(i<k-1):
       strrev =strrev+("* "*(i+1)).center(2*k-1)+"\n"
    if(i==k-1):
        str=str+("* "*(i+1)).center(2*k-1)
print(strrev+str+strrev[::-1])
print("\n"*2)
#for inputing total rows
#supose k is the total rows
str2=""
strrev2=""
for i in range(0,k):
    if(i<k//2):
        strrev2 =strrev2+("* "*(i+1)).center(2*k-1)+"\n"
    if(i==k//2):
        str2 =str2+("* "*(i+1)).center(2*k-1)
print(strrev2+str2+strrev2[::-1])
