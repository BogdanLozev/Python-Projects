# create an regions

regions = {
	'Severna Bulgaria': 'SB', 
	'Yujna Bulgaria': 'YB', 
	'Zapadna Bulgaria': 'ZB', 
	'Iztochna Bulgaria': 'IB'
}

# create a basic set of regions and some cities in them: 

cities = {
	'SB': 'Gabrovo',
	'YB': 'Haskovo',
	'ZB': 'Sofia',
	'IB': 'Burgaz'
}

# add some more cities

cities['SB'] = 'Silistra'
cities['YB'] = 'Stara Zagora'

#print out some cities

print '-' * 10
print "SB has: ", cities['SB']
print "YB has: ", cities['YB']

#print out some regions
print '-' * 10
print "Zapadna Bulgaria abbreviation is: ", regions ['Zapadna Bulgaria']
print "Iztochna Bulgaria abbreviation is: ", regions ['Iztochna Bulgaria']

#do it by using the region then cities directly

print '-' * 10
print "Severna Bulgaria has: ", cities [regions['Severna Bulgaria']]
print "Yujna Bulgaria has: ", cities [regions['Yujna Bulgaria']]

# print every region abbreviation

print '-' * 10
for region, abbrev in regions.items(): 
	print "%s is abbreviated %s" % (region, abbrev)


#print every city in region
print '-' * 10
for abbrev, city in cities.items(): 
	print "%s has the city %s" % (abbrev, city)


# now do both at the same time
print '-' * 10
for region, abbrev in regions.items():
    print "%s region is abbreviated %s and has city %s" % (
        region, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by region that might not be there
region = regions.get('Texas')

if not region:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the region 'TX' is: %s" % city