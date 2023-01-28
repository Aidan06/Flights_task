# Программа авиарейсов

# 1.Отобразить список перелетов 
#a) номер рейса
# б)название: от куда куда, 
# в)время вылета
# г)цена за перелет
# 2.Пользователю требуется выбрать по номеру перелет и свое ФИО
# 3.Заплатить сколько требуется
# если введеные денежные средства совпадает с ценой то успешно
# если больше отдать сдачу
# если меньше то отказать и отобразить сообщение
# 4.После успешного прохождения, вывести сообщение
# номер рейса
# ФИО
# название от куда куда
# время вылета
# 5. Обязательно обработать ошибки с применением try, except


Amsterdam = [
    {
   'id': 'Bishkek - Amsterdam',
    'flight_number' : 'AC300', 
    'time': '9:00AM', 
    'price': 1200,
    'transit': 'Turkey'
    }
]
Bali = [
    {
    'id' : 'Almaty - Bali',
    'flight_number':'VD123', 
    'time': '11:00PM', 
    'price': 1950, 
    'transit': 'Malaysia'
   }
]
NY = [
   {
   'id' :'Bishkek - New York',
   'flight_number':'EO5623', 
   'time': '04:00PM',
   'price': 2035, 
   'transit': 'Germany'
    }
]

flights_list = (Amsterdam, Bali, NY)


for flights in flights_list: 
    print('-------------------------------')
    print(f'Табло рейсов на 10 апреля: {flights ["id"]}')
    print(f'Цена: {flights ["price"]}')
    print(f'Время рейса: {flights ["time"]}')
    print(f'Номер рейса: {flights ["flight_number"]}')
    print(f'Транзит: {flights ["transit"]}')
    print('-------------------------------')

while True:
    number = int(input('Введите название нужного города: '))
    your_name = str(input('Введите свое ФИО:'))
    cash = int(input('Оплатите: '))

    flight_price = 0
    flight_id = ''

for flights in flights_list: 
    if number == flights["id"]:
             flight_price = flights["price"]
             flight_id = flights ["id"]
             flight_time = flights ["time"]
             flight_transit = flights ["transit"]


    if cash < flight_price:
        print('У вас недостаточно средств! Повторите попытку снова!')
        break

    change = cash - flight_price

    if cash == flights['price']:
        print(f'Уважаемый_ая {your_name} , вы купили билет на {flight_id}. Время вылета {flight_time} , а транзит через {flight_transit}')






