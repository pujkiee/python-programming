def ispower(n,base):
    if n==base:
        return yes
    if base ==1:
        return no
    temp=base
    while (temp<=n):
        if temp ==n:
            return yes
        temp*= base
     return no
