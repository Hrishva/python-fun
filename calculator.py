def calculate(num1,num2,operate):
	
	plus_list=["+","plus","add","addition","ad"]
	minus_list=["-","minus","subtract"]
	into_list=["*","into","multiply","multiplication","×"]
	by_list=["/","divide","by","division","÷"]
	power_list=["**","power","to the"]
	factorial_list=["!","fact","factorial","fac"]
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
	if operate in factorial_list:
		facto=1
		for x in range(1,num1+1):
			facto=facto*x
		print(facto)
		
		
		
calculate(4,4,"×")
		
   
       
    
    
                
    
    