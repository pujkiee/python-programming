a=[]
b=raw_input()
a=b.split("")
for i in range(int(a[0])+1,int(a[1])):
    if(i % 2 != 0):
        print i
