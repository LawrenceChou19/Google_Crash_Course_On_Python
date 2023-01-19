x = 1
sum = 0
while x < 10:
    sum+=x
    x+=1

product =1 
while x< 10:
    product = product * x #
    x +=1
print(sum,product)

for x in range(5):
    print(x)
    
def factorial(n):
    print("Factorial called with "+ str(n))
    if n < 2:
        print("Returning 1")
        return 1 
    result = n * factorial(n-1)
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result
print(factorial(5))


def digits(n):
    count = 0
    if n == 0:
        return 1
    while (n>=1):
        count += 1
        n=n/10
        # print(n)
    return count
	
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1

def multiplication_table(start, stop):
    for x in range(start,stop+1):
        for y in range(start,stop+1):
            print(str(x*y), end=" ")
        print()

multiplication_table(1, 3)
# Should print the multiplication table shown above

def counter(start, stop):
    x = start
    if start>stop:
        return_string = "Counting down: "
        while x >= stop:
            return_string += str(x)
            if x>stop:
                return_string += ","
            x-=1
    else:
        return_string = "Counting up: "
        while x <= stop:
            return_string += str(x)
            if x<stop:
                return_string += ","
            x+=1
    return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"


def even_numbers(maximum):
    return_string = ""
    for x in range(2,maximum+1,2):
        return_string += str(x) + " "
    return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed

# def decade_counter(year):
#     while year < 50:
#         year += 10
#     return year
# print(decade_counter(0))

# for x in range(1, 10, 3):
#     print(x)
    
for x in range(10):
    # print(x)
    for y in range(x):
        print(y)
        
        