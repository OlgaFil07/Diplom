# Ольга Фильнова, 24-я когорта - Финальный проект. Инженер по тестированию плюс.


from order_api import create_order, get_order_by_track
import data

def test_create_and_get_order_by_track():

    order_response = create_order(data.order_body)
    assert order_response.status_code == 201


    order_track_number = order_response.json().get("track")
    assert order_track_number is not None


    data_order = get_order_by_track(order_track_number)
    assert data_order.status_code == 200