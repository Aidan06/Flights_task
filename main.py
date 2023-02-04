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

flights_list = {
1: {
    'id': 'Bishkek - Amsterdam',
    'flight_number' : 'AC300', 
    'time': '9:00AM', 
    'price': 1200},

2: {
    'id': 'Almaty - Bali',
    'flight_number':'VD123', 
    'time': '11:00PM', 
    'price': 1950},

3: {
    'id' :'Bishkek - New York',
    'flight_number':'EO5623', 
    'time': '04:00PM',
    'price': 2035}
}



for flights in flights_list: 
    print('-------------------------------')
    print(f'Табло рейсов на 10 апреля: {flights ["id"]}')
    print(f'Цена: {flights ["price"]}')
    print(f'Время рейса: {flights ["time"]}')
    print(f'Номер рейса: {flights ["flight_number"]}')
    print('-------------------------------')

while True:
    number = int(input('Введите номер нужного рейса: '))
    your_name = str(input('Введите свое ФИО:'))
    check_question = input('Вы правильно ввели информацию?\nYes(y)/No(n)')
    no = ['N', 'No']
    yes =['Y', 'Yes']
    if check_question is no:
        print('Введите правильно')
        continue
    if check_question is yes:
        print('Продолжите операцию')
        break

while True:
    flights_list_id = (1, 2, 3)

    try: 
        info = int(input('Введите номер нужного рейса:'))
    except:

        print('Введите номер из списка!')
        continue

    if info in flights_list_id:
        right_flight = flights_list.get(info)

        print(right_flight)
        print(f"Оплатите {right_flight.get('price')}$")
        break

    if not info in flights_list_id :
        print('Вам нужно выбрать рейс из списка : 1, 2, 3!')
        continue 


while True: 
    cash = right_flight.get('price')

    try:
        pay = int(input('Пожалуйста, внесите деньги:'))

    except:
        print('Введите нужные банкноты')
        continue

    if pay > cash: 
        print(f"Спасибо, ваша сдача {pay-cash} $.
        Ваш рейс {info}.
        Название рейса {right_flight.get('id')}.
        Ваша информация: {your_name.title()}.
        Номер рейса:{right_flight.get('flight_number')}.
        Время вылета: {right_flight.get('time')}")
        break

    if pay <cash:
        print(f'Вы недоплатили {cash-pay}$')
        continue

    if pay == cash: 
        print(f'Операция завершена успешно!
        Ваш рейс {info}.
        Название рейса {right_flight.get('id')}.
        Ваша информация: {your_name.title()}.
        Номер рейса: {right_flight.get('flight_number')}.
        Время вылета: {right_flight.get('time')}')
        break


#     cash = int(input('Оплатите: '))

#     flight_price = 0
#     flight_id = ''

# for flights in flights_list: 
#     if number == flights["id"]:
#              flight_price = flights["price"]
#              flight_id = flights ["id"]
#              flight_time = flights ["time"]
#              flight_transit = flights ["transit"]


#     if cash < flight_price:
#         print('У вас недостаточно средств! Повторите попытку снова!')
#         break

#     change = cash - flight_price

#     if cash == flights['price']:
#         print(f'Уважаемый_ая {your_name} , вы купили билет на {flight_id}. Время вылета {flight_time} , а транзит через {flight_transit}')






