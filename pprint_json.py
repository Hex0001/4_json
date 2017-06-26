# import json
from sys import argv


def load_data(filepath):
    f = open(filepath, encoding="utf8")
    return f.read()


def pretty_print_json(data):
    k = 0   # Множитель отступа
    flag = False    # Используется для проверки прохождения по нередактируемой области в " "
    data = list(data)
    for i in range(len(data)):
        if flag:
            if data[i] == '"':
                flag = False
            continue
        elif data[i] == '{' or data[i] == '[':
            k += 1
            data[i] = data[i] + '\n' + '    ' * k
        elif data[i] == '}' or data[i] == ']':
            k -= 1
            data[i] = '\n' + '    ' * k + data[i]
        elif data[i] == ',':
            data[i] = data[i] + '\n' + '    ' * k
        elif data[i] == '"':
            flag = True
        elif data[i] == ':':
            data[i] += ' '
    data = ''.join(data)
    return data

if __name__ == '__main__':
    print(pretty_print_json(load_data(argv[1])))