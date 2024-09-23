from pprint import pprint

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    string_position = {}
    string_num = 0
    start_pos_str = file.seek(0)
    for item in strings:
        file.write(item+'\n')
        string_num +=1
        key = (string_num, start_pos_str)
        string_position[key] = item
        start_pos_str = file.tell()
    file.close()
    return string_position

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

file_name = './test.txt'
result = custom_write(file_name, info)
for elem in result.items():
  print(elem)