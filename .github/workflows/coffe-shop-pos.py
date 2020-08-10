import os

clr = "clear"
os.system(clr)

products = [
	{"ProductName":"Nescafe", "Price":12},
	{"ProductName":"Kopiko brown", "Price":14},
	{"ProductName":"Coffe Blanca", "Price":12},
	{"ProductName":"Coffemate", "Price":12},
	{"ProductName":"Jims 5in1 coffe ", "Price":15}
]

pickupTimes = [
	"9:00 AM to 10:00 AM",
	"11:00 AM to 12:00 PM",
	"12:00 PM to 1:00 PM",
	"1:00 PM to 2:00 PM",
	"2:00 PM to 3:00 PM"
]

orders = []

print("\nWelcome to My Coffe Shop\n" + "\nCoded:Mark Anthony Gabo\n")
name = input("What's your name? > ")
credNum = input("Credit Card Number > ")

def orderMenu():
	os.system(clr)
	print("""
Welcome {}, Choose your Order!

Menu Item:                   Price
[1] Nescafe                  Php 12.00
[2] Kopiko brown             Php 14.00
[3] Coffe Blanca             Php 12.00
[4] Coffemate                Php 12.00
[5] Jims 5in1 coffe          Php 15.00 
[6] Back
""".format(name))

	while True:
		try:
			choiceNum = int(input("Select your order > "))
			if(choiceNum == ""):
				print("Choice should not be blank.")
				pass
			elif(int(choiceNum) > 6):
				print("Choose from 1 to 6 only")
				pass
			else:
				break
		except ValueError:
			print("Choose from 1 to 6")
			pass
		
	if(choiceNum == 6):
		if(len(orders) == 0):
			exit()
		else:
			receipt()
		
	while True:
		try:
			quan = int(input("Quantity > "))
			if(type(quan) != int):
				print("Enter a number only!")
				pass
			else:
				break
		except ValueError:
			print("Enter a number only")
			pass
	
	orderName = products[choiceNum - 1]['ProductName']
	orderPrice = products[choiceNum - 1]['Price']
	orderTotal = orderPrice*quan
	
	orders.append({"ItemName":orderName, "Price":orderPrice, "Quantity":quan, "Total":orderTotal})
	
	if(len(orders) < 3):
		newOrd = input("Would you like to add another one? [y/N] > ")
		if(newOrd.lower() == "y"):
			orderMenu()
		else:
			receipt()
	else:
		receipt()

def receipt():
	os.system(clr)
	while True:
		print("""
		
What is your preferred pickup time?
[1] 9:00 AM to 10:00 A
[2] 11:00 AM to 12:00 PM
[3] 12:00 PM to 1:00 PM
[4] 1:00 PM to 2:00 PM
[5] 2:00 PM to 3:00 PM
	
	""")
	
		try:
			pickupTime = int(input("Select > "))
			if(pickupTime < 6 and pickupTime != ""):
				pickup = pickupTimes[pickupTime - 1]
				break
			else:
				print("Enter 1 - 5 only!")
				continue
		except ValueError:
			print("Enter 1 - 5 only!")
			continue
	
	os.system(clr)
	totalReceipt = 0
	print("""
----------- ORDER SUMMARY -----------
""")
	print("Product{}Price{}Qty{}Total".format(" "*19, " "*3, " "*3, " "*3))
	for x in orders:
		spc1 = " "*(25-len(x['ItemName']))
		spc2 = " "*(7-len(str(x['Price'])))
		spc3 = " "*(5-len(str(x['Quantity'])))
		print("{} {} {} {}".format(x['ItemName'] + spc1, str(x['Price']) + spc2, str(x['Quantity']) + spc3, x['Total']))
		totalReceipt += x['Total']
	print("\nCustomer Name: {}".format(name))
	print("Deliver by: {}".format(pickup))
	print("Order Total: {}".format(str(totalReceipt)))
	print("Credit to: {}\n".format(str(credNum)))
	comp = input("Confirm Transaction? [y/N] > ")
	if(comp.lower() == "y"):
		print("Thank you for your order!")
		exit()
	else:
		print("Order Cancelled.")
		exit()
		
while True:
	if(name.strip() == ""):
		os.system(clr)
		print("Name shouldn't be blank!")
		name = input("What's your name? > ")
		
	if(credNum.strip() == ""):
		os.system(clr)
		print("Credit Number shouldn't be blank!")
		credNum = input("Credit Card Number > ")
	else:
		orderMenu()
		
