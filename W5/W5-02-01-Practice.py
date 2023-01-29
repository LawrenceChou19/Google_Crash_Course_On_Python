
class Piglet:
    name = "piglet"
    def speak(self):
        print("Oink! I'm {}! Oink!".format(self.name))
hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()

petunia = Piglet()
petunia.name ="Petunia"
petunia.speak()

class Piglet:
    years = 0
    def pig_years(self):
        return self.years * 18

hamlet = Piglet()
print(hamlet.pig_years())
hamlet.years = 2
print(hamlet.pig_years())

class Apple:
    def __init__(self,color,flavor):
        self.color = color
        self.flavor = flavor
        
        
jonagold = Apple("red","sweet")
print(jonagold.color)


class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return  ("hi, my name is {}".format(self.name))

# Create a new instance with a name of your choice
some_person = Person("Ivan") 
# Call the greeting method
print(some_person.greeting())

class Apple:
    def __init__(self,color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color,self.flavor)
joangold = Apple("red","sweet")
print(jonagold)
print(help(Apple))

def to_second(hours,minutes,seconds):
    """Returns the amount of seconds in the given hours, minutes, and seconds."""
    return hours*3600+minutes*60+seconds
print(help(to_second))

class Piglet:
    """Represents a piglet that can say their name."""
    years = 0
    name = ""
    def speak(self):
        """Outputs a message including the name of the piglet."""
        print("Oink! I'm {}! Oink!".format(self.name))
    def pig_years(self):
        """Converts the current age to equivalent pig years."""
        return self.years * 18
print(help(Piglet))


class Person:
	def __init__(self, name):
		self.name = name
	def greeting(self):
		"""Outputs a message with the name of the person"""
		print("Hello! My name is {name}.".format(name=self.name))     
help(Person)

class Elevator:
	def __init__(self, bottom, top, current):
		"""Initializes the Elevator instance."""
		self.bottom = bottom #-1
		self.top = top #10
		self.current = current #0

	def up(self):
		"""Makes the elevator go up one floor."""
		# print('current is',self.current)
		if self.current < self.top: # 0 vs 10
			self.current += 1 #1
			# print('current is',self.current)
		else: 
			self.current #0

	def down(self):
		"""Makes the elevator go down one floor."""
		# print('current is',self.current)
		if self.current > self.bottom: # 1 vs -1
			self.current -= 1
			# print('current is',self.current)
		else: 
			self.current 

	def go_to(self, floor):
		"""Makes the elevator go to the specific floor."""
		# print('Currnet floor is ',self.current)
		self.current = floor

	def current(self):
		print('Current is',self.current)
		return self.current

elevator = Elevator(-1, 10, 0)

elevator.up() 
print(elevator.current) #should output 1
elevator.down() 
print(elevator.current) #should output 0
elevator.go_to(10) 
print(elevator.current) #should output 10

# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current) # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1