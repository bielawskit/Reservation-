from django.urls import reverse

from reservation.models import Reservation


def test_reservation_show_all(db, client, club_id, user):
    endpoint = reverse('reservation:reservation_show_all')
    response = client.get(endpoint)
    assert response.status_code == 200
    assert 'Klub' in str(response.content)


def test_reservation_add_get(db, client, club_id, user, coach_id):
    client.force_login(user)
    endpoint = reverse('reservation:reservation_view')
    response = client.get(endpoint)
    assert response.status_code == 200
    assert 'Start' in str(response.content)


# def test_reservation_get_user_no_login(db, client, user_no_perm):
#     endpoint = reverse('reservation:reservation_view')
#     response = client.get(endpoint)
#     assert response.status_code == 403

# def test_reservation_add_post(db, client, club_id, user, coach_id):
#     client.force_login(user)
#     data = {'start': '08.12.1999 12:00', 'finish': '08.12.1999 13:00'}
#     endpoint = reverse('reservation:reservation_view')
#     response = client.post(endpoint, data)
#     reservation = Reservation.objects.all()
#     assert response.status_code == 302
#     assert response.url.startswith(reverse('reservation:reservation_view'))
#     assert len(reservation) == 2
