import csv

f = open('Daejeon_temp.csv', 'r', encoding='cp949')
data = csv.reader(f)
header = next(data)
print(header)
for row in data:
    
    print(row)
f.close()
