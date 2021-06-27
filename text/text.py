import os


path = os.getcwd()
directory = [f for f in os.listdir(path) if f.endswith('.txt')]


def count_lines(file_name):
    dict_lines = {}
    for name in file_name:
        with open(f'{name}', encoding='utf-8') as file:
            lines = file.readlines()
        dict_lines[name] = len(lines)
    doc_sort = {}
    doc_sorted = sorted(dict_lines, key=dict_lines.get)
    for f in doc_sorted:
        doc_sort[f] = dict_lines[f]
    return doc_sort
    # print(dict_lines)
    # print(doc_sorted)
    # print(doc_sort)


# count_lines(directory)
def create_file(name_file):
    with open(f'{name_file}', 'w+', encoding='utf-8') as file:
        file.write('')


# create_file('all_files.txt')


def write_all_files(file):
    dict_file = count_lines(directory)
    keys = []
    values = []
    for key, value in dict_file.items():
        keys.append(key)
        values.append(value)
    for a in range(len(keys) - 1):
        with open(f'{keys[0]}', 'a', encoding='utf-8') as one,  open(f'{keys[a+1]}', encoding='utf-8') as two:
            one.write(f'{keys[a + 1]}\n')
            one.write(f'{values[a + 1]}\n')
            for id_line, line in enumerate(two, start=1):
                one.write(f'Строка номер {format(id_line)} Файл номер {keys[a + 1].rsplit(".",1)[0]} \n')


write_all_files(create_file('all_files.txt'))
