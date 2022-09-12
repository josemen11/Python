#IF
a = 90
b = 50
# test expression
if a < b:
    # statement to be run
    print(b)

#ELSE
a = 90
b = 50
if a >= b:
    print(a)
else:
    print(b)

#ELIF
a = 90
b = 30
if a >= b:
    print("a is greater than or equal to b")
elif a == b:
    print("a is equal to b")

#IF ELSE ELIF
a = 10
b = 20
c = 30
if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")
    
#OR
a = 23
b = 30
if a == 30 or b == 30:
    print(a + b)   
    
#AND
a = 23
b = 25
if a == 25 and b == 25:
    print (a + b)     

a = 23
b = 34
if a == 12 and b == 34:
    print (a + b)    
    