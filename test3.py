import csv

f = open('Daejeon_temp.csv', 'r', encoding='cp949')
data = csv.reader(f)
header = next(data)
print(header)
max_temp = -999
max_date = ''
for row in data:
    if row[-1] == '':
        row[-1] = -999
    row[-1] = float(row[-1])
    if max_temp < row[-1]:
        max_temp = row[-1]
        max_date = row[0]
f.close()

print("기상 관측 이래, 대전의 최고 기온이 가장 높았던 날은", max_date,"로,", max_temp, "도 였습니다.")
