import csv

with open(r'C:\Users\Biswajeet\Desktop\example.csv') as csvfile:
    readcsv=csv.reader(csvfile,delimiter=',')

dates=[]
color=[]
for row in readcsv:
    dates=row[0]
    color=row[3]

    dates.append(dates)
    color.append(color)

print(dates)
print(color)

