import time
import datetime
class MyManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        self.time = datetime.datetime.now()
        print('Время запуска кода {}'.format(self.time.time()))
        self.file = open(self.file_path)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        self.new_time = datetime.datetime.now()
        self.delta = self.new_time - self.time
        print('Время на выполнение кода {}'.format(self.delta))
        print('Время окончания работы кода {}'.format(self.new_time.time()))

with MyManager('recipes.txt') as file:
    print('Содержимое файла:')
    for line in file:
        print(line.strip())
        time.sleep(0.3)