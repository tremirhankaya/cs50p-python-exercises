
def toSnakeCase(s):

    my_list=[]
    for c in s:
        if c.isupper():
            my_list.append('_')
            
        my_list.append(c.lower())

    return(''.join(my_list))


def main():
  s=input('Camel Case: ')
  print('snake_case: '+toSnakeCase(s))

main()