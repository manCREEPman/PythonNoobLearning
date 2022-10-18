import random
from datetime import date, datetime
# import json

# p = {
#     'first_name': '',
#     'last_name': '',
#     'birth_date': '',
#     'sex': ''
# }

# with open('./new_json.json', 'w', encoding='utf-8') as f:
#     json.dump(p, f)
#     f.close()

# with open('./new_json.json', 'r', encoding='utf-8') as f:
#     p = json.load(f)
#     f.close()

CUR_DATE_FORMAT = '%d.%m.%Y'
CUR_DATE = date.today()
# print(CUR_DATE.strftime(CUR_DATE_FORMAT))

n = random.randint(3, 20)
print(f'Кол-во мигрантов {n}')


def errors(instring: str):
    k = 0
    
    for i in range(len(instring)):
        if k == len(instring) // 2:
            break
        if random.randrange(10) < 3:
            instring = instring[:i] + '?' + instring[i + 1:]
            k = k + 1
    return instring


def get_age(birth_date: date):
    cur_year = CUR_DATE.year
    cur_month = CUR_DATE.month
    cur_day = CUR_DATE.day
    
    age = cur_year - birth_date.year - ((cur_month, cur_day) < (birth_date.month, birth_date.day))
    return age


def names_has_errors(person: dict) -> bool:
    return person['first_name'].find('?') != -1 or person['last_name'].find('?') != -1


def input_from_file(n: int) -> list:
    m = []
    with open('./data.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        # если выносить словарь person сюда, то мы будем добавлять в список одну и ту же ссылку на этот словарь


        for i in range(n):
            try:
                person = {
                    'first_name': '',
                    'last_name': '',
                    'birth_date': '',
                    'sex': ''
                }
                line_data = lines[i].replace('\n', '').split('|')

                first_name = line_data[0]
                first_name = errors(first_name.capitalize())
                person['first_name'] = first_name

                last_name = line_data[1].capitalize()
                last_name = errors(last_name)
                person['last_name'] = last_name

                date_str = line_data[2]
                birth_date = datetime.strptime(date_str, CUR_DATE_FORMAT).date()
                person['birth_date'] = birth_date

                sex = line_data[3]
                person['sex'] = sex

                m.append(person)
            except IndexError:
                break
            finally:
                pass

        f.close()
        return m



def input_m(n: int) -> list:
    m = []
    for i in range(n):
        person = {
            'first_name': '',
            'last_name': '',
            'birth_date': '',
            'sex': ''
        }

        print('Введите имя', i + 1, 'мигранта')
        first_name = input()
        first_name = errors(first_name.capitalize())
        person['first_name'] = first_name

        print('Введите фамилию', i + 1, 'мигранта')
        last_name = input().capitalize()
        last_name = errors(last_name)
        person['last_name'] = last_name

        print('Введите дату рождения:')
        date_str = input()
        birth_date = datetime.strptime(date_str, CUR_DATE_FORMAT).date()
        person['birth_date'] = birth_date

        print('Выберете пол', i + 1, 'мигранта (м/ж)')
        sex = input()
        person['sex'] = sex

        m.append(person)
    return m


migrators = input_from_file(n)

print(migrators)

for migrator in migrators:
    if (18 <= get_age(migrator['birth_date']) <= 35 and
        names_has_errors(migrator) and 
        migrator['sex'] == 'м'):
        print(migrator)