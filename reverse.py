n=int(input("enter number"))
s=0
x=n
while(x>0):
    r=x%10
    s=s*10+r
    x=x//10
print("reverse of {} is {}".format(n,s))
