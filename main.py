import json
from pydantic import BaseModel, Field


class Guide(BaseModel):
    FIO: str = None
    name_organization: str = None
    phone: int = None
    phone_mob: int = None
    organization: str= None
    name: str= None


    @classmethod
    def start(cls):
        first_request = str(input('Добавить/Редактировать/Поиск/Записи?\n')).lower()
        if first_request == 'добавить':
            cls.add()
        if first_request == 'редактировать':
            cls.edit()
        if first_request == 'поиск':
            cls.search()
        if first_request == 'записи':
            cls.records()

    @staticmethod
    def add():
        add_data = Guide(
            # Запрашиваем данные для записи в json
            FIO=input('Введите ФИО:\n'),
            name_organization=str(input('Введите название организации:\n')),
            phone=input('Введите рабочий телефон:\n'),
            phone_mob=input('Введите личный номер телефона:\n'))

        # Открываем json для записи
        with open('data.json') as f:
            data = json.load(f)
            data['personal'].append({
                'ФИО': add_data.FIO,
                'Название ораганизации': add_data.name_organization,
                'Рабочий телефон': add_data.phone,
                'Личный номер телефона': add_data.phone_mob
            }
            )
            # Записываем данные в файл
            with open('data.json', 'w') as outfile:
                json.dump(data, outfile, ensure_ascii=False, indent=4)
            print("Вы добавили новую запись в справочник!")

    @staticmethod
    def edit():
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)
            # запрашивем фамилию по которой будем искать
            a = str(input('Введите фамилию человека:\n'))
            # Получаем список всех записей
            for f in data['personal']:
                if a in f['ФИО']:  # ищем нужную карточку
                    b = str(input(
                        'Что вы хотите поменять?(ФИО,Название ораганизации,Рабочий телефон,Личный номер телефона):\n'))
                    r = str(input('На какое значение меняем?'))
                    # Заменяем данные в карточке на новые
                    f[b] = r
                    print('Новое значение', f)
                    # Сохраняем файл с новыми данными
                    with open('data.json', 'w') as file:
                        json.dump(data, file, ensure_ascii=False, indent=4)

    @staticmethod
    def search():
        add_search = Guide(
            # Запрашиваем данные для записи в json
            name=input('Фамилия того кого ищем:\n'),
            organization=str(input('Введите название организации:\n')))

        with open('data.json', 'r') as json_file:
            data = json.load(json_file)
            for f in data['personal']:
                # Если Имя или Название оранизации подходит под поиск то выдает ответ
                if add_search.name in f['ФИО'] or add_search.organization in f['Название ораганизации']:
                    print('ФИО:', f['ФИО'])
                    print('Название ораганизации:', f['Название ораганизации'])
                    print('Рабочий телефон:', f['Рабочий телефон'])
                    print('Личный номер телефона:', f['Личный номер телефона'])

    @staticmethod
    def records():
        quantity = int(input('Сколько записей показать\n'))
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)
            for f in data['personal'][:quantity]:
                print(f)


if __name__ == '__main__':
    Guide.start()
