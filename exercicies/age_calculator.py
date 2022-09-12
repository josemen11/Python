
c=0
while True and c<3:
    user_input=input("enter your age: ")
    try:
        age=int(user_input)
        break
    except Exception as e:
        print(f"Cannot convert {user_input} to valid number: {e}")
        c +=1
decades= age//10
years= age%10        
display_text= "Age: {} decades: {} years {}".format(age,decades,years)  
print(display_text)      