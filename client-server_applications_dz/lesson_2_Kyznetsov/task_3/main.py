"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""
import yaml


dict_yaml = {
    "list_key": ["el_1", "el_2", "el_3", "el_4"],
    "int_key": 3,
    "dict_key": {
        "liter_1": "\u9748",
        "liter_2": "\u8383",
        "liter_3": "\u8364",
        "liter_4": "\u9201"
    }
}


with open('yaml_file.yaml', 'w') as y_f:
    yaml.dump(dict_yaml, y_f, allow_unicode = True, default_flow_style = True)

with open('yaml_file.yaml') as y_f:
    print(y_f.read())
