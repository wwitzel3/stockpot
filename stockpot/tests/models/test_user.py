import unittest
from pyramid import testing

import stockpot.models as M

class UserModelTest(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.kwargs = dict(username='test', password='password',
                email='test@example.com')

    def tearDown(self):
        testing.tearDown()

    def test_init(self):
        user = M.User(**self.kwargs)

        self.assertEquals(user.username, self.kwargs.get('username'))
        self.assertEquals(user.email, self.kwargs.get('email'))
        self.assertEquals(user.password,
                M.User.generate_password(self.kwargs.get('password'),
                    str(user.signup_date)))

    def test_update(self):
        user = M.User(**self.kwargs)
        kwargs = dict(username='test2', password='password1',
                email='demo@example.com')
        user.update(**kwargs)
        self.assertEquals(user.username, kwargs.get('username'))
        self.assertEquals(user.email, kwargs.get('email'))
        self.assertEquals(user.password,
                M.User.generate_password(kwargs.get('password'),
                    str(user.signup_date)))

    def test_social_twitter(self):
        pass

    def test_social_facebook(self):
        pass

    def test_random_username(self):
        username = M.User.random_username(prefix='demo')
        self.assertEquals(len(username), 9)

        username = M.User.random_username(prefix='demo', _range=3)
        self.assertEquals(len(username), 7)

