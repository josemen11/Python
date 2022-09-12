fact = "The Moon has no atmosphere."
print(fact)
fact + "No sound can be heard on the Moon."
print(fact)


two_facts = fact + "No sound can be heard on the Moon."
print(two_facts)
'The Moon has no atmosphere.No sound can be heard on the Moon.'

multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)

 #------------
 
multiline = """Facts about the Moon:
...  There is no atmosphere.
...  There is no sound."""
print(multiline)

#TITLE
heading = "temperatures and facts about the moon"
print(heading.title())



#split
temperatures = """Daylight: 260 F
... Nighttime: -280 F"""
temperatures .split()


temperatures .split('\n')


"Moon" in "This text will describe facts and challenges with space travel"
"Moon" in "This text will describe facts about the Moon"
 

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
... while Mars has -28 Celsius."""
temperatures.find("Moon")
temperatures.find("Mars")
temperatures.count("Mars")
temperatures.count("Moon")
 

"The Moon And The Earth".lower()

"The Moon And The Earth".upper()
 

#chequear
temperatures = "Mars Average Temperature: -60 C"

parts = temperatures.split(':')
print(parts)


mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
  if item.isnumeric():
       print(item)


"-60".startswith('-')

if "30 C".endswith("C"):
    print("This temperature is in Celsius")


"Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C")


text = "Temperatures on the Moon can vary wildly."
"temperatures" in text

"temperatures" in text.lower()

moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year"]
'\n'.join(moon_facts)
print(moon_facts)


#add %
print("--------------------------------")
print("""Both sides of the %s get the same amount of sunlight,\n but only one side is seen from %s because\n the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))
print("--------------------------------")
mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth".format(mass_percentage))

print("--------------------------------")
print("""You are lighter on the {0}, because on the {0} \nyou would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage))



print("--------------------------------")
print("""You are lighter on the {moon}, because on the {moon} \nyou would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))



print("--------------------------------")
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth")

print("--------------------------------")
round(100/6, 1)
16.7


print("--------------------------------")

print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth")

print("---------------------------------------")
subject = "interesting facts about the moon"
f"{subject.title()}"

