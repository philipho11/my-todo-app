password = input("Please input a password: ")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

print(result)

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digits"] = digit

print(result)


upper = False
for i in password:
    if i.isupper():
        upper = True

result["upper-case"] = upper

print(result)

if all(result.values()):
    print("You input a strong password!")
else:
    print("You input a weak password!")