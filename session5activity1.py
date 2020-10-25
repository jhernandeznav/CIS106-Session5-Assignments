# program for activity one

def get_ep(qty, up):
    ep = qty * up
    return ep


# main
print("Enter quantity ordered")
qty = float(input())
print("Enter unit price")
up = float(input())
ep = get_ep(qty, up)
tax = ep * 0.07
if ep > 100:
    sp = 0.0
else:
    sp = ep * 0.1
total = ep + sp + tax
print("Quantity Ordered: " + str(qty))
print("Unit Price: $" + str(up))
print("Extended Price: $" + str(ep))
print("Tax Amount: $" + str(tax))
print("Shipping: $" + str(sp))
print("Total Order: $" + str(total))
