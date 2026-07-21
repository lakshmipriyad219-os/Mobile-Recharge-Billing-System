def customer():
    name = input("Enter customer name: ")
    return name


def mobile():
    while True:
        number = input("Enter mobile number: ")

        if len(number) == 10:
            return number
        else:
            print("Enter valid 10 digit mobile number")


def recharge():
    while True:
        plan = int(input("Enter plan (1/2/3): "))

        if plan == 1 or plan == 2 or plan == 3:
            break
        else:
            print("Invalid plan")

    if plan == 1:
        price = 199
    elif plan == 2:
        price = 399
    else:
        price = 599

    gst = (price * 18) / 100
    total = price + gst

    cashback = 0
    if total > 500:
        cashback = 50

    final = total - cashback

    return plan, price, gst, total, cashback, final


name = customer()
number = mobile()

plan, price, gst, total, cashback, final = recharge()

print("\n----- Recharge Receipt -----")
print("Customer Name =", name)
print("Mobile Number =", number)
print("Plan =", plan)
print("Price =", price)
print("GST =", gst)
print("Total Bill =", total)
print("Cashback =", cashback)
print("Final Bill =", final)
