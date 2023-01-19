# def calculate(d):
#     q = 3.14
#     z = q * (d ** 2)
#     print(z)
# calculate(5)

# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
my_trip_miles = 55


# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)
# my_trip_km = my_trip_miles *1.6
# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(my_trip_km))


def convert_distance(miles):
    km = miles * 1.6 
    return km
result = convert_distance(55)
print("The distance in Kilometers is " + str(result))
print("The round-trip in Kilometers is " + str(result*2))
