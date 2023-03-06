filenames = ["1.doc", "1.report", "1.presentation"]

# new_filenames = []
# for filename in filenames:
#     new_filenames.append(filename + ".txt")

filenames = [filename.replace('.','-') + ".txt" for filename in filenames]

print(filenames)
temperatures = [10, 12, 14]

file = open("file.txt", 'w')

file.writelines(str(temperatures))

