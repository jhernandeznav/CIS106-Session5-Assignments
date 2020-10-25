# program for activity 2
def fun_get_up(widget):
    if widget == "A":
        up = 10.00
    else:
        up = 20.00
    return up


widget = input("Enter widget(A or B)")
qty = input("Enter quantity ordered:")

# input phase
up = fun_get_up(widget)


ext_price = float(qty) * float(up)

# output phase
print("Unit Price: $", up)
print("Extended price: $", ext_price)
