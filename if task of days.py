mylist=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]

user_input=int(input("enter day name from 0 to 6 for sunday to monday respectively: "))

if user_input<=6 and user_input>=0:
	print(mylist[user_input])