import requests
import time

# отправляем на сервис запросы
for i in range(40):
    params = {
        'x': str(i),
        'y': '-16',
    }
    response = requests.get('http://localhost:1702/predict', params=params)
    
    # на 30 запросе перерыв 30 секунд
    if i == 30:
        time.sleep(30)
    
    # после каждого запроса перерыв 2 секунды
    time.sleep(2)