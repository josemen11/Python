from time import sleep

user_input = ''

while user_input.lower() != 'done':
    user_input = input('Enter a new value, or done when done: \n')
    
    
user_input = ''
inputs = []


while user_input.lower() != 'done':
    if user_input:
        inputs.append(user_input)
    user_input = input('Enter a new value, or done when done: \n')    
    
#for
countdown = [4, 3, 2, 1, 0]
for number in countdown:
    print(number)
print("Blast off!! 🚀")    



countdown = [4, 3, 2, 1, 0]

for number in countdown:
    print(number)
    sleep(1)  # Wait 1 second
print("Blast off!! 🚀")
