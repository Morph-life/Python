from msilib.schema import File
import storage as file
import time

def play() -> None:
    print(f'Starting: {file.name}')
    print(f'Version: {file.vers}')
    file.wait1 = input('Press 1 for starting!')
    if file.wait1 == '1':
        print('Loading assets...')
        time.sleep(1)
        print('Waiting signal...')
        for i in range (100):
            print(f'Loading: {file.loading}%')
            time.sleep(0.5)
            file.loading += 1
        print('Loading servers...')
        print('Loading...')
        time.sleep(5)
        file.wait2 = input('Ready! Press 1 for play!')
        if file.wait2 == '1':
            game()
        else:
            print('Ok! Game stopped!')
            time.sleep(999999999999999999)
    else:
        print('Ok, game stopped!')
        time.sleep(999999999999999)

def game():
    print('Привет!')
    file.wait3 = input('Вы играете впервые? 1 - да, 2 - нет')
    if file.wait3 == '1':
        print('Добро пожаловать игру...')
    elif file.wait3 == '2':
        file.wait4 = input('Введите ваш номер ячейки!')
        file.impData(file.wait4)
    print('Данные успешно импортированы или созданы!')
    file.lobbywait = input('Вы в главном меню! p - пауза, f - фарм монет, q - выйти из игры, g - поддержка ссылки и помощь')
    if file.lobbywait == 'p':
        file.wait5 = input('Вы в меню паузы. s - сохранение, q - выход в главное меню')
        if file.wait5 == 's':
            file.save()
        elif file.wait5 == 'q':
            exit
        else:
            print('Неверный код!')
            exit
    elif file.lobbywait == 'f':
        while True:
            file.wait6 = input('Нажимайте любую кнопку! 1 кнопка = 1 монета. Выход = 1')
            if file.wait6 == '1':
                break
            else:
                file.wait6 = input('Нажимайте любую кнопку! 1 кнопка = 1 монета. Выход = 1')
    elif file.lobbywait == 'q':
        exit
    elif file.lobbywait == 'g':
        file.wait7 = input('Вы в меню ссылок. h - помощь, l - ссылки, i - исходный код проекта')
        if file.wait7 == 'h':
            print('Напишите: dimon0092@vk.com')
        elif file.wait7 == 'l':
            print('Ссылки: тг - t.me/ProgrammerDmitriy , GitHub - www.GitHub.com/Morph-life ')
        elif file.wait7 == 'i':
            print('Расположено на: www.GitHub.com/Python')
        else:
            print('неверный код')
    else: 
        print('неверный код')

play()

#Как использовать проект?
#Поместите этот файл и файл storage.py в одной папке с файлом игры
#В вашем файле напишите 'import game'
#Для запуска игры пропишите 'game.play()'
#Игра запустится и сама выберет и сделает операции с нужными файлами
#Наслаждайтесь игрой!