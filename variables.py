name = "sai"
print(name)

_number = 10
print(_number)

# _number = "sai" # this will throw an error because we are trying to reassign a variable to a different data type
first_name = "Venkat"
last_name = "Sai"
full_name = first_name + " " + last_name
print(full_name)

#int x = 10 # this will throw an error because python does not have explicit type declaration
x = 10


total = 0
for i in range(1, 10):
    total += i
    print(total)


name = "sai"
for i in range(0, len(name)):
    print(name[i])
    

count = 1
while count <= 10:
    print(count)
    count += 1
    

# Nested Loops
for i in range (1,5):
    for j in range(1,5):
        print(i,j)
        
"""Explanation of Logic   
The range(1, 5) Function: In Python, the range(start, stop) function includes the starting number but excludes the stopping number. Therefore, range(1, 5) generates the sequence 1, 2, 3, 4.
Outer Loop (i): The outer loop starts with i = 1. It will not move to i = 2 until the inner loop has finished all its iterations.
Inner Loop (j): For every single value of i, the inner loop runs completely from 1 to 4. This results in a total of 16 printed lines ()."""
