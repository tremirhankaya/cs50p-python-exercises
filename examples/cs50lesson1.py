#x=int(input('Whats the X value? '))
#y=int(input('Whats the Y value? '))

#print(f'{x/y:.5f}')

def main():
    print(hello('Alice', "25"))
    print(hello('Bob', 30))
    print(square(3))


def hello(name, age):
    print(f'Hello {name}, you are {age}!')
    print (type(age))
    return name 
def square(x):
    return pow(x, 2)
main()