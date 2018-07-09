z= raw_input()
y= int(z)
if y<0:
    print "Invalid"
elif y>0:
    x = y % 2
    if x > 0:
        print "Odd"
    else:
        print "Even"
