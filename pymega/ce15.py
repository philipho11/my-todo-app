import glob
import csv
import shutil
import webbrowser


#glob demo
myfiles = glob.glob("*.txt")
print (myfiles)

#shutil demo
shutil.make_archive("output", "zip", "*.txt")

#webbrowser demo
user_term = input("Enter a search term: ")
webbrowser.open('https://www.google.com/search?q=' + user_term)

#csv demo
with open('weather.csv') as csvfile:
    weather = list(csv.reader(csvfile))

city = input("Enter a city: ")
for row in weather[1:]:
    if row[0] == city:
        print(row[1])

