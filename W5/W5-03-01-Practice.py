class Fruit:
    def __init__(self,color,flavor):
        self.color = color
        self.flavor = flavor

class Apple(Fruit):
    pass
class Grape(Fruit):
    pass
granny_smith = Apple("green", "tart")
carnelian = Grape("purple","sweet")
print(granny_smith.flavor)
print(carnelian.color)

class Animal:
    sound=""
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("{sound} I'm {name}! {sound}".format(name=self.name,sound=self.sound))
class Piglet(Animal):
    sound = "Oink!"
hamlet = Piglet("Hamlet")
hamlet.speak()
class Cow(Animal):
    sound = "Moooo"
milky = Cow("Milky White")
milky.speak()

class Clothing:
  material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.name,self.material))
			
class Shirt(Clothing):
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()

class Repository:
    def __init__(self):
        self.packages = {}
    def add_package(self, package):
        self.packages[package.name] = package
    def total_size(self):
        result = 0 
        for package in self.packages.values():
            result += package.size
        return result


class Clothing:
  stock={ 'name': [],'material' :[], 'amount':[]}
  def __init__(self,name):
    material = ""
    self.name = name
  def add_item(self, name, material, amount):
    Clothing.stock['name'].append(self.name)
    Clothing.stock['material'].append(self.material)
    Clothing.stock['amount'].append(amount)
  def Stock_by_Material(self, material):
    count=0
    n=0
    for item in Clothing.stock['material']:
      if item == material:
        count += Clothing.stock['amount'][n]
        n+=1
    return count

class shirt(Clothing):
  material="Cotton"
class pants(Clothing):
  material="Cotton"
  
polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)


import random
random.randint(1,10)
print(random.randint(1,10))
import datetime
now = datetime.datetime.now()
print(type(now))
print(now)

class Animal:
    name = ""
    category = ""
    
    def __init__(self, name):
        self.name = name
    
    def set_category(self, category):
        self.category = category

class Turtle(Animal):
    category = "Reptile"        
print(Turtle.category)
class Snake(Animal):
    category = "Reptile"
class Zoo:
    def __init__(self):
        self.current_animals = {}
    
    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category
    
    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal == category:
                result += 1
        return result

zoo = Zoo()

turtle = Turtle("Turtle") #create an instance of the Turtle class
snake = Snake("Snake") #create an instance of the Snake class

zoo.add_animal(turtle)
zoo.add_animal(snake)

print(zoo.total_of_category("Reptile")) #how many zoo animal types in the reptile category