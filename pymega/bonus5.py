waiting_list = ["sen", "ben", "john"]
waiting_list.sort()


for i, item in enumerate (waiting_list):
    row = f"{i + 1}.{item.capitalize()}"
    print(row)