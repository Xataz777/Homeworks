import time
from threading import Thread


def write_words(word_count, file_name):
    for i in range(1, word_count+1):
        with open(file_name, 'a') as file:
            print(f'Какое-то слово №{i}', file=file)
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


start1 = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end1 = time.time()
time1 = end1 - start1
print(f'Работа потоков: {time1}')

start2 = time.time()

thr1 = Thread(target=write_words, args=(10, 'example5.txt'))
thr2 = Thread(target=write_words, args=(30, 'example6.txt'))
thr3 = Thread(target=write_words, args=(200, 'example7.txt'))
thr4 = Thread(target=write_words, args=(100, 'example8.txt'))

thr1.start()
thr2.start()
thr3.start()
thr4.start()

thr1.join()
thr2.join()
thr3.join()
thr4.join()

end2 = time.time()
time2 = end2 - start2
print(f'Работа потоков: {time2}')