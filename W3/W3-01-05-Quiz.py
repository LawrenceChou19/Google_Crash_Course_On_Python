# def print_prime_factors(number):
#       # Start with two, which is the first prime
#   factor = 2
#   # Keep going until the factor is larger than the number
#   while factor <= number:
#     # Check if factor is a divisor of number
#     if number % factor == 0:
#       # If it is, print it and divide the original number
#       print(factor)
#       number = number / factor
#       print(number)
#     else:
#       # If it's not, increment the factor by one
#       factor += 1
#   return "Done"

# print_prime_factors(100)
# # Should print 2,2,5,5
# # DO NOT DELETE THIS COMMENT


# def is_power_of_two(n):
#       # Check if the number can be divided by two without a remainder
#   while n % 2 == 0:
#     if n == 0:
#         break
#     else:
#       n = n / 2
#   # If after dividing by two the number is 1, it's a power of two
#   if n == 1:
#     return True
#   return False
  

# print(is_power_of_two(0)) # Should be False
# print(is_power_of_two(1)) # Should be True
# print(is_power_of_two(8)) # Should be True
# print(is_power_of_two(9)) # Should be False

# def sum_divisors(n):
#   sum = 0
#   div = 1

#   while div<n and n>1:
#     if n % div ==0:
#       sum = sum+div
#       div+=1
#     else:
#       div+=1      
 
#   # Return the sum of all divisors of n, not including n
#   return sum  

# print(sum_divisors(0))
# # 0
# print(sum_divisors(3)) # Should sum of 1
# # 1
# print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# # 55
# print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# # 114

# def multiplication_table(number):
#     	# Initialize the starting point of the multiplication table
# 	multiplier = 1
# 	# Only want to loop through 5
# 	while multiplier <= 5:
# 		result = multiplier * number 
# 		# What is the additional condition to exit out of the loop?
# 		if result>25 :
# 			break
# 		print(str(number) + "x" + str(multiplier) + "=" + str(result))
# 		# Increment the variable for the loop
# 		multiplier += 1

# multiplication_table(3) 
# # Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

# multiplication_table(5) 
# # Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

# multiplication_table(8)	
# # Should print: 8x1=8 8x2=16 8x3=24

def factorial(n):
    result = 1
    for x in range(1,n+1):
        result = result * x # 1*1=1 1*2=2 2*3=6 6*4=24 24*5=120
    return result

for n in range(0,10):
    print(n, factorial(n))
    
for x in range(1,11):
      print(x**3)

for x in range (0,100):
    if x%7==0:
        print(x)
i = 0
while 100> i:
    if i > 100:
      break
    else:
      if i%7==0:
        print(i)
    i+=1

def retry(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
      break  
    else:
      print("Attempt " + str(n) + " failed")

print(retry(create_user, 3))
print(retry(stop_service, 5))