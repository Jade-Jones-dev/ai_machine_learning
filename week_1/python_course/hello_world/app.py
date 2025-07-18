import math
print('hello world')
print('*' * 10)

x = 1
y = 2
unit_price = 3

# int -->
students_count = 1000
# <!-- float -->
rating = 4.99
# <!-- bool -->
is_Published = True
# <!-- str -->
course_name = 'Python Programming'
# len
print(len(course_name))
print(course_name[0])
print(course_name[-1])
print(course_name[0:3])
print(course_name[:3])
print(course_name[:])

# \"
# \'
# \\
# \n

course = "new \"python course\""
print(course)

# formatted strings
first = "Jade"
last = "Jones"
full = first + ' ' + last
print(full)
print(f'{first} {last}')
print(f'{first} {last} is a student in the {course_name} course.')

course = "learning python programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.find('python'))
print(course.replace('p', 'j'))
print("python" in course)
print("python" not in course)
print(course.split(' '))
print(course.split(' '))

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

x=10
x=x + 3
x += 3

print(round(2.9))
print(abs(-2.9))
math.ceil(13)

x=input("x: ")
y=int(x) + 1
print(f'x: {x}, y: {y}')
# y = x + 1

# int(x)
# float(x)
# complex(x)
# bool(x)
# str(x)

# Falsy
# ""
# 0
# None

# 10 > 3
# 10 >= 3
# 10 < 3
# 10 <= 3
# 10 == 3
# 10 != 3
# 10 is 3

# conditional statements
temperature = 35

if temperature > 30:
    print("It's a hot day")
elif temperature > 20:
    print("It's a nice day")
else:
    print("It's a cold day")
print("Done")

# ternary operator
age = 22
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

# logical operators
has_high_income = True
has_good_credit = True
student = True

if has_high_income and has_good_credit:
    print("Eligible")
else:
    print("Not eligible")

if not student :
    print("Not a student")
else:
    print("Is a student")   

if(has_high_income or has_good_credit) and not student:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# chaining comparison operators
age = 22
if 18 <= age < 65:
    print("Eligible for work")
else:
    print("Not eligible for work")


# loops
for number in range(5):
    print("attempt" , number , number * "." )

successful = True
for number in range(3):
    print("attempt")
    if successful:
        print("successful")
        break
else:
    print("attempted 3 times and failed")

# nested loops

for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')    