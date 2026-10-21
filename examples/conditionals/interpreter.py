expression=input("Enter the expression: ")
x, y, z = expression.split(" ")
x=float(x)
z=float(z)
match y:
    case "+":
        print(f"{x + z:.1f}")
    case '-':
        print(f"{x - z:.1f}")
    case '*':
        print(f"{x*z:.1f}")
    case '/':
        if z==0:
            print('You cannot divide a number by 0')
        else:
            print(f"{x/z:.1f}")

