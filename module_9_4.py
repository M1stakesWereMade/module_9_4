lambda x, y: [x[i] == y[i] for i in range(min(len(x), len(y)))]

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: [x[i] == y[i] for i in range(min(len(x), len(y)))], first, second))
print(result)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a') as file:
            for data in data_set:
                file.write(str(data) + '\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])