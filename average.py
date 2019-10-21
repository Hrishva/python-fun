inp=int(input("How many numbers you want to find average of: "))
s=0
x=1
while x<=inp:
	a= int(input("Enter number: "))
	s=s+a
	x+=1
ag=s/inp
print("Average of your numbers is ",ag,"." )
	