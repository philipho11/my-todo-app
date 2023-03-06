def get_average():
    with open("data.txt", "r") as file:
        vals = file.readlines()

    temps = vals[1:]
    temps = [float(i) for i in temps]
    avg = sum(temps) / len(temps)

    return avg


average = get_average()
print(average)
