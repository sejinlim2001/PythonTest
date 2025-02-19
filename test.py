import csv

f = open('deajeon_temp.csv', 'r', encoding='cp949')
data = csv.reader(f)
header = next(data)
print(header)
f.close()

print("Hello, World!")