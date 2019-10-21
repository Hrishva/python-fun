name1=input("Player 1 name: ")
name2=input("Player 2 name: ")
import getpass
w1=name1+" won!"
w2=name2+" won!"
p1=0
p2=0
for m in range(1,4):
	inp1=input("move1: ")
	inp2=input("move2: ")
	
	if inp1=="stone"and inp2=="scissor":
		print(w1)
		p1+=1
	if inp1=="stone"and inp2=="paper":
		print(w2)
		p2+=1
	if inp1=="scissor"and inp2=="stone":
		print(w2)
		p2+=1
	if inp1=="scissor"and inp2=="paper":
		print(w1)
		p1+=1
	if inp1=="paper"and inp2=="stone":
		print(w1)
		p1+=1
	if inp1=="paper"and inp2=="scissor":
		print(w2)
		p2+=1
	if inp1==inp2:
		print("round tied.")
	elif p1==2:
		break
	elif p2==2:
		break
if p1==2:
	print(name1," won best of 3.")
	
elif p2==2:
	print(name2," won best of 3.")
else:
	print("best of 3 tied.")