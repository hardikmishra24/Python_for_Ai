def greet(name):
    print("Hello", name)
greet("Hardik") 


# Function using a return statement
def add(a, b):
    print(a + b)
result = add(3, 5)
print(result)


# keyword arguments
def students(name, age):
    print(name, age)
students( "Hardik", 20)

#Arbitrary Arguments (*args) use *args when you don't know how many positional arguments the user will pass.
def numbers(*args):
    print(args)
numbers(10, 20, 30, 40, 50)


#Keyword Arbitrary Arguments (**kwargs) Use **kwargs when you don't know how many keyword arguments will be passed.)
def function_name(**kwargs):
    print(kwargs)
function_name(name = "hardik", age = 20, city = "Jaipur")