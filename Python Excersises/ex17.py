def cheese_and_crackers (cheese_count, boxes_of_crackers): 
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that is enough for nothing"
	print "Get a hooker.\n"

print "We can just give the function nummbers directly"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script: "
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even math inside too: "
cheese_and_crackers(10 + 20, 5 + 5)

print "And we also can combine the two, variables and math: "
cheese_and_crackers(amount_of_cheese + 230, amount_of_crackers + 420)