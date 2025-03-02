import csv
import numpy

f = open('Daejeon_temp.csv', 'r', encoding='cp949')
data = csv.reader(f)
header = next(data)
print(header)

max_avg_temp_range = 0
max_avg_temp_range_date = ''
temp_ranges = [[], [], [], [], [], [], [], [], [], [], [], []]


for row in data:  
    if row[-2] != '' and row[-1] != '':
        temp_range = float(row[-1]) - float(row[-2])
        temp_ranges[int(row[0].split('-')[1])-1].append(temp_range)
f.close()

for index, temp_range in enumerate(temp_ranges):
    avg_temp_range = numpy.mean(temp_range)
    if avg_temp_range > max_avg_temp_range:
        max_avg_temp_range = avg_temp_range
        max_avg_temp_range_date = index + 1

max_avg_temp_range = round(max_avg_temp_range, 1)

print("기상 관측 이래, 대전의 최고 기온과 최저 기온 차의 평균이 가장 높은 달", max_avg_temp_range_date,"월로,", max_avg_temp_range, "도 였습니다.")