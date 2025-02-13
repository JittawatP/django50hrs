def hello():
    print("Hello! My name is Somchai.")

# hello()
def helloName(name):
    print("Hello! My name is "+ name)

# helloName("Bank")
# helloName("Somsri")
# helloName("Sompong")

def helloNameAge(name,age):
    print(f"Hello! My name is {name}.")
    print(f"I'm {age} years old.")

# helloNameAge("John",40)
# helloNameAge(name="Somchai", age=50)
# helloNameAge(age=80, name="Somying")

# Optional

def helloOptional(name, age=60):
    print(f"Hello! My name is {name}.")
    print(f"I'm {age} years old.")

# helloOptional("Somsuk")
# helloOptional("Somying",30)

def addNumber(x,y):
    return x+y

sum = addNumber(15,25)
# print(sum)

def calculate(z):
    return addNumber(15,25) * z

result = calculate(5)
print(result)



