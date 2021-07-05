import csv, numpy

arr1 = []
arr2 = []

with open("dwarf.csv", "r") as f1:
    reader1 = csv.reader(f1)
    arr1 = [i for i in reader1]

with open("bright_stars.csv", "r") as f2:
    reader2 = csv.reader(f2)
    arr2 = [i for i in reader2]

header1, data1 = arr1[0], arr1[1::]
header2, data2 = arr2[0], arr2[1::]

headers = header1 + ["Luminosity"]

data = data1 + data2

with open("final-data.csv","w+", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data)
