#Этот файл только для хранения переменных!

#Игровые файлы
vers = '0.4.32'
name = 'Хлебушек'
about = 'Симулятор хлебушка'
coins = 5000
siggnal0 = 1

#Промежуточные переменные
wait1 = ''
loading = 1
wait2 = ''
wait3 = ''
wait4 = ''
lobbywait = ''
wait5 = ''
wait6 = ''
wait7 = ''

#Пользовательские
money = 1
name = ''

#save
filer1_money = 0
filer1_name = ''
filer2_money = 0
filer2_name = ''
filer3_money = 0
filer3_name = ''
filer4_money = 0
filer4_name = ''

def save():
    filer1 = False
    filer2 = False
    filer3 = False
    filer4 = False

    global filer1_money
    global filer1_name
    global filer2_money
    global filer2_name
    global filer3_money
    global filer3_name
    global filer4_money
    global filer4_name

    if filer4 == True:
        if filer3 == True:
            if filer2 == True:
                if filer1 == True:
                    print('На данный момент не свободных ячеек!')
                else:
                    filer1_money = money
                    filer1_name = name
                    filer1 = True
            else:
                filer2_money = money
                filer2_name = name
                filer2 = True
        else:
            filer3_money = money
            filer3_name = name
            filer3 = True
    else:
        filer4_money = money
        filer4_name = name
        filer4 = True

def impData(yacheyka):
    global money
    global name
    if yacheyka == '1':
        money = filer1_money
        name = filer1_name
    elif yacheyka == '2':
        money = filer2_money
        name = filer2_name
    elif yacheyka == '3':
        money = filer3_money
        name = filer3_name
    elif yacheyka == '4':
        money = filer4_money
        name = filer4_name
    else:
        print('Неверный код ячейки!')

#Этот файл необходим для хранения переменных и не подлежит редактированию!