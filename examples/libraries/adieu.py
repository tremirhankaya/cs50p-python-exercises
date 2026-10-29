import inflect
p = inflect.engine()
user_list=[]


while True:
    try:
        user_input=input("Name: ")
        user_list.append(user_input)
    except EOFError:
        break


print(f"Adieu, adieu, to {p.join(user_list)}")


    