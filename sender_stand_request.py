import configuration
import requests
import data

# Создание заказа

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE+configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)

# Получение заказа по треку заказа

def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE+configuration.GET_ORDER_PATH+str(track))


