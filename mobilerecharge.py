customer_name = input("Enter a customer name: ")
mobile_number = input("Enter a mobile number: ")
plan = int(input("Enter plan(1/2/3): "))

if(plan == 1):
    price = 199
    print("price = 199")

elif(plan == 2):
    price = 399
    print("price = 399")

elif(plan == 3):
    price = 599
    print("price = 599")

else:
    print("Invalid plan")


gst = (price * 18) / 100
print("Gst = ", gst)
total_bill = price + gst
print("Total bill =  ", total_bill)

Cashback = 0
if(total_bill > 500):
    print("Cashback =  50")

else:
    print("Cashback = 0")

final_bill = total_bill - Cashback
print("final bill =  ", final_bill)


print("customer name =  ", customer_name)
print("mobile number =  ", mobile_number)
print("plan = ", plan)
print("Price =", price)
print("Gst =", gst)
print("Total bill =", total_bill)
print("Cashback =", Cashback)
print("Final bill =", final_bill)