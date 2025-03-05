import csv
import numpy

f = open('Daejeon_temp.csv', 'r', encoding='cp949')
data = csv.reader(f)
header = next(data)
print(header)

target_date = [12, 1, 2]
min_avg_min_temp = 999
min_avg_min_temp_date = ''
min_temps = [[], [], []]


for row in data:  
    if row[-2] != '':
        month = int(row[0].split('-')[1])
        if month in target_date:
            min_temps[target_date.index(month)].append(float(row[-2]))
f.close()

for index, min_temp in enumerate(min_temps):
    avg_min_temp = numpy.mean(min_temp)
    if avg_min_temp < min_avg_min_temp:
        min_avg_min_temp = avg_min_temp
        min_avg_min_temp_date = target_date[index]

min_avg_min_temp = round(min_avg_min_temp, 1)

print("기상 관측 이래, 대전의 12월, 1월, 2월 중 최저 기온의 평균이 가장 낮은 달은", min_avg_min_temp_date, "월로,", min_avg_min_temp, "도 였습니다.")