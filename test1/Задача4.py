'''Задача 4: Мини-CLI утилита
Напишите программу, которая представляет собой мини-CLI утилиту для работы с файлами. Она должна:
Копировать файл из одного места в другое.
Удалять указанный файл.
Переименовывать файл.
Искать текст внутри файлов определенного формата в заданной директории и поддиректориях.
Подсказки:
Используйте модули os, shutil и glob.
Реализуйте интерфейс командной строки с помощью argparse.'''
import os
import shutil as sh 
import glob
import click 

class main_functions():
        
    def rename(path):
        os.rename(path)
    def copy_file():
        sourse = "A:/"
        destination = "C:/"
        sh.move(sourse, destination)
    def permission_checker(file_path):
        default_permission = True
        linux_permission = "rwrwrw"
        if not os.access(file_path, os.R_OK):
            return default_permission
class main():
    funcs = main_functions()
    rename = funcs.rename()
    @click.group()
    def cli():
        rename
        file_copy()

def changer():
    print("1)Копировать файл\n2)Удалить файл\n3)Переименовать файл\n4)Найти текст")
    znachenie = int(input("Введите значение от 1 до 4: "))
    if znachenie == 1:
        print("1")
    elif znachenie == 2:
        print("2")
    elif znachenie == 3:
        print("3")
    elif znachenie == 4:
        print("4")
    else:
        print("Неверное значение, введите значение от 1 до 4")
        return changer()


        
