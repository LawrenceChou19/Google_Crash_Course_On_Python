x = ["Now", "We","are","cooking!"]
print(type(x))
print(len(x))


def get_word(sentence, n):
# Only proceed if n is positive 
    if n > 0:
        words = sentence.split()
    # Only proceed if n is not more than the number of words 
        if n <= len(words):
            return(words[n-1])
    return("")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing

fruits = ["Pineapple","Banana","Apple","Melon"]
fruits.append("Kiwi")
print(fruits)
fruits.insert(0,"Orange")
print(fruits)
fruits.insert(25,"Peach")
print(fruits)
fruits.remove("Melon")
print(fruits)
# fruits.remove("Pear")
fruits.pop(3)


fullname = ('Grace','M','Hopper')

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600)//60
    remaining_seconds = seconds - hours *3600 -minutes*60
    return hours, minutes, remaining_seconds

result = convert_seconds(5000)
print(type(result))

print(result)
hours, minutes, seconds = result
print(hours,minutes,seconds)
hours, minutes, seconds = convert_seconds(1000)
print(hours, minutes,seconds)

def file_size(file_info):
	name,filetype,size= file_info
	return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21


animals = ["lion","Zebra","Dolphin","Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)
print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))


winners = ["Ashley","Dylan","Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1 ,person))

def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
        # print(type(result))
    return result
print(full_emails([("alex@examole.com","Alex Diego"),("shay@example.com","Shay Brandt")]))


def skip_elements(elements):
	# code goes here
    result = []
    for index, name in enumerate(elements):
        if index%2 ==0:
            # print("{} - {}".format(index + 1 ,name))
            result.append(name)
        else:
            continue
    return result

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']



multiples = []
for x in range(1,11):
    multiples.append(x*7)
print(multiples)

multiples= [x*7 for x in range(1,11)]
print(multiples)

languages = ["Python","Perl","Ruby","Go","Java","C"]
lengths = [len(language) for language in languages]
print(lengths) 
z = [x for x in range(0,101) if x % 3 == 0]
print(z)

def odd_numbers(n):
	return [x for x in range(0,n+1) if x%2 !=0 ]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []


filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = [rename.replace('.hpp','.h') for rename in filenames]

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

def pig_latin(text):
    say = "ay"
  # Separate the text into words
    words = text.split()
    sentence = []
    for word in words:    
        words = word[1:]+word[0]+say
        sentence.append(words)
    # for word in words:
    # # Create the pig latin word and add it to the list
    
    # # Turn the list back into a phrase
    return ' '.join(sentence)
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"


def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for values in [int(n) for n in str(octal)]:
        # print(value)
        # Check for each of the permissions values
        for value, letter in value_letters:
            if  values >= value:
                result += letter
                values -= value
            else:
                result +="-"
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------


def group_list(group, users):
    members = ', '.join(users)
    return "{}: {}".format(group, members)


print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"


def guest_list(guests):
	for name, age, job in guests:
		print('{} is {} years old and works as {}'.format(name,age,job))
guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""