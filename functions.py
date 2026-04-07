def greet():
    print("Hello World")
greet()

def add_numbers(a, b):
    return a + b
print(add_numbers(10, 20))

def multiply_numbers(a, b):
    return a * b
print(multiply_numbers(10, 20))

numbers = [1,2,3,4,5,6,7,8,9,10]

def even_num(number):
    return number % 2 == 0
print(list(filter(even_num, numbers)))


def odd_num(number):
    return number % 2 != 0
print(list(filter(odd_num, numbers)))

employees = [{
    "name":"user1", "age":30, "salary":10000
}, {
    "name":"user2", "age":25, "salary":20000
},
{
    "name":"user3", "age":35, "salary":30000
},
{
    "name":"user4", "age":40, "salary":40000
}
]

def get_Employee(employee):
    return employee["name"] + " is " + str(employee["age"]) + " years old and earns " + str(employee["salary"])

print(list(map(get_Employee, employees)))