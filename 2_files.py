"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        content_split = content.split(' ')
        print(f'Количество слов в тексте: {len(content_split)}')
        #print(content)
        print(f'Длина строки состовляет: {len(content)} симоволов')
        content_chng = content.replace('.', '!')
        print(f"Текст с замененными на восклицательный знак точками:\n{content_chng}")

    with open('referat2.txt', 'w', encoding='utf=8') as x:
        content2 = x.write(content_chng)

if __name__ == "__main__":
    main()
