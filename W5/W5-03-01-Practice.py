# class Fruit:
#     def __init__(self,color,flavor):
#         self.color = color
#         self.flavor = flavor

# class Apple(Fruit):
#     pass
# class Grape(Fruit):
#     pass
# granny_smith = Apple("green", "tart")
# carnelian = Grape("purple","sweet")
# print(granny_smith.flavor)
# print(carnelian.color)

# class Animal:
#     sound=""
#     def __init__(self,name):
#         self.name = name
#     def speak(self):
#         print("{sound} I'm {name}! {sound}".format(name=self.name,sound=self.sound))
# class Piglet(Animal):
#     sound = "Oink!"
# hamlet = Piglet("Hamlet")
# hamlet.speak()
# class Cow(Animal):
#     sound = "Moooo"
# milky = Cow("Milky White")
# milky.speak()

##############quiz

# class Clothing:
#   material = ""
#   def __init__(self,name):
#     self.name = name
#   def checkmaterial(self):
# 	  print("This {} is made of {}".format(self.name,self.material))
			
# class Shirt(Clothing):
#   material="Cotton"

# polo = Shirt("Polo")
# polo.checkmaterial()

############################################################

# class Repository:
#     def __init__(self):
#         self.packages = {} #empty packages
#     def add_package(self, package): # add dicrionary class
#         self.packages[package.name] = package # accessing size attribute
#     def total_size(self):
#         result = 0 
#         for package in self.packages.values():
#             result += package.size
#         return result

###############quiz

# Let’s expand a bit on our Clothing classes from the previous in-video question. 
# Your mission: Finish the "Stock_by_Material" method and iterate over the amount of each item of a given material that is in stock. 
# When you’re finished, the script should add up to 10 cotton Polo shirts.

# class Clothing:
#   stock={ 'name': [],'material' :[], 'amount':[]}
# #   print(stock)
#   def __init__(self,name):
#     material = ""
#     self.name = name
#   def add_item(self, name, material, amount):# add item in each dictionary
#     Clothing.stock['name'].append(self.name)
#     Clothing.stock['material'].append(self.material)
#     Clothing.stock['amount'].append(amount)
#   def Stock_by_Material(self, material):
#     count=0
#     n=0
#     # print(Clothing.stock)
#     for item in Clothing.stock['material']:
#         # print(item)
#         if item == material: #if Polo("Cotton") == Sweatpants("Cotton") 
#             count += Clothing.stock['amount'][n] # 4:1 , 10:2
#             print("count is ",count)
#             n+=1
#             print("n is ",n)
#     return count #retunt 10
  

# class shirt(Clothing):# define shirt class
#   material="Cotton"
# class pants(Clothing):# define pants class
#   material="Cotton"
# class underwaer(Clothing):# define pants class
#   material="Nylon"
  
# polo = shirt("Polo")
# sweatpants = pants("Sweatpants")
# panties = underwaer("Panties")
# polo.add_item(polo.name, polo.material, 4)#call add_item def
# sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
# panties.add_item(panties.name,panties.material,15)


# current_stock = polo.Stock_by_Material("Cotton") # calculator the cotton in stock
# print(current_stock)


################################################################################


# import random
# random.randint(1,10)
# print(random.randint(1,10))

# import datetime
# now = datetime.datetime.now()
# print(type(now))
# print(now)
# print(now.year)
# print(now+datetime.timedelta(days=28))

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
        for animal in self.current_animals.values(): #for animal in self.___.values():
            if animal == category: # if ___ == category:
                result += 1
        return result

zoo = Zoo()

turtle = Turtle("Turtle") #create an instance of the Turtle class
snake = Snake("Snake") #create an instance of the Snake class

zoo.add_animal(turtle)
zoo.add_animal(snake)

print(zoo.total_of_category("Reptile")) #how many zoo animal types in the reptile category

