n=int(input("enter the no. of line"))
c=3
for i in range(1,n+1):
	for k in range(1,c+1):
		print(" ",end=" ")
	for j in range(1,i+1):
		print("*",end=" ")
	print()
	c-=1
