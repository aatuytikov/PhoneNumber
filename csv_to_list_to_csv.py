import csv

file = list(csv.reader(open('phone_numbers.csv'))) # Открыл файл со списко номеров с сайта mtt

phone_list = [] # Создал пустой список для предварительного хранения
new_phone_list = [] # Cоздал пустой список для хранения только номеров
new_phone_list_final = [] # Очередной промежуточный список
new_phone_list_final_2 = [] # Надеюсь последний вложенный список

check_true = 0 #Счетчик индекса корректной строки
check_false = 0 #Счетчик индекса некоректной строки
for row in file: # Цикл для перебора строк файла phone_number.csv и сохранения по 2 строки пропуская следующие 4
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

for i in phone_list: #Цикл устранения вложенности списка
    for j in i:
        new_phone_list.append(j)


index = 0
for i in new_phone_list:
    if index % 2 == 0:
        new_phone_list_final.append(i)
        index += 1
    else:
        new_phone_list_final.append(i.split('-'))
        index += 1

index_2 = 0
for i in new_phone_list_final: #Цикл устранения вложенности списка
    if index_2 % 2 != 0:
        for j in i:
            new_phone_list_final_2.append(j)
        index_2 += 1
    else:
        new_phone_list_final_2.append(i)
        index_2 += 1
        continue



file = open('new_phone_list.csv', 'w')

index_3 = 0
for i in new_phone_list_final_2: #Сохрание нового файла с таблицой код + диапазон номеров
    if index_3 % 3 == 0:
        file.write(new_phone_list_final_2[index_3] + ',' + new_phone_list_final_2[index_3 + 1] + ',' + new_phone_list_final_2[index_3 + 2] + '\n')
    index_3 += 1







