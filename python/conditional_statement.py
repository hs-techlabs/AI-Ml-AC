'''
age=17
if age>=18:
    print("You are eligible to vote")
    print("You are eligible to drive")
else:
    print("You are not eligible to vote")
    print("You are not eligible to drive")
'''


'''nested if else'''
'''
col=input("Enter your favourite color :")
if col=="red":
    print("stop")
elif col=="yellow":
    print("ready")
elif col=="green":
    print("go")
else:
    print("invalid color")
'''

'''nested if else'''
'''
age=int(input("Enter your age :"))
if age<=13:
    print("You are a child")
elif age>13 and age<=19:
    print("You are a teenager")
elif age>19 and age<=60:
    print("You are an adult")
else:
    print("You are a senior citizen")
'''

'''login system'''
'''
username=input("Enter your username :")
password=input("Enter your password :")
if username=="admin" and password=="admin":
    print("Login successful")
else:
    print("Login failed")
'''

'''check if number is divisible by 5'''
'''
num=int(input("Enter a number :"))
if(num%5==0):
    print(num,"is divisible by 5")
else:
    print(num,"is not divisible by 5")
'''

'''check if number is even or odd'''
'''
num=int(input("Enter a number :"))
if(num%2==0):
    print(num,"is even")
else:
    print(num,"is odd")
'''

'''nesting if else'''
'''
username=input("Enter your username :")
password=input("Enter your password :")
if username=="admin":
    if password=="admin":
        print("Login successful")
    else:
        print("Login failed")
else:
    print("Login failed")
'''

'''nesting if else'''   
'''
username=input("Enter your username :")
password=input("Enter your password :")

if username=="admin" and password=="pass":
    print("Login successful")
else:
    if username!="admin":
        print("wrong username")
    else:
        print("Login failed")
'''

'''match case '''
'''
color=input("Enter your favourite color :")
match color:
    case "red":
        print("stop")
    case "yellow":
        print("ready")
    case "green":
        print("go")
    case _:
        print("give right color")
'''