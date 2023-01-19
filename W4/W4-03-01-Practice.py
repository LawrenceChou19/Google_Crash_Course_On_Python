x = {}
type(x)

file_counts = {"jpg":10,"txt":14,"csv":2,"py":23}
print(file_counts)
print(file_counts["txt"])
print("jpg" in file_counts)
print("html" in file_counts)

file_counts["cfg"]=8
print(file_counts)

file_counts["csv"]=17
print(file_counts)

del file_counts["cfg"]
print(file_counts)


file_counts = {"jpg":[10,20],"txt":14,"csv":2,"py":23}
for extension in file_counts:
    print(extension)
    
for ext, amount in file_counts.items():
    print("There are {} file with the .{} extension".format(amount,ext))
    
print(file_counts.keys()) # dict_keys(['jpg','txt','csv','py'])
print(file_counts.values())

for value in file_counts.values():
    print(value)
    
cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for animal,parts in cool_beasts.items():
    print("{} have {}".format(animal,parts))
    
    
    
def count_letters(text):
    result={}# create curly bruckets 
    for letter in text: # eg 
        if letter not in result:
            result[letter]=0 #eg if a != a end of the count
        result[letter] +=1 # else continue cound the letter
    return result

print(count_letters("aaaaa"))
print(count_letters("tenant)"))
print(count_letters("a long string with a lot of letters"))

ip_addresses = ["192.168.1.1","127.0.0.1","8.8.8.8"]
host_address = {"router": "192.168.1.1","localhost":"127.0.0.1","google":"8.8.8.8"}

x = {"Practice1":10,"Practice5":30}
print(len(x))
for ket in x:
    print(ket)
 
for ket, valeu in x.items():
    print(ket,valeu)
    
print(x.get("Practice1"))
print(x.keys())
print(x.values())
y = {"Practice3":55,"Practice6":66}
print(x.update(y))
print(x.keys())
print(x.clear())
print(x.keys())



wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)

def format_address(address_string):
  # Declare variables
    lista =''
    address=[]
  # Separate the address string into parts
    address_string = address_string.split()
  # Traverse through the address parts
    for parts in address_string:
        if parts.isnumeric():
            lista=parts
        else:
            address.append(parts)

    # Determine if the address part is the
    # house number or part of the street name
    
  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  

    return "house number {} on street named {}".format(lista,' '.join(address))
print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"


def highlight_word(sentence, word):
	result = []
	sentence = sentence.split()
	for cword in sentence:
		if word in cword:
			result.append(cword.upper())
		else:
			result.append(cword)
	return ' '.join(result)# convert list to string with blank

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))


def combine_lists(list1, list2):
  new_list = []
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  list1.reverse()
  new_list = list2+list1
  return new_list
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

def squares(start, end):
	return [i**2 for i in range(start,end+1)]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def car_listing(car_prices):
  result = ""
  for car, price in car_prices.items():
    result += "{} costs {} dollars".format(car,price) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))


def combine_guests(guests1, guests2):
  new_list = []
  new_list = guests2
  new_list.update(guests1)

  return new_list
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))

def count_letters(text):
  result = {}
  text= text.lower()
  print(text)
  # Go through each letter in the text
  for letter in text.replace(" ",""):
    # print(letter)
    # Check if the letter needs to be counted or not
    if letter.isalpha():

      count = text.count(letter)
      result[letter] = count
  return result

    # Add or increment the value in the dictionary
    # ___
  # return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

animal = "Hippopotamus"
print(animal[3:6])
print(animal[-5])
print(animal[10:])

colors = ["red", "white", "blue"]
colors.insert(2, "yellow")

host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
host_addresses.keys()

