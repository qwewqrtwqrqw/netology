import csv

# Функция для формирования описания покупателя
def create_description(row):
    name = row["name"]
    sex = row["sex"]
    age = row["age"]
    device_type = row["device_type"]
    browser = row["browser"]
    bill = row["bill"]
    region = row["region"]

    description = f"Пользователь {name} {sex} пола, {age} лет совершил покупку на {bill} у.е. с {device_type} браузера {browser}. Регион, из которого совершалась покупка: {region}."

    return description

# Загрузка данных из CSV-файла
with open('покупатели.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    descriptions = []
    for row in reader:
        description = create_description(row)
        descriptions.append(description)

# Запись описаний в TXT-файл
with open('описания_покупателей.txt', mode='w', encoding='utf-8') as file:
    for description in descriptions:
        file.write(description + "\n")