import csv

file = list(csv.reader(open('phone_numbers.csv')))

phone_list = []
new_phone_list = []
check_true = 0
check_false = 0

for row in file:
    if check_true == 0 or check_true == 1:
        phone_list.append(row)
        check_true += 1
    elif check_true == 2:
        if check_false == 3:
            check_true = 0
            check_false = 0
        else:
            check_false += 1
            continue

for i in phone_list:
    for j in i:
        new_phone_list.append(j)

file = open('new_phone_list.csv', 'w')

index = 0
for i in new_phone_list:
    if index % 2 == 0:
        file.write(new_phone_list[index] + ',' + new_phone_list[index + 1] + '\n')
        print(i)
    index += 1







