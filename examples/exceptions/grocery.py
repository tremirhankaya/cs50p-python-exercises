grocery_list = {}
while True:
    try:
        item = input().upper()
        if item in grocery_list:
            grocery_list.update({item: grocery_list[item] + 1})
        else:
            grocery_list.update({item: 1})
    except EOFError:
        break

for item in sorted(grocery_list):
    print(f"{grocery_list[item]} {item}")
