#defops V1. a simple defense tool to advise on drone mission readiness.

print("Mission Readiness System")
print("                        ")

#ask the user the equipment they'd like to check mission readiness for
equipment_type = input("Check mission readiness for Drone/Jet?: ").lower()

#collect required input
fuel = int (input("Amount of fuel available: "))
ammo = int (input("Available ammo: "))
weather = input("Weather condition (clear/Rainy/Stormy): ").lower()

#advise on mission readiness based on user input
if equipment_type == "drone":
   if fuel <= 30 or ammo <= 30 or weather == "stormy":
    print("Drone is NOT mission ready. Conditions unsafe.")
   elif weather == "rainy":
    light_or_heavy = input("Heavy or Light?: ")
    if light_or_heavy == "heavy":
     print ("Weather conditions unsafe for flight operations.")
    elif light_or_heavy == "light":
      print("Weather conditions safe for flight operations.")
    else:
      print("Invalid input")
   else:
     print("Drone cleared for mission. Proceed with operation.")

elif equipment_type == "jet":
  if fuel <= 50 or ammo <= 40 or weather == "stormy":
    print("Jet is not mission ready. Conditions unsafe.")
  elif weather == "rainy":
    light_or_heavy = input("Heavy or Light?: ")
    if light_or_heavy == "heavy":
     print("Weather conditions unsafe for flight operations.")
    elif light_or_heavy == "light":
      print("Weather conditions safe for flight operations.")
    else:
      print("Invalid input")
  else:
     print("Jet cleared for mission. Proceed with operation")

else:
  print("Invalid input. Select either Drone or Jet")
