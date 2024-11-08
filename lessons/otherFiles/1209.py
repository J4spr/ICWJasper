# pass code block temporarly
for i in range(0, 4):
    pass


def sumof(num1=0, num2=0):
    return (num1 + num2)


def sumofmany(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum


def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


print(sumof(10, 1))
print(sumof(num1=7, num2=8))
print(sumof())
print(sumofmany(1, 2, 10, 20))
print(factorial(4))


def outerfunction():
    variable = "outer"

    def innerfunction():
        variable = "inner"

    innerfunction()
    print(variable)


outerfunction()
