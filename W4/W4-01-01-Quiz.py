def is_palindrome(input_string):
	# We'll create two strings, to compare them
    new_string = ""
    reverse_string = ""
	# Traverse through each letter of the input string
    for i in input_string.lower():
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
        if i.replace(" ",""):# eg abc -> cba FIFO
            new_string = i+new_string
            print(new_string)
            reverse_string = i+reverse_string
            print(reverse_string)
	# Compare the strings
    if new_string[::-1]==reverse_string:

        return True
    return False

# print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
# print(is_palindrome("kayak")) # Should be True



def convert_distance(miles):
	km = miles * 1.6 
	result = "{} miles equals {:.1f} km".format(miles,km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

Weather = "Rainfall"

print(Weather[:4])

def nametag(first_name, last_name):
	return("{} {}.".format(first_name,last_name[:1]))

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 

def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence 
	if sentence.endswith(old):#if old word match in the last word in the string No.2 print will skip
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the 
		# end with the new string
		i = sentence.rindex(old) #find the index number assign to i variable
		new_sentence = sentence[:i] + new # keep the original sentence until i variable e.g "It's raining cats and ","dogs"
		return new_sentence

	# Return the original sentence if there is no match 
	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"




