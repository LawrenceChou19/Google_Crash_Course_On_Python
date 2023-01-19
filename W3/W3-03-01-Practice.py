def factorial(n):
    if n <2:
        return 1
    return n * factorial(n-1)
print(factorial(5))


def factorial(n):
    print("Factorial called with " +str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n-1)
    print("Retunring "+ str(result) + " for factorial of "+ str(n))
    return result

print(factorial(4))
 
def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return 0

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

# def recursive_function(parameters):
#     if base_case_condition(parameters):
#         return base_case_value
#     recursive_function(modified_parameters)