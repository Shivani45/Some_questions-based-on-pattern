def halk_k(n):
    for i in range(0,n):
        print(" "*(n-i-1)+"* "*(i+1))
k=int(input("Enter the number of rows you want"))
halk_k(k)
# in another way by inbuilt function(best nd esy)
for i in range(0,k):
    print(("* "*(i+1)).center(2*k-1))


        
