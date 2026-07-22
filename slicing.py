# SLICING - Extracting a specific chunk or part from a list or string
#           indexing[] or slice[]
#           [start:stop:step]

name = "Agostino Scholes"
first_name = name[0:3]
last_name = name[7:13]
funky_name = name[0:8:2]
reversed_name = name[::-1]
print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7, -4)
print(website[slice])
print(website2[slice])