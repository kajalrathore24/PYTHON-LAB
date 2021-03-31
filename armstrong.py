n=int(input("enter no."))
x=n
s=0
c=len(str(n))
while(x>0):
    r=x%10
    s=s+r**c
    x=x//10
if(n==s):
    print("armstrong")
else:
    print("not")
