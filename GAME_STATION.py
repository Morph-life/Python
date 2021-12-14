#Для просмотра подробных сведений  о программе, создателе и т.д. в начале программы после ее запуска напишите "да".
import time
import random

def title():
    print("Привет!")
    print("Информация о программе далее:")
    print("Дата время и т.д.: Эта программа называется GAME_STATION, в ней присутствуют 3 игры (подробнее после старта). Эта программа была создана 5.12.2021 в 20:05. (последнее редактирование было 11.12.2021 в 16:16)")
    print("Создатель: Дмитрий Федоренко, 11 лет")
    print("Для остальной информации обращайтесь по номеру +7(921)999-27-05 или e-mail: mitya.fedorenko10@outlook.com")
    print("...")
    print("...")
    print("...")
    print("DEVELOPER INFORMATION!")
    print("ВНИМАНИЕ!")
    print("Текущая версия:")
    print("...")
    print("RELEASE-46GOO09 | 1.0")
    print("...")
    print("Статус игры: АКТИВНО - РЕЛИЗ 1 ЗАГРУЖЕН В ПОСЛЕДНИЕ 7 ДНЕЙ - ОБНОВЛЕНИЙ НЕТ - ОБСЛУЖИВАНИЕ ЗАВЕРШЕНО В ПОСЛЕДНИЕ 24 ЧАСА.")
    print("...")
    print("...")
    print("...")

def game_number_1():
    print("Правила игры: вы загадываете число, если оно совпадает = вы победили, иначе = вы проиграли.")
    print("...")
    game_1__computer = input("Ведущий, введите число.")
    print("...")
    game_1__player = input("Введите число, которое хотите загадать.")
    print("...")
    if game_1__computer == game_1__player:
        print("Вы победили")
        print("...")
    else:
        print("Вы проиграли")
        print("...")

def game_word_2():
    print("Правила: Ведущий вводит слово и вы вводите слово, если кол-во букв совпадает = вы победили, иначе = вы проиграли.")
    print("...")
    game_2__computer = len(input("Ведущий, введите слово."))
    print("...")
    game_2__player = len(input("Введите ваше слово"))
    print("...")
    if game_2__player == game_2__computer:
        print(f'Ты выиграл, букв было {game_2__computer}')
        print("...")
    else:
        print(f'Ты проиграл, букв было {game_2__computer}')
        print("...")

def game_2player_3():
    print("Правила: сначала один игрок загадывает число и слово, потом другой делает тоже самое. Если числа совпадают, а букв в словах одинаковое количество = вы победили. Если что-то совпадает, что-то нет = 50/50, иначе = вы проиграли.")
    print("...")
    game_3__1_num = input("Игрок 1, введите ваше число от 1 до 10")
    print("...")
    game_3__1_word = len(input("Игрок 1, введите ваше слово"))
    print("...")
    game_3__2_num = input("Игрок 2, угадайте число!")
    print("...")
    game_3__2_word = len(input("Игрок 2, угадайте слово."))
    print("...")
    if game_3__1_num == game_3__2_num and game_3__1_word == game_3__2_word:
        print("Вы выиграли!")
        print("...")
    elif game_3__1_num == game_3__2_num and game_3__1_word != game_3__2_word or game_3__1_num != game_3__2_num and game_3__1_word == game_3__2_word:
        print("50/50")
        print("...")
    elif game_3__1_num != game_3__2_num and game_3__1_word != game_3__2_word:
        print("ВЫ ПРОИГРАЛИ!!!")
        print("...")


def game_BIG_3():
    print("In progress...")
    import os
    os.system('python C:.py')



name = input("Привет друг! Напиши свое имя, чтобы я знал как к тебе обращатся.")
print("...")

tittle = input(f'Привет {name}, далее напишите "да", чтобы посмотреть информацию.')
print("...")

if tittle == 'да':
    title()
    time.sleep(1.5)


else:
    print("Хорошо, мы начинаем игру")
    print("...")
    time.sleep(1.5)

while True:
    print("Погнали!")
    print("...")
    select_game = input("Выберите игру в которую хотите сыграть. (Позже вы сможете изменить это) Варианты: -угадай число- ; -угадай слово- ; -число и слово- (для двоих)")
    if select_game == 'угадай число':
        game_number_1()
    elif select_game == 'угадай слово':
        game_word_2()
    elif select_game == 'число и слово':
        game_2player_3()
    else:
        print("НЕВЕРНЫЙ ФОРМАТ!!! Попробуйте без знаков - или перепроверьте введенный текст. Если ошибка повторяется попробуйте перезагрузить игру. ERROR CODE: Release-66/current_data456|file-ex57/error990.87ui,UI_FIX")
        print("...")
        print("...")
        print("...")
        break
    new_game = input("Игра завершена, понравилось? Думаю да! Ладно, давай ещё раз. Если не хочешь играть, напиши -нет- (без знака -). А если хочешь, напиши какую-нибудь белеберду.")
    print("...")
    if new_game == 'нет':
        print("Хорошо, пока.")
        print()
        break
    else:
        print("Круто! Ещё раз!")
        print("...")



