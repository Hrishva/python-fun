inp=int(input("enter no. of rows: "))
r=1
while r<=inp:
	print(" "*(inp-r),end="")
	f="*"*r
	print(f*2)
	
	r+=1
i=0
while i<=inp:

	print(" "*i,end="")
	u="*"*(inp-i)
	print(u*2)
	i+=1