import subprocess as sub
def user_add():
    def first():
        while input != "exit":
            print("имя пользователя - \nвведите exit чтобы вернуться назад")
            print("")
            def set_mandatory_level()
            
    def second():
        print('second')
    print("Выберите параметр который хотите выполнит \n1)Добавление пользователя \n2)Модификация пользователя \n3)Назад")
    while True:
        try:
            x = int(input("ввод: "))
            if x == 1:
                first()
            elif x == 2:
                second()
            else: user_add()
            break
        except ValueError:
            print("Введите цифру 1-2")

user_add()