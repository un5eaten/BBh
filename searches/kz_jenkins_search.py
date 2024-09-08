import shodan

# Введите ваш API-ключ Shodan
SHODAN_API_KEY = '[YOUR_API_KEY_FROM_SHODAN]'

# Создание клиента Shodan
api = shodan.Shodan(SHODAN_API_KEY)

# Запрос для поиска Jenkins-серверов в Казахстане
query = 'Jenkins country:KZ'

try:
    # Выполнение поиска
    results = api.search(query)

    print(f'Найдено {results["total"]} результатов:')
    
    # Вывод информации о найденных хостах
    for result in results['matches']:
        ip = result['ip_str']
        port = result['port']
        print(f'IP: {ip}:{port}')
        if 'org' in result:
            print(f'Организация: {result["org"]}')
        if 'location' in result:
            print(f'Город: {result["location"].get("city", "Неизвестно")}')
        print('-----------------------------')

except shodan.APIError as e:
    print(f'Ошибка API Shodan: {e}')