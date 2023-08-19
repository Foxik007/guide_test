import json


print('**Справочник**')
print(' ************\n')


def main():
    # Узнаем что хочет пользователь
    first_request = str(input('Добавить/Редактировать/Поиск/Записи?\n')).lower()

    if first_request == 'добавить':
        #Запрашиваем данные для записи в json
        FIO = str(input('Введите ФИО:\n'))
        name_organization = str(input('Введите название организации:\n'))
        phone = int(input('Введите рабочий телефон:\n'))
        phone_mob = int(input('Введите личный номер телефона:\n'))

        #Открываем json для записи
        with open('data.json') as f:
            data = json.load(f)
            data['personal'].append({
                'ФИО': FIO,
                'Название ораганизации': name_organization,
                'Рабочий телефон': phone,
                'Личный номер телефона': phone_mob
            }
            )
            #Записываем данные в файл
            with open('data.json','w') as outfile:
                json.dump(data,outfile,ensure_ascii=False,indent=4)
            print("Вы добавили новую запись в справочник!")


    if first_request == 'редактировать':
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)
            # запрашивем фамилию по которой будем искать
            a = str(input('Введите фамилию человека:\n'))
            # Получаем список всех записей
            for f in data['personal']:
                if a in f['ФИО']:      # ищем нужную карточку
                    b = str(input('Что вы хотите поменять?(ФИО,Название ораганизации,Рабочий телефон,Личный номер телефона):\n'))
                    r = str(input('На какое значение меняем?'))
                    #Заменяем данные в карточке на новые
                    f[b] = r
                    print('Новое значение',f )
                    #Сохраняем файл с новыми данными
                    with open('data.json', 'w') as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)

    if first_request == 'поиск':
        name = str(input('Фамилия того кого ищем?\n'))
        organization = str(input('Название ораганизации?\n'))

        with open('data.json', 'r') as json_file:
            data = json.load(json_file)

            for f in data['personal']:

    # Если Имя или Название оранизации подходит под поиск то выдает ответ
                if name in f['ФИО'] or organization in f['Название ораганизации']:
                    print('ФИО:',f['ФИО'])
                    print('Название ораганизации:',f['Название ораганизации'])
                    print('Рабочий телефон:',f['Рабочий телефон'])
                    print('Личный номер телефона:',f['Личный номер телефона'])


    # Выдает количество записей которые мы хотим получить
    if first_request == 'записи':
        quantity = int(input('Сколько записей показать\n'))

        with open('data.json', 'r') as json_file:
            data = json.load(json_file)

            for f in data['personal'][:quantity]:
                print(f)

if __name__ == '__main__':
    main()
