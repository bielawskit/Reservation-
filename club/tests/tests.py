from random import randint

from django.urls import reverse

from club.models import Club, Court, Coach, PriceList


def test_club_add_get(db, client, user):
    client.force_login(user)
    endpoint = reverse('club:clubAdd')
    response = client.get(endpoint)
    assert response.status_code == 200
    assert 'Multisport' in str(response.content)


# def test_club_add_get_no_permission(db, client, user_no_perm):
#     client.force_login(user_no_perm)
#     endpoint = reverse('club:clubAdd')
#     response = client.get(endpoint)
#     assert response.status_code == 302


def test_club_add_post(db, client, club_id, user):
    client.force_login(user)
    data = {'name': 'TestAddedClub', 'location': 'Added Location Test', 'quantity': 2, 'multisport': 1}
    endpoint = reverse('club:clubAdd')
    response = client.post(endpoint, data)
    club = Club.objects.all()
    assert response.status_code == 302
    assert response.url.startswith(reverse('home:home'))
    assert len(club) == 2

    # czy w bazie znajduje sie juz 1 pozycja klubu ?


def test_club_show_all(db, client, club_id, user):
    endpoint = reverse('club:clubShowAll')
    response = client.get(endpoint)
    assert response.status_code == 200
    assert 'Lokalizacja' in str(response.content)


def test_club_edit_get(db, client, club_id, user):
    client.force_login(user)
    endpoint = reverse('club:clubEdit', kwargs={'pk': club_id})
    response = client.get(endpoint)
    assert response.status_code == 200
    assert 'Edytuj' in str(response.content)


def test_club_edit_post(db, client, club_id, user):
    client.force_login(user)
    endpoint = reverse('club:clubEdit', kwargs={'pk': club_id})
    data = {'name': 'TestEditedClub', 'location': 'Edited Location Test', 'quantity': 2, 'multisport': 1}
    response = client.post(endpoint, data)
    assert response.status_code == 302
    assert response.url.startswith(reverse('club:clubShowAll'))
    assert Club.objects.get(name='TestEditedClub')


def test_club_delete_get(db, client, club_id, user):
    client.force_login(user)
    endpoint = reverse('club:clubDelete', kwargs={'pk': club_id})
    response = client.get(endpoint)
    assert response.status_code == 200
    assert 'chcesz' in str(response.content)


def test_club_edit_get_no_permission(db, client, club_id, user_no_perm):
    client.force_login(user_no_perm)
    endpoint = reverse('club:clubDelete', kwargs={'pk': club_id})
    response = client.get(endpoint)
    assert response.status_code == 403


def test_club_delete_post(db, client, club_id, user):
    client.force_login(user)
    endpoint = reverse('club:clubDelete', kwargs={'pk': club_id})
    response = client.post(endpoint)
    club = Club.objects.all()
    assert response.status_code == 302
    assert response.url.startswith(reverse('club:clubShowAll'))
    assert len(club) == 0


def test_club_delete_get_no_permission(db, client, club_id, user_no_perm):
    client.force_login(user_no_perm)
    endpoint = reverse('club:clubDelete', kwargs={'pk': club_id})
    response = client.get(endpoint)
    assert response.status_code == 403


def test_club_details_get(db, client, club_id, user):
    endpoint = reverse('club:clubDetails', kwargs={'pk': club_id})
    response = client.get(endpoint)
    assert response.status_code == 200
    assert 'Typ' in str(response.content)


def test_court_add_get(db, client, user):
    client.force_login(user)
    endpoint = reverse('club:courtAdd')
    response = client.get(endpoint)
    assert response.status_code == 200
    assert 'Typ' in str(response.content)


def test_court_add_post(db, client, club_id, user):
    client.force_login(user)
    data = {'name': 'TestAddedCourt', 'type': randint(0, 2), 'preference': 1, 'club': club_id}
    endpoint = reverse('club:courtAdd')
    response = client.post(endpoint, data)
    court = Court.objects.all()
    assert response.status_code == 302
    assert response.url.startswith(reverse('home:home'))
    assert len(court) == 1

    # assert Court.objects.get(name='TestAddedCourt') - do wyjasnienia


def test_coach_add_get(db, client, user):
    client.force_login(user)
    endpoint = reverse('club:coachAdd')
    response = client.get(endpoint)
    assert response.status_code == 200
    assert 'Surname' in str(response.content)


def test_coach_add_post(db, client, club_id, user):
    client.force_login(user)
    data = {'name': 'TestCoach', 'surname': 'TestSurname', 'price': 50, 'club': club_id}
    endpoint = reverse('club:coachAdd')
    response = client.post(endpoint, data)
    coach = Coach.objects.all()
    assert response.status_code == 302
    assert response.url.startswith(reverse('home:home'))
    assert len(coach) == 1


def test_coach_show_all(db, client, club_id, user):
    endpoint = reverse('club:coachShowAll')
    response = client.get(endpoint)
    assert response.status_code == 200
    assert 'Cena' in str(response.content)


def test_coach_edit_get(db, client, club_id, user, coach_id):
    client.force_login(user)
    endpoint = reverse('club:coachEdit', kwargs={'pk': coach_id})
    response = client.get(endpoint)
    assert response.status_code == 200
    assert 'Edytuj' in str(response.content)


# def test_coach_edit_post(db, client, club_id, user, coach_id):
#     client.force_login(user)
#     endpoint = reverse('club:clubEdit', kwargs={'pk': coach_id})
#     data = {'name': 'TestEditedCoach', 'surname': 'TestEditedCoach', 'price': 50, 'club': club_id}
#     response = client.post(endpoint, data)
#     assert response.status_code == 302
#     assert response.url.startswith(reverse('club:coachShowAll'))
#     assert Coach.objects.get(name='TestEditedCoach')


def test_coach_delete_get(db, client, coach_id, user):
    client.force_login(user)
    endpoint = reverse('club:coachDelete', kwargs={'pk': coach_id})
    response = client.get(endpoint)
    assert response.status_code == 200
    assert 'chcesz' in str(response.content)


def test_coach_delete_get_no_permission(db, client, user_no_perm, coach_id):
    client.force_login(user_no_perm)
    endpoint = reverse('club:clubDelete', kwargs={'pk': coach_id})
    response = client.get(endpoint)
    assert response.status_code == 403


def test_coach_delete_post(db, client, club_id, user, coach_id):
    client.force_login(user)
    endpoint = reverse('club:coachDelete', kwargs={'pk': coach_id})
    response = client.post(endpoint)
    assert response.status_code == 302


def test_price_list_add_get(db, client, user):
    client.force_login(user)
    endpoint = reverse('club:courtPriceListAdd')
    response = client.get(endpoint)
    assert response.status_code == 200
    assert 'Cost' in str(response.content)


# def test_price_list_add_post(db, client, court_id, user, club_id):
#     client.force_login(user)
#     data = {'name': 'TestAddedCourt', 'type': 1, 'preference': 1, 'court': court_id}
#     endpoint = reverse('club:courtPriceListAdd')
#     response = client.post(endpoint, data)
#     pricelist = PriceList.objects.all()
#     assert response.status_code == 302
#     assert response.url.startswith(reverse('home:home'))
#     assert len(pricelist) == 1
