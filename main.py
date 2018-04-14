import requests

resp = requests.get("https://www.tinkoff.ru/api/v1/currency_rates/")
birg = resp.json()['payload']['rates'][0]['buy']
birg2 = resp.json()['payload']['rates'][1]['buy']
print(birg, birg2)

token = '08e35f615f6579bda204ef012617ea8703349210c983a34068f0e87af95a371be9559cbe0ef0ad969358d'


requests.get('https://api.vk.com/method/notifications.markAsViewed',
                    params={'v': 5.74, 'access_token': token}).json()['response']
data = requests.get('https://api.vk.com/method/messages.getLongPollServer',
                    params={'v': 5.74, 'access_token': token}).json()['response']  # получение ответа от сервера
data2 = requests.get('https://api.vk.com/method/messages.getDialogs',
                    params={'v': 5.74, 'access_token': token}).json()['response']  # получение ответа от сервера
data3 = requests.get('https://api.vk.com/method/friends.getRequests',
                    params={'v': 5.74, 'access_token': token}).json()['response']  # получение ответа от сервера
data4 = requests.get('https://api.vk.com/method/notifications.get',
                    params={'v': 5.74, 'access_token': token}).json()['response']  # получение ответа от сервера
count_unread = 0
for i in data2['items']:
    if 'unread' in i:
        count_unread = count_unread + 1
print(count_unread)
print(data4['count'])
print("data " + str(data3['count']))
while True:
    response = requests.get('https://{server}?act=a_check&key={key}&ts={ts}&wait=60&mode=2&version=2'.format(server=data['server'], key=data['key'], ts=data['ts'])).json()  # отправление запроса на Long Poll сервер со временем ожидания 20 и опциями ответа 2
    updates = response['updates']
    if updates:  # проверка, были ли обновления
        for element in updates:  # проход по всем обновлениям в ответе
            if element[0] == 80:
                print(element[1])
    data['ts'] = response['ts']  # обновление номера последнего обновления
    data5 = requests.get('https://api.vk.com/method/notifications.get',
                         params={'v': 5.74, 'access_token': token}).json()['response']  # получение ответа от сервера
    print(int(data5['count'])-int(data4['count']))
