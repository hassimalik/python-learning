numbers = [1,2,3,4,5]

squares = []

for number in numbers :
    squares.append(number ** 2)
print (squares)


squares = [number ** 2 for number in numbers]
squares = {number : number ** 2 for number in numbers}


numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)


def greet():
    print("Hello Hassaan")

greet()

def add_numbers(a, b):
    print(a+b)

add_numbers(50, 40)


def add(a, b):
    return a + b

result = add(10, 20)
print(result)



def greet(name="Guest"):
    print("Hello", name)

greet()

greet("Hassaan")


def create_user(name, age):
    return{
        "name": name,
        "age" : age
    }


user = create_user("Hassaan", 21)
print(user)

def add(*args):
    print(args)

add(10, 20)
add(10, 20, 30)


def add(*args):
    total = 0

    for number in args:
        total += number
    return total

print(add(10, 20))


def calculate_sum(*args):
    total = 0
    for number in args:
        total += number
    return total

print(calculate_sum(40, 20))


