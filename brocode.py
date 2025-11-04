#variable = a container for a value. Behaves as the value it contains

#first_name = "Eddie"
#last_name = "Kairu"
#full_name = first_name +" "+last_name
#print("Hello "+full_name)
#print("Hello " +name)

#age = 22
#age += 1
#print("My age is: " +str (age))
#print(type(age))
#height = 250.5
#print("My height is: " +str(height)+"cm")
#print(type(height))

#human = True
#print("Are you a human: " +str(human))
#print(type(human))

#multiple assignment = allows us to assign multiple variables at the same time in one line of code

#name = "Eddie"
#age = 23
#attractive = True
#name, age, attractive = "Eddie", 23, True
#print(name)
#print(age)
#print(attractive)

#Spongebob = 30
#Patrick = 30
#Sandy = 30
#Squidward = 30

#Spongebob = Patrick = Sandy = Squidward = 30
#print(Spongebob)
#print(Patrick)
#print(Sandy)
#print(Squidward)

#Google Example
#a = b = c = "Hello"
#print(f"a:{a}, b:{b}, c:{c}")
#name = "Eddie"
#age = 23
#print(f"My name is {name} and I am {age} years old.")
#reassigning variables
#mission = "Recon"
#mission = "Assault"
#print (mission)
#mixing variables
#soldiers = 6
#humvees = 2
#print(f"{soldiers} soldiers on ground with {humvees} humvees for the {mission} mission.")
#print(soldiers + humvees)
#print(f"Total units: {soldiers + humvees}")

#Practice Exercise for Def HQ
#operation_name = "Skyfall"
#total_drones = 10
#total_drones = 15
#fuel_capacity = 250.5
#enemy_detected = True
#equipment = "Radar", "Radio", "Thermo"
#commander_info = "Lt. Smith, Rank: Captain, Experience: 5 years"
#print(f"Operation {operation_name} was successful with {total_drones} drones deployed flying at {fuel_capacity} liters fuel capacity. It's {enemy_detected} enemies were detected thanks to the {equipment}. Commander details are as follows: {commander_info}.")
#print(type(operation_name))
#print(type(total_drones))
#print(type(fuel_capacity))
#print(type(enemy_detected))
#print(type(equipment))
#print(type(commander_info))

#String Methods
#name = "Eddie"
#print(len(name))
#print(name.find("E")) #finds the index of the first occurence of the specified value
#print(name.capitalize()) #capitalizes the first letter of the string
#print(name.upper()) #converts the string to uppercase
#print(name.lower()) #converts the string to lowercase
#print(name.isdigit()) #returns True or False if all characters in the string are digits
#print(name.isalpha()) #returns True or False if all characters in the string are alphabetic
#print(name.count("d")) #returns the number of times a specified value occurs in the string
#print(name.replace("d", "b")) #replaces a specified value with another value in the string
#print(name*3) #repeats the string a specified number of times

#Type casting = converting the data type of a value to another data type
#x = 1 #int
#y = 2.0 #float
#z = "3" #str

#print ("x is now "+str(x))
#print ("y is now "+str(y))
#print(z*3)

#user input
#name = input("what is your name?: ")
#age = int (input("How old are you?: "))
#height = float (input("How tall are you? "))

#print("Hello " + name)
#print(f"You are {age} years old and {height} meters tall")

#useful functions related to numbers: math functions
#import math
#pi = 3.14

#x = 1
#y = 2
#z = 3

#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(math.abs(pi))
#print(math.pow(pi,2))
#print(math.sqrt(pi))
#print(max(x,y,z))
#print(min(x,y,z))

#slicing = create a substring by extracting elements from another string
#To slice a string we can either use the indexing[] or slice() function
#With slicing, there are 3 optional arguments [start:stop:step]

#name = "Eddie Kairu"
#first_name = name[:5]
#last_name = name[6:11]
#funky_name = name[0:12:3]
#reversed_name = name[::-1]
#print(first_name)
#print(last_name)
#print(funky_name)
#print(reversed_name)

#part 2; explaining the slice function. We can use the slice function to create a slice object which is reusable.

#website1 = "http://google.com"
#website2 = "http://wikipedia.com"
#slice = slice(7,-4)
#print(website1[slice])
#print(website2[slice])

#if statement = A block of code that will execute if it's condition is true

#age = int (input("How old are you? "))
#if age >=100:
    #print("You are century old!")

#elif age >= 18:
    #print("You are an adult!")

#elif age < 0:
    #print("Input a valid age")
#else:
    #print("You are a minor.")

#Logical operators (and,or,not) = used to check if two or more conditional statements are true.

temp = int(input("What is the temperature outside? "))

if not(temp >= 0 and temp <= 30):
    print("The temperature is bad today.")
    print("Don't go outside!")
elif not (temp < 0 or temp > 30):
    print("The temperature is good today")
    print("Go outside!")

age = int(input("How old are you? "))
if (age >= 18 and age <=99):
    print("You are an adult!")
elif age >= 100:
    print("You are a century old")
elif age < 18 or age is 0:
    print("You are a minor.")
else:
    print("Input a valid age")


bot_name = "Trigger"
print(f"hello, I'm {bot_name}. How can I help you?")

while True:
 user_input = input("You: ").strip().lower()

 if user_input in ["hi", "hello"]:
    print(f"{bot_name}: Hello, what's up!")

 elif user_input in ["What is your name?"]:
    print(f"{bot_name}: {bot_name}, my name is {bot_name}!")

 elif user_input in ["bye", "goodbye"]:
    print(f"{bot_name}: Goodbye!")

 else:
   print(f"{bot_name}: I don't understand yet, I'm still learning!")