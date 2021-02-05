def computepay(h,r):
    h = float(hrs);
    r = float(rat);
    if h <= 40:
        return(h * r);
    else:
        return(40 * r + (h-40) * 1.5 * r);

hrs = input("Enter Hours:")
rat = input("Enter Rate:")
p = computepay(hrs,rat)
print("Pay",p)