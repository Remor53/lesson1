dict = {'city': 'Москва', 'temperature': '20'}
print(dict['city'])
dict['temperature'] = int(dict['temperature'])
dict['temperature'] -= 5
print(dict['temperature'])
if dict.get('country') is True:
    print('Ключ \'country\' есть в словаре')
else:
    print('Ключа \'country\' нет в словаре')
print(dict.get('country', 'Россия'))
dict['date'] = '27.05.2017'
print(len(dict))