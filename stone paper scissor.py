name1=input("Player 1 name: ")
name2=input("Player 2 name: ")
import getpass
inp1=getpass.getpass("move1: ")
inp2=getpass.getpass("move2: ")
if inp1=="stone" and inp2=="scissor":
	print(name1,"won!")
elif inp1=="stone" and inp2=="paper":
	print(name2,"won!")
elif inp1=="scissor" and inp2=="stone":
	print(name2,"won!")
elif inp1=="scissor" and inp2=="paper":
	print(name1,"won!")
elif inp1=="paper" and inp2=="stone":
	print(name1,"won!")
elif inp1=="paper" and inp2=="scissor":
	print(name2,"won!")
elif inp1==inp2:
	print("Game tie!")
else:
	print("invalid move!")