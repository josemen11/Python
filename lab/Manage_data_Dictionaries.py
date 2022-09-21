planet = {
    'name': 'Earth',
    'moons': 1
}

print(planet.get('name'))
print(planet['name'])
#wibble = planet.get('wibble') # Returns None
#wibble = planet['wibble'] # Throws KeyError
planet.update({'name': 'Makemake'})
print(planet)
planet['name'] = 'Makemake'
print(planet)


rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}
for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1
    
total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'There was {total_rainfall}cm in the last quarter')    