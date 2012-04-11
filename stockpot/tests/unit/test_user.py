from pyramid import testing

from stockpot.tests import UnitTestBase

class TestUserViews(UnitTestBase):
    def test_login_fails_empty(self):
        from stockpot.views.default import login_view
        request = testing.DummyRequest(post={
            'form.auth':True,
        })
        view = login_view(request)
        self.assertEquals(
            view.get('errors'),
            {'password': u'Required', 'email': u'Required'}
            )

    def test_login_success(self):
        from stockpot.views.default import login_view
        from stockpot.models import User

        user = User(email='nobody@example.com',
                    password='password',
                    username='username')
        self.session.add(user)
        self.session.flush()

        self.config.add_route('index','')

        request = testing.DummyRequest(post={
            'form.auth':True,
            'email':'nobody@example.com',
            'password':'password'
        })

        view = login_view(request)
        self.assertEquals(view.code, 302)
        self.assertEquals(view.location, 'http://example.com/')

