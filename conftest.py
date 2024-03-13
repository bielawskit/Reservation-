import pytest
from django.contrib.auth.models import Permission

from club.models import Club, Coach


@pytest.fixture()
def user(db, django_user_model):

    user = django_user_model.objects.create_user(
        name="Test", surname="123", email="test@test.pl", password="Testpass123"
    )
    permission_add_club = Permission.objects.get(name="Can add club")
    permission_add_court = Permission.objects.get(name="Can add court")
    permission_add_couch = Permission.objects.get(name="Can add coach")
    permission_edit_club = Permission.objects.get(name="Can change club")
    permission_edit_coach = Permission.objects.get(name="Can change coach")
    permission_delete_club = Permission.objects.get(name="Can delete club")
    permission_delete_coach = Permission.objects.get(name="Can delete coach")
    permission_view_coach = Permission.objects.get(name="Can view coach")

    user.user_permissions.add(
        permission_add_club,
        permission_add_court,
        permission_add_couch,
        permission_edit_club,
        permission_edit_coach,
        permission_delete_club,
        permission_delete_coach,
        permission_view_coach,
    )
    return user


@pytest.fixture
def user_no_perm(db, django_user_model):
    user = django_user_model.objects.create_user(
        email="test1@admin.com",
        name="Test1 User",
        surname="Test2",
        password="TestPass321",
    )
    return user


@pytest.fixture()
def create_club(user):
    yield Club.objects.create(
        name="Test", location="Test1", quantity=1, multisport=1, user=user
    )


@pytest.fixture()
def club_id(create_club):
    yield create_club.id


@pytest.fixture()
def create_coach(user, create_club):
    yield Coach.objects.create(
        name="Test2", surname="Test1", price=50, club_id=create_club.id
    )


@pytest.fixture()
def create_court(user, create_club):
    yield Club.objects.create(
        name="Test3", type=1, preference=1, club_id=create_club.id
    )


@pytest.fixture()
def court_id(user, create_club):
    yield create_court.id


@pytest.fixture()
def coach_id(create_coach):
    yield create_coach.id


# @pytest.fixture()
# def user_with_permission_edit(user):
#     permission = Permission.objects.get(name='Can change club')
#     yield user.user_permissions.add(permission)


# @pytest.fixture()
# def user_login(user):

#     user_login.force_login(user)
#     return user_login
