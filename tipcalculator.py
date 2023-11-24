print(" Hello, Welcome to the tip bill calculator using python")
bill = float(input("what was the total bill ? $"))
tip = int(input("How much would you like to tip ? 10 , 12 , 15? "))
people = int(input("how many people would like to split the bill ?"))
total_tip = tip/100 * bill + bill
total_bill = total_tip / people
total_bill = round(total_bill, 2)
total_bill= round(total_bill,2)
print(f"Each person should pay ${total_bill}")
#output :
Hello, Welcome to the tip bill calculator using python
what was the total bill ? $250
How much would you like to tip ? 10 , 12 , 15? 10
how many people would like to split the bill ?5
Each person should pay $55.0
