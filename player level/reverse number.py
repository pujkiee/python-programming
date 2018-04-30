num=int(input("enter the number:\n"))
reverse=0
while num>0:
reminder=num%10
reverse=(reverse*10)+reminder
num=num/10
print("\n reverse is=%d",%reverse)
