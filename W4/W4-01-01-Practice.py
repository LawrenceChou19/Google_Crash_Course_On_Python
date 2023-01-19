name = "Sasha"
color = "gold"
place = "Cambridge"

pet =""
prt ="looooooooooooooooooooooooooooooooooong cat"

print("Name: " + name + ", Favorite color: " + color)

def double_word(word):
    word = word*2 + str(len(word*2))
    return word

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

name = "Jaylen"

print(name[1])
print(name[0])
print(name[5])
# print(name[6])

text="Random string with a lot of characters"
print(text[-1])
print(text[-2])

color = "Orange"
print(color[1:4])

fruit = "Pineapple"
print(fruit[:4])
print(fruit[4:])

message = "A kong string with a silly typo"
# message[2]= "l"
# print(message)
new_message = message[0:2] + "L" + message[3:]
print(new_message) 
message= "And another one"
print(message)

pets= "Cats & Dogs"

print(pets.index("&"))
print(pets.index("C"))
print(pets.index("Dog"))

word = "supercalifragilisticexpialidocious"
print(word.index("x"))

print("Dragon" in pets)
print("Cats" in pets)

def replace_domain(email,old_domain,new_domain):
    if "@" + old_domain in email:# check the email domain is old or not
        index = email.index("@"+ old_domain)
        new_email = email[:index] + "@" +new_domain
        return new_email
    return email
print(replace_domain('ichou@strongtie.com','strongtie.com','simpsonmfg.com'))
print(replace_domain('ichou@simpsonmfg.com','strongtie.com','simpsonmfg.com'))

print("Mountains".upper())
print("Mountains".lower())
answer = 'YES'
if answer.lower() == "yes":
    print("User said yes")
print(" yes ".strip())
print(" yes ".lstrip())
print(" yes ".rstrip())
"Forest".endswith("rest")
"Forest".isnumeric()
"12345".isnumeric()
int("12345")+int("54321")
print(" ".join(["This","is","a","phrase","joined","by","spaces"]))
print("...".join(["This","is","a","phrase","joined","by","dots"]))
print("This is another example".split())

name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name,number))
print("Your lucky number is {number}, {name}.".format(name=name,number=len(name)*3))

def student_grade(name, grade):
	return "{} received {}% on the exam".format(name,grade)
print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

price = 7.5
with_tax = price * 1.09
print(price,with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price,with_tax))

def to_celsius(x):
    return (x-32)*5/9
for x in range(0,101,10):
    print(x,to_celsius(x))

for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C".format(x,to_celsius(x))) # Use > greater than operator to align text to the right


# "base string with {} placeholders".format(variables)

example = "format() method"

formatted_string = "this is an example of using the {} on a string".format(example)

print(formatted_string)

"""Outputs:
this is an example of using the format() method on a string
"""

# "{0} {1}".format(first, second)

first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)

print(formatted_string)

"""Outputs:
apple carrot banana
"""

# "{var1} {var2}".format(var1=value1, var2=value2)

# {:d} integer value
# '{:d}'.format(10.5) → '10'


