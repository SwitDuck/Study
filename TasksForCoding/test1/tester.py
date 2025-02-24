import argparse as ar
import os 
import click

@click.group()
def cli():
    rename()
    file_copy()

def rename():
    parser = ar.ArgumentParser(
        prog="Renamer",
        description="Программа для переименования файла",
        epilog="Использование: python script.py --rename старое_имя новое_имя"
    )

    parser.add_argument("-r", "--rename", nargs=2, metavar=('OLD', 'NEW'),
                        help="Переименовывает файл: укажите старое и новое имя.")

    args = parser.parse_args()

    if args.rename:
        old_name, new_name = args.rename
        if not os.path.exists(old_name):
            print(f"Ошибка: файл '{old_name}' не найден.")
            return
        
        try:
            os.rename(old_name, new_name)
            print(f"Файл '{old_name}' переименован в '{new_name}'")
        except OSError as e:
            print(f"Ошибка при переименовании: {e}")
    else:
        parser.print_help()

if __name__ == "__main__":
    rename()
def file_copy():
    ...
def delete_file():
    ...
def find_text_in_file():
    ... 