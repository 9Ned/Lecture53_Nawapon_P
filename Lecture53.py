def vatCal():
    totalPrice = int(input("Please enter price:"))
    result = totalPrice +(totalPrice*7/100)
    return result

print(vatCal())
