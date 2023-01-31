# print(type(0))
# print(type("")) 
# print(dir(""))

# # print(help("int"))

# class Apple:
#     pass

# class Apple:
#     color = ""
#     flavor = ""

# jonagold= Apple()
# jonagold.color = "red"
# jonagold.flavor = "sweet"
# print(jonagold.color)
# print(jonagold.flavor)

# goldem =  Apple()
# goldem.color = "Yellow"
# goldem.flavor = "Soft"


# #quiz
# class Flower:
#   color = 'unknown'

# rose = Flower()
# rose.color = "Red"

# violet = Flower()
# violet.color = "Blue"

# this_pun_is_for_you = "Sugar is sweet, and so are you."

# print("Roses are {},".format(rose.color))
# print("violets are {},".format(violet.color))
# print(this_pun_is_for_you) 


###################Practice Quiz: Object-oriented Programming (Optional)################

# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
#Here, despite G.B. Shaw's quote, our characters have started with       
#different amounts of apples so we can better observe the results. 
#We're going to have Martin and Johanna exchange ALL their apples with #one another.
#Hint: how would you switch values of variables, 
#so that "you" and "me" will exchange ALL their apples with one another?
#Do you need a temporary variable to store one of the values?
#You may need more than one line of code to do that, which is OK. 
      you.apples, me.apples = me.apples, you.apples #exchange apples
        
      return you.apples, me.apples
    
def exchange_ideas(you, me):
    #"you" and "me" will share our ideas with one another.
    #What operations need to be performed, so that each object receives
    #the shared number of ideas?
    #Hint: how would you assign the total number of ideas to 
    #each idea attribute? Do you need a temporary variable to store 
    #the sum of ideas, or can you find another way? 
    #Use as many lines of code as you need here.

	# print('before you.ideas is ',you.ideas,'me.ideas is ',me.ideas)
	you.ideas += me.ideas #exchange the idea you.ideas add me.ideas = 2
	# print('after you.ideas is ',you.ideas,'me.ideas is ',me.ideas)
	me.ideas += you.ideas - me.ideas # me.ideas = 1, plus you.ideas-me.ideas=1, 1+1 =2
	# print('after you.ideas is ',you.ideas,'me.ideas is ',me.ideas)
	return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))



# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0
	population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
	# Initialize the variable that will hold
# the information of the city with
# the highest elevation
	return_city = City()

	# Evaluate the 1st instance to meet the requirements:
	# does city #1 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city1.population >= min_population:
		print('min_population is ',min_population,'City population is ',city1.population)
		return_city = city1
	# Evaluate the 2nd instance to meet the requirements:
	# does city #2 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city2.population >= min_population and city2.elevation > return_city.elevation:
		print('min_population is ',min_population,'City2 population is',city2.population,'and city2 elevation vs return_city.elevation is ',city2.elevation," > ",return_city.elevation)
		return_city = city2
		# print(return_city.elevation)
	# Evaluate the 3rd instance to meet the requirements:
	# does city #3 have at least min_population and
	
	# is its elevation the highest evaluated so far?
	if city3.population >= min_population and city3.elevation > return_city.elevation:
		print('min_population is ',min_population,'City2 population is',city3.population,'and city3 elevation >',return_city.elevation)
		return_city = city3

	#Format the return string
	if return_city.name:
		return f"{return_city.name}, {return_city.country}"
	else:
		return ""

print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""

# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0
	population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
	# Initialize the variable that will hold
# the information of the city with
# the highest elevation
	return_city = City()

	# Evaluate the 1st instance to meet the requirements:
	# does city #1 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city1.population >= min_population:
		return_city = city1
	# Evaluate the 2nd instance to meet the requirements:
	# does city #2 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city2.population >= min_population and city2.elevation > return_city.elevation:
		return_city = city2
	# Evaluate the 3rd instance to meet the requirements:
	# does city #3 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city3.population >= min_population and city3.elevation > return_city.elevation:
		return_city = city3

	#Format the return string
	if return_city.name:
		return f"{return_city.name}, {return_city.country}"
	else:
		return ""

print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""

class Furniture:
	color = ""
	material = ""

table = Furniture()
table.color = "brown"
table.material = "wood"

couch = Furniture()
couch.color = "red"
couch.material = "leather"

def describe_furniture(piece):
	return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))

print(describe_furniture(table)) 
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch)) 
# Should be "This piece of furniture is made of red leather"




