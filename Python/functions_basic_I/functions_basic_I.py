#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# This will return the number 5.


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# This will print an error message because the function 'number_of_days_in_a_week_silicon_or_triangle_sides()' is not defined yet.


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# This will return the number 5, the second return statement will never get run.


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# This will return the number 5. the second return statement will never get run.


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# Nothing is being returned from the function therefore it will print 5 while it runs the function and then it will print none.


# #6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# This will create and erro because nothing is returned from the function and therefore can not complete the equation in the print statement/

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# This will print the string "25"


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# This will return 100 then 10.


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# This will return 7, 14, 21 on different lines.


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# This will return 8.


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# This will print 500, 500, 300, 500


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# This will print 500, 500, 300, 500. The return statement is does not do anything here.


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# This will print 500 twice on separate lines and then 300 twice on subsequent lines


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# This will print 1 then 3 then 2 on different lines.


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# This will print 1 then 3 then 5 then 10 on different lines