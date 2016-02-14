import sys

# выводим на экран список всех аргументов
for arg in sys.argv[1:]:
    if len(arg)%3==0:
        print(arg)
