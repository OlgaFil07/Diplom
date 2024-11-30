import configuration
import requests

def create_order(order_body):
    response = requests.post(configuration.URL + configuration.CREATE_ORDER_PATH, json=order_body)
    response.raise_for_status()
    return response

def get_order_by_track(order_track_number):
    response = requests.get(configuration.URL + configuration.GET_ORDER_BY_TRACK_PATH + str(order_track_number))
    response.raise_for_status()
    return response