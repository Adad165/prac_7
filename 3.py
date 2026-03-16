pop = 0
while pop<3:
    game = input('Введите название игры: ')
    pop += 1
    if game == 'FIFA':
        print('Поздавляем! Вы угадали с попытки №', pop)
        break