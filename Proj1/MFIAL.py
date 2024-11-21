'''import subprocess as sub
# Исходный словарь с параметрами команды
command_list = {
    'useradd': [
        'useradd',  # Основная команда
        '-b — базовый каталог',
        '-d — домашний каталог',
        '-e — дата блокировки учётной записи',
        '-f — блокировка после создания',
        '-g — группа пользователя',
        '-p — пароль пользователя',
        '-u — идентификатор пользователя'
    ],
    'pdpl-user': [
        'pdpl-user',
        '-l',
        '-i',
        '-c',
        '-d',
        '-z'
    ],
    'pdpl-file': [
        'pdpl-file',
        ''
    ]
}
def check(vvod):
    if vvod == 'exit':
        main()
        return True

def main():
    def create_user():
        while True:
            if input("Введите exit чтобы вернуться назад: \nНажмите enter чтобы продолжить ") == "exit":
                    main()
                    break
            # Начинаем формирование команды с основного имени пользователя
            command_with_params = ['useradd']
            
            # Определяем список параметров и их запросов
            user_add_params = [
                ('Базовый каталог: ', '-b'),
                ('Домашний каталог: ', '-d'),
                ('Дата блокировки учётной записи (дд:мм:гг): ', '-e'),
                ('Блокировать учётную запись после создания? (y/n): ', '-f'),
                ('Группа пользователя: ', '-g'),
                ('Пароль пользователя: ', '-p'),
                ('Идентификатор: ', '-u')
            ]
            
            # Перебираем параметры и запрашиваем ввод
            for i, (prompt, flag) in enumerate(user_add_params):
                
                user_input = input(prompt)
                if check(user_input)==True:
                    break    
                # Если параметр должен быть пропущен
                if not user_input:
                    print(f"Параметр '{flag}' пропущен.")
                    continue

                # Обработка специального параметра '-f'
                if i == 3:  # Если это параметр блокировки
                    if user_input.lower() == 'y':
                        command_with_params.append(flag)  # Добавляем только флаг без значения
                    elif user_input.lower() == 'n':
                        print(f"Параметр '{flag}' пропущен.")
                    continue

                # Добавляем флаг и значение параметра
                command_with_params.extend([flag, user_input])
            print("Введите имя пользователя:")
            user_name = input("Ввод: ")
            command_with_params.extend([user_name])
            # Вывод собранной команды перед выполнением
            print("Выполняем команду:", " ".join(command_with_params))

            # Выполнение команды
            try:
                print(" ".join(command_with_params))
                #sub.run(command_with_params)
            except Exception as e:
                print(f"Ошибка при выполнении команды: {e}")
                
    # Основное меню функции
    def user_modify():
        print('modify')
    def mandatory_manage():
        print('manage')
    print("Выберите параметр который хотите выполнит \n1)Добавление пользователя \n2)Модификация пользователя \n3)Назад")
    while True:
        try:
            x = int(input("ввод: "))
            if x == 1:
                create_user()
            elif x == 2:
                user_modify()
            elif x == 3:
                mandatory_manage()
            else: return
            break
        except ValueError:
            print("Введите цифру 1-2")
main()'''

import subprocess as sub

# Словарь с параметрами команд
command_list = {
    'useradd': [
        'useradd',  # Основная команда
        '-b — базовый каталог',
        '-d — домашний каталог',
        '-e — дата блокировки учётной записи',
        '-f — блокировка после создания',
        '-g — группа пользователя',
        '-p — пароль пользователя',
        '-u — идентификатор пользователя'
    ],
    'pdpl-user': [
        'pdpl-user',
        '-l — установить уровень конфиденциальности',
        '-i — установить уровень целостности',
        '-c — создать пользователя',
        '-d — удалить пользователя',
        '-z — сбросить уровни'
    ],
    'pdpl-file': [
        'pdpl-file',
        '-l — установить уровень конфиденциальности для файла',
        '-i — установить уровень целостности для файла'
    ],
    'usercat': [
        'usercat',
        '-a — добавить категорию',
        '-d — удалить категорию',
        '-m — изменить категорию',
        '-p — задать привилегии пользователя'
    ]
}

def check(vvod):
    if vvod == 'exit':
        main()
        return True

def main():
    def create_user():
        while True:
            if input("Введите exit чтобы вернуться назад: \nНажмите enter чтобы продолжить ") == "exit":
                main()
                break
            # Начинаем формирование команды с основного имени пользователя
            command_with_params = ['useradd']
            
            # Определяем список параметров и их запросов
            user_add_params = [
                ('Базовый каталог: ', '-b'),
                ('Домашний каталог: ', '-d'),
                ('Дата блокировки учётной записи (дд:мм:гг): ', '-e'),
                ('Блокировать учётную запись после создания? (y/n): ', '-f'),
                ('Группа пользователя: ', '-g'),
                ('Пароль пользователя: ', '-p'),
                ('Идентификатор: ', '-u')
            ]
            
            # Перебираем параметры и запрашиваем ввод
            for i, (prompt, flag) in enumerate(user_add_params):
                user_input = input(prompt)
                if check(user_input) == True:
                    break
                # Если параметр должен быть пропущен
                if not user_input:
                    print(f"Параметр '{flag}' пропущен.")
                    continue

                # Обработка специального параметра '-f'
                if i == 3:  # Если это параметр блокировки
                    if user_input.lower() == 'y':
                        command_with_params.append(flag)  # Добавляем только флаг без значения
                    elif user_input.lower() == 'n':
                        print(f"Параметр '{flag}' пропущен.")
                    continue

                # Добавляем флаг и значение параметра
                command_with_params.extend([flag, user_input])
                
            # Ввод имени пользователя
            print("Введите имя пользователя:")
            user_name = input("Ввод: ")
            command_with_params.append(user_name)

            # Вывод собранной команды перед выполнением
            print("Выполняем команду:", " ".join(command_with_params))

            # Выполнение команды
            try:
                print(" ".join(command_with_params))
                # sub.run(command_with_params)
            except Exception as e:
                print(f"Ошибка при выполнении команды: {e}")

    def user_modify():
        print('Функция для модификации пользователя.')

    def mandatory_manage():
        while True:
            print("\nВыберите действие с мандатным контролем:\n1) Установить уровни для пользователя (pdpl-user)\n2) Установить уровни для файла/каталога (pdpl-file)\n3) Управление привилегиями и категориями (usercat)\n4) Назад")
            choice = input("Ввод: ")

            if choice == "1":
                # Работа с pdpl-user
                pdpl_user_command = ['pdpl-user']
                pdpl_user_params = [
                    ('Уровень конфиденциальности: ', '-l'),
                    ('Уровень целостности: ', '-i'),
                    ('Создать пользователя? (y/n): ', '-c'),
                    ('Удалить пользователя? (y/n): ', '-d'),
                    ('Сбросить уровни? (y/n): ', '-z')
                ]
                
                for prompt, flag in pdpl_user_params:
                    user_input = input(prompt)
                    if user_input.lower() == 'y':
                        pdpl_user_command.append(flag)
                    elif user_input and flag not in ('-c', '-d', '-z'):
                        pdpl_user_command.extend([flag, user_input])
                
                print("Выполняем команду:", " ".join(pdpl_user_command))
                # sub.run(pdpl_user_command)

            elif choice == "2":
                # Работа с pdpl-file
                pdpl_file_command = ['pdpl-file']
                pdpl_file_params = [
                    ('Уровень конфиденциальности для файла: ', '-l'),
                    ('Уровень целостности для файла: ', '-i')
                ]

                for prompt, flag in pdpl_file_params:
                    user_input = input(prompt)
                    if user_input:
                        pdpl_file_command.extend([flag, user_input])

                print("Выполняем команду:", " ".join(pdpl_file_command))
                # sub.run(pdpl_file_command)

            elif choice == "3":
                # Работа с usercat
                usercat_command = ['usercat']
                usercat_params = [
                    ('Добавить категорию? (y/n): ', '-a'),
                    ('Удалить категорию? (y/n): ', '-d'),
                    ('Изменить категорию? (y/n): ', '-m'),
                    ('Задать привилегии пользователя? (y/n): ', '-p')
                ]

                for prompt, flag in usercat_params:
                    user_input = input(prompt)
                    if user_input.lower() == 'y':
                        usercat_command.append(flag)

                print("Выполняем команду:", " ".join(usercat_command))
                # sub.run(usercat_command)

            elif choice == "4":
                break
            else:
                print("Введите число от 1 до 4.")

    print("Выберите параметр, который хотите выполнить:\n1) Добавление пользователя\n2) Модификация пользователя\n3) Мандатное управление\n4) Выход")
    while True:
        try:
            x = int(input("Ввод: "))
            if x == 1:
                create_user()
            elif x == 2:
                user_modify()
            elif x == 3:
                mandatory_manage()
            elif x == 4:
                return
            else:
                print("Введите число от 1 до 4.")
        except ValueError:
            print("Введите корректное число.")

main()