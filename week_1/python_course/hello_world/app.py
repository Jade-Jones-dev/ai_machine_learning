print('hello world')
print('*' * 10)

x = 1
y = 2
unit_price = 3

#int -->
students_count = 1000
#<!-- float -->
rating = 4.99
#<!-- bool -->
is_Published = True
#<!-- str -->
course_name = 'Python Programming'
#len
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
print(course.find('python')
print(course.replace('p', 'j'))
print("python" in course)
print("python" not in course)
print(course.split(' '))
print(course.split(' '))
