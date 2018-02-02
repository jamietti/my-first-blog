from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="miettinj", password="secret",is_staff="True")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        mina = User.objects.get(username="miettinj")
        self.assertEqual(mina.is_staff, True)

    def test_login(self):
        #c = Client(enforce_csrf_checks=True)
        c = Client()
        print("l 17 ",c.session.__dict__)
        #response = c.post('/accounts/login/', {'username': 'miettinj', 'password': 'secret'})
        #print("l 19 ",c.session.__dict__)
        #response = c.post('/login/', {'username': 'john', 'password': 'smith'})
        #print("res1: ",response.status_code)
        objs=User.objects.all()
        for o in objs:
            if o.username=="miettinj":
                user = o

        print(c.force_login(user))
        response = c.get('/')
        print("res2: ",response.status_code)
        print(c.session.__dict__)
