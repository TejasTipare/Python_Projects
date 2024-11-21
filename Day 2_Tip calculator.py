print("Welcome to the Tip calculator!")
Bill = float(input("What was the total bill?\n$"))
Tip = int(input("How much Tip you would like to give? 10, 12, or 15?\n"))
People = int(input("How many people to split the bill?\n"))
Tip_Cal = round(Bill* float(Tip/100),2)
Amount = Bill + Tip_Cal
Bill_Cal = round(Amount/People,2)
print(f"Each person should pay:{Bill_Cal}")
