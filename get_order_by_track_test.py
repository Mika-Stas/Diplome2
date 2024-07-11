# Анастасия Михалева, 18-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request


def possitive_assert():
    current_body = data.order_body.copy()
    new_order = sender_stand_request.post_new_order(current_body)
    track = new_order.json()["track"]
    get_order = sender_stand_request.get_order_by_track(track)

    assert get_order.status_code == 200

def test_get_order_by_track():
    possitive_assert()