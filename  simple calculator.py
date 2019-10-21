num1=float(input("enter a number: "))

num2=float(input("enter another number: "))

operate=input("Give any math's operator to perform calculation: ").lower().replace(' ','')

plus_list=["+","plus","add","addition","ad"]

minus_list=["-","minus","subtract","subtraction","sub"]

into_list=["*","into","multiply","multiplication","in"]

by_list=["/","divide","by","division","devision","divition","devition"]

power_list=["**","power","to the"]

if operate in plus_list:
	print(num1+num2)
	
if operate in minus_list:
	print(num1-num2)

if operate in into_list:
	print(num1*num2)

if operate in by_list:
	print(num1/num2)

if operate in power_list:
	print(num1**num2)


