n=input()
if(n>1 and n<=1000):
   for i in range(2,n):
        if(n%i)==0:
            print("no")
    else:
        print("yes")
else:
    print("no")
