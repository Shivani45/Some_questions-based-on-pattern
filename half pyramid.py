def half_pyramid(n):
    str=""
    for i in range(0,n):
        if(i<n-1):
           str=str+" "*(n-i-1)+"*"*(2*i+1)+" "*(n-i-1)+"\n"
        else:
            str=str+" "*(n-i-1)+"*"*(2*i+1)+" "*(n-i-1)
    print(str+"\n"+str[::-1])

x=int(input("Enter Number of rows"))
half_pyramid(x)
