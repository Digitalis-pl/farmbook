from django.urls import reverse
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User

from materials.models import Course, Lessons

from payments.models import Subscription, Payments
from users.permissions import IsModer


# Create your tests here.


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@mail.ru")
        self.course = Course.objects.create(name="test", owner=self.user)
        self.client.force_authenticate(user=self.user)
        self.ct = ContentType.objects.get_for_model(Course)

    def test_course_retrieve(self):
        url = reverse('materials:course-detail', args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), self.course.name
        )

    def test_course_access_not_owner_retrieve_(self):
        self.course = Course.objects.create(name="test")
        self.user = User.objects.create(email="test2@mail.ru")
        url = reverse('materials:course-detail', args=(self.course.pk,))
        response = self.client.get(url)
        self.assertEqual(
            response.status_code, status.HTTP_403_FORBIDDEN
        )

    def test_course_access_for_moder_retrieve_(self):
        self.course = Course.objects.create(name="test")
        self.user = User.objects.create(email="test2@mail.ru")
        group = Group.objects.create(name='moders')
        group.permissions.add(Permission.objects.get(codename='view_course').id)
        group.user_set.add(self.user)
        self.client.force_authenticate(user=self.user)
        url = reverse('materials:course-detail', args=(self.course.pk,))
        response = self.client.get(url)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_course_create(self):
        url = reverse('materials:course-list')
        data = {
            "name": "test"
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Course.objects.all().count(), 2
        )

    def test_course_update(self):
        url = reverse('materials:course-detail', args=(self.course.pk,))
        data = {
            "name": "test2"
        }
        response = self.client.patch(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), "test2"
        )

    def test_course_delete(self):
        url = reverse('materials:course-detail', args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Course.objects.all().count(), 0
        )

    def test_course_list(self):
        url = reverse('materials:course-list')
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.course.pk,
                    "name": "test",
                    "preview": None,
                    "description": None,
                    "owner": self.user.pk
                }
            ]
        }
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@mail.ru")
        self.course = Course.objects.create(name="test")
        self.client.force_authenticate(user=self.user)

    def test_create_sub(self):
        url = reverse('payments:subscription_controller')
        data = {
            "course_id": self.course.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            Subscription.objects.all().count(), 1
        )


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@mail.ru")
        self.course = Course.objects.create(name="c_test", owner=self.user)
        self.lesson = Lessons.objects.create(name="l_test", owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse('materials:lesson_detail', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), self.lesson.name
        )

    def test_lesson_access_not_owner_retrieve_(self):
        self.lesson = Lessons.objects.create(name="test")
        self.user = User.objects.create(email="test2@mail.ru")
        url = reverse('materials:lesson_detail', args=(self.lesson.pk,))
        response = self.client.get(url)
        self.assertEqual(
            response.status_code, status.HTTP_403_FORBIDDEN
        )

    def test_lesson_access_for_moder_retrieve_(self):
        self.course = Lessons.objects.create(name="test")
        self.user = User.objects.create(email="test2@mail.ru")
        group = Group.objects.create(name='moders')
        group.permissions.add(Permission.objects.get(codename='view_lessons').id)
        group.user_set.add(self.user)
        self.client.force_authenticate(user=self.user)
        url = reverse('materials:lesson_detail', args=(self.course.pk,))
        response = self.client.get(url)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_lesson_create(self):
        url = reverse('materials:lesson_create')
        data = {
            "name": "test",
            "link": "https://www.youtube.com/"
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lessons.objects.all().count(), 2
        )

    def test_lesson_update(self):
        url = reverse('materials:lesson_update', args=(self.lesson.pk,))
        data = {
            "name": "test2"
        }
        response = self.client.patch(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), "test2"
        )

    def test_lesson_moder_update(self):
        self.course = Lessons.objects.create(name="test")
        self.user = User.objects.create(email="test2@mail.ru")
        group = Group.objects.create(name='moders')
        group.permissions.add(Permission.objects.get(codename='view_lessons').id)
        group.user_set.add(self.user)
        self.client.force_authenticate(user=self.user)
        url = reverse('materials:lesson_update', args=(self.lesson.pk,))
        data = {
            "name": "test2"
        }
        response = self.client.patch(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), "test2"
        )

    def test_lesson_simple_user_update(self):
        self.lesson = Lessons.objects.create(name="test")
        self.user = User.objects.create(email="test2@mail.ru")
        url = reverse('materials:lesson_update', args=(self.lesson.pk,))
        data = {
            "name": "test2"
        }
        response = self.client.patch(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_403_FORBIDDEN
        )

    def test_lesson_delete(self):
        url = reverse('materials:lesson_delete', args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lessons.objects.all().count(), 0
        )

    def test_lesson_moder_delete(self):
        self.course = Lessons.objects.create(name="test")
        self.user = User.objects.create(email="test2@mail.ru")
        group = Group.objects.create(name='moders')
        group.permissions.add(Permission.objects.get(codename='view_lessons').id)
        group.user_set.add(self.user)
        self.client.force_authenticate(user=self.user)
        url = reverse('materials:lesson_delete', args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_403_FORBIDDEN
        )

    def test_lesson_list(self):
        url = reverse('materials:lessons_List')
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "link": None,
                    "name": self.lesson.name,
                    "preview": None,
                    "description": None,
                    "course": None,
                    "owner": self.user.pk
                }
            ]
        }
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )


class UserTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@mail.ru")
        # self.course = Course.objects.create(name="c_test", owner=self.user)
        # self.lesson = Lessons.objects.create(name="l_test", owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_user_retrieve(self):
        url = reverse('users:user_detail', args=(self.user.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("email"), self.user.email
        )

    def test_user_create(self):
        url = reverse('users:user_create')
        data = {
            "email": "test1@mail.ru",
            "password": "test"
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            User.objects.all().count(), 2
        )

    def test_user_update(self):
        url = reverse('users:user_update', args=(self.user.pk,))
        data = {
            "name": "test2"
        }
        response = self.client.patch(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), "test2"
        )

    def test_user_delete(self):
        url = reverse('users:user_delete', args=(self.user.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            User.objects.all().count(), 0
        )

    def test_user_list(self):
        url = reverse('users:user_list')
        response = self.client.get(url)
        data = response.json()
        result = [
            {
                "first_name": "",
                "email": self.user.email,
                "city": None
            }
        ]
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )


class PaymentTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@mail.ru")
        self.course = Course.objects.create(name="test", owner=self.user)
        self.payment = Payments.objects.create(payments_summ=100, payment_method="card")
        self.client.force_authenticate(user=self.user)

    def test_payment_retrieve(self):
        url = reverse('payments:payments-detail', args=(self.payment.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("payments_summ"), 100
        )

    def test_payment_create(self):
        url = reverse('payments:payments-list')
        data = {
            "user": self.user.pk,
            "course": self.course.pk,
            "payments_summ": 100,
            "payment_method": "card"
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Payments.objects.all().count(), 2
        )

    def test_payment_update(self):
        url = reverse('payments:payments-detail', args=(self.payment.pk,))
        data = {
            "payments_summ": 3,
            "user": self.user.pk
        }
        response = self.client.patch(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("payments_summ"), 3
        )

    def test_payment_delete(self):
        url = reverse('payments:payments-detail', args=(self.payment.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Payments.objects.all().count(), 0
        )

    def test_payment_list(self):
        url = reverse('payments:payments-list')
        response = self.client.get(url)
        data = response.json()
        result = [
            {
                "id": self.payment.pk,
                "date": None,
                "payments_summ": 100,
                "payment_method": "card",
                "user": None,
                "course": [],
                "lesson": []
            }
        ]
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )
