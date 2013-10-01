meal = float(raw_input("Enter the cost of your meal before tax"))
tax = float(raw_input("Enter the tax rate"))
tip = float(raw_input("Enter the tip rate"))
#tax_value = 
meal_with_tax = meal + tax
tip_value = meal_with_tax * tip
total = meal_with_tax + tip_value

print "the base cost of your meal was %r" % (meal)
print "you need to pay $%r for tax" % (tax)
print "tipping at a rate of %r, you should leave $%r for a tip" %(tip, tip_value)
print "The Grand total of your meal is $%r." % (total)

#meal = meal + meal * tax

print("%.2f" % total)