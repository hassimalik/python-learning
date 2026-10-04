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



