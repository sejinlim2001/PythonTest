import csv

f1 = open('Daejeon_temp.csv', 'r', encoding='cp949')
f2 = open('Daegu_temp.csv', 'r', encoding='cp949')

data1 = csv.reader(f1)
data2 = csv.reader(f2)

header1 = next(data1)
header2 = next(data2)

print(header1)
print(header2)

daejeon_max_temps = []
daejeon_dates = []

daegu_max_temps = []
daegu_dates = []

count = 0

for row1 in data1:
    daejeon_max_temps.append(row1[-1])
    daejeon_dates.append(row1[0])

for row2 in data2:
    daegu_max_temps.append(row2[-1])
    daegu_dates.append(row2[0])

f1.close()
f2.close()

if daejeon_dates == daegu_dates:
    for index in range(len(daejeon_max_temps)):
        daejeon_max_temp = daejeon_max_temps[index]
        daegu_max_temp = daegu_max_temps[index]

        if daejeon_max_temp != '' and daegu_max_temp != '':
            daejeon_max_temp = float(daejeon_max_temp)
            daegu_max_temp = float(daegu_max_temp)
            if daejeon_max_temp > daegu_max_temp:
                count = count + 1

print("기상 관측 이래, 대구의 최고 기온보다 대전의 최고 기온이 높은 날은 총", count, "일 입니다.")