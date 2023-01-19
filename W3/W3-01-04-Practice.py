for x in range(25):
    print(x)
    
def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)

# print(greet_friends(['Taylor','Luisa','Jamaal','Eli']))
print(greet_friends("Barry"))

def count_down(start_number):
    while (start_number > 0):
        print(start_number)
        start_number -= 1
    print("Zero!")

count_down(3)