"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

data_list = [
{'name': 'Зинаиды', 'age': '21', 'job': 'Джуниор Доярка'},
{'name': 'Стефан', 'age': '23', 'job': 'Мидл Плотник'},
{'name': 'Фекла', 'age': '29', 'job': 'Сеньер Доярка'},
{'name': 'Виссарион', 'age': '31', 'job': 'Зоотехник'},
{'name': 'Алексия', 'age': '25', 'job': 'Джуниор Повар'}
]



def main():
   
   with open('export_data_list.csv', 'w', encoding='utf=8') as f:
       fields = ['name', 'age', 'job']
       writer = csv.DictWriter(f, fields, delimiter=';')
       writer.writeheader()
       for _ in data_list:
           writer.writerow(_)

if __name__ == "__main__":
    main()
