# Variables & Data Types
int_var = 5
float_var = 3.14
string_var = "abc"
bool_var = True

# Viewing Data Types
print(type(int_var))
print(type(float_var))
print(type(string_var))
print(type(bool_var))

# Casting
str10 = "10"
int10 = int(str10)
print(type(str10))
print(type(int10))

int20 = 20
str20 = str(int20)
print(type(int20))
print(type(str20))

# Constants
INCHES_IN_FOOT = 12
PI_APPROX = 3.14

# Integer Addition and Subtraction
a = 10 + 5
print(a)

b = 6
c = -1
d = b + c
print(d)

f = 3 - 9
print(f)

g = 4
h = 2
i = g - h
print(i)

j = 6
k = 3
l = j/k
print(l)

m = 2
n = 3
p = m/n
print(p)



# Updating Shortcut
x = 10
x = x + 5
print(x)
x = 10
x += 5
print(x)
y = 10
y = y - 5
print(y)
y = 10
y -= 5
print(y)

# String Concatenation
first_name = "John"
last_name = "Smith"
full_name = first_name + " " + last_name
print(full_name)

age = 45
# full_name_and_age = first_name + " " + last_name + " " + age
full_name_and_age = first_name + " " + last_name + " " + str(age)
print(full_name_and_age)

bday_year = 2020
bday_month = 12
bday_day = 11
bday_str1 = str(bday_month) + "/" + str(bday_day) + "/" + str(bday_year)
print(bday_str1)
bday_str2 = str(bday_year) + "-" + str(bday_month) + "-" + str(bday_day)
print(bday_str2)

# Boolean COnditions
b1 = 2 < 5
b2 = 2 > 5
b3 = 3 >= 1
b4 = 3 <= 1
b5 = 2 == 1
b6 = 2 != 1
print(b1)
print(b2)
print(b3)
print(b4)
print(b5)
print(b6)

# Building compound boolean conditions
age = 12
with_adult = False
# allowed = (age >= 18) or (age < 18 and age >= 16 and with_adult)
allowed = (age >= 18) or (age >= 16 and with_adult)
print(allowed)

# Negating Boolean Conditions
rejected = not allowed
print(rejected)
rejected = not ((age >= 18) or (age >= 16 and with_adult))
print(rejected)

# If-Elif-Else Statements
if allowed:
    print("Welcome to the event!")

if (age >= 18) or (age >= 16 and with_adult):
    print("Welcome to the event!")

if (age >= 18) or (age >= 16 and with_adult):
    print("Welcome to the event!")
else:
    print("Sorry, you cannot enter!")

if age >= 18:
    print("Welcome to the event!")
elif age >= 16 and with_adult:
    print("Welcome to the event, stay with your adult!")
else:
    print("Sorry, you cannot enter!")

if age < 5:
    print("Pre-school")
elif age < 13:
    print("Middle school")
elif age < 18:
    print("High school")
elif age <= 22:
    print("College")
else:
    print("Post-college")

if age < 5:
    print("Pre-school")
elif age >= 5 and age < 13:
    print("Middle school")
elif age >= 13 and age < 18:
    print("High school")
elif age >= 18 and age <= 22:
    print("College")
else:
    print("Post-college")

if age < 5:
    print("Pre-school")
if age < 13:
    print("Middle school")
if age < 18:
    print("High school")
if age <= 22:
    print("College")
else:
    print("Post-college")

# Ternary Operator (if-else shortcut)
age = 20

age_group = ""
if age >= 18:
    age_group = "adult"
else:
    age_group = "child"
print(age_group)

age_group = "adult" if age >= 18 else "child"

# While Loops
n = 32
k = 0
while n > 1:
    k += 1
    n /= 2
print(k)

a = 2
b = 3
result = a
i = 1
while i < b:
    result *= a
    i += 1
print(result)

# For Loops
result = a
for i in range(1,b):
    result *= a
print(result)

n = 10
s = 0
for i in range(n):
    s += i + 1
print(s)

# Nested loops
for i in range(1,13):
    for j in range(1,13):
        print(i*j)


# Printing Multiple Data Types
first_name = "John"
last_name = "Smith"
age = 13
pstr = first_name + " " + last_name + " is " + str(age) + " years old!"
print(pstr)
print(first_name + " " + last_name + " is " + str(age) + " years old!")

# Printing on the same line
print(1, end="")
print(2.3)

print(1, end=" ")
print(2.3)

# The input() function
# name_in = input("Enter your name! ")
# print(name_in)

# String to List (split())
# info = input("Enter your first name, last name, age, and gender separated by commas: ")
# info_list = info.split(",")
# print(info_list)

# Indexing a List
ls = [1, 2, 3]
for i in range(len(ls)):
    ls[i] *= -1
print(ls)

# Two dimensional lists
identity = [[1, 0, 0],[0, 1, 0],[0, 0, 1]]
print(type(identity[0]))
print(type(identity[1]))
print(type(identity[2]))

print(identity)

for i in range(3):
    for j in range(3):
        print(identity[i][j],end=" ")
    print("")

# Tuple, the Immutable List
tup = (1,2,3,4,5)
print(type(tup))

# Copying Lists and the Shallow Copy
ls = [1,2,3,4,5]
ls2 = ls

ls2[2] = 0
print(ls[2])

ls = [1,2,3,4,5]
ls2 = [1,2,3,4,5]
ls2[2] = 0
print(ls[2])

# Why do we need functions? (Introduction to Modularity)
def y(x):
    return 3*x + 5

print(y(3))

def z(x,y):
    return 3*x + 2*y + 5

print(z(3,7))

# Parameters v. Argument

for xi in range(1,11):
    print(y(xi))

# Variables inside a function (and Scope)
def yp(x):
    return 5*x**3 + 4*x**2 + 3*x + 6

def yp2(x):
    cube_term = 5*x**3
    quad_term = 4*x**2
    lin_term = 3*x
    return cube_term + quad_term + lin_term + 6

print(yp(1))

# The return statement (do we need it?)
def psum(n):
    if n < 1:
        return 0

    s = 0
    for i in range(1,n+1):
        s += i
    return s

def psum2(n):
    s = 0
    if n >= 1:
        for i in range(1,n+1):
            s += i
    return s

print(psum(2))
print(psum2(2))

# Functions that Edit Input
def print_list(ls):
    for i in range(len(ls)):
        print(ls[i])

l1 = [1,2,3]
print_list(l1)

def negate_list(ls):
    for i in range(len(ls)):
        ls[i] *= -1

negate_list(l1)

# multiple return values
def roots(n):
    rt = n**0.5
    return (rt, -1*rt)

out = roots(25)
print(type(out))
print(out)

def roots2(n):
    rt = n**0.5
    return rt, -1*rt
rp, rn = roots2(25)
print(rp, rn)

# Constants II
environment = []
for i in range(3):
    environment.append([0, 0, 0, 1, 0, 0, 0])
environment.append([1]*7)
for i in range(3):
    environment.append([0]*7)
print(environment)
