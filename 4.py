while True:
    print("Введите 1 – рекомендация, 2 – розыгрыш, off – завершить")
    n1 = input()
    if n1 == "1":
        z = input("Введите предпочтение: ")
        if z == "спорт":
            print("Подкаст Убойный спорт")
        else:
            print("Новый альбом Канье Уэста")
    if n1 == "2":
        pop = 0
        while pop < 3:
            game = input('Введите название группы: ')
            pop += 1
            if game == 'Queen':
                print('Вы выиграли билет на концерт!')
                pop = 1488

    if n1 == "off":
        break