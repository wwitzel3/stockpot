import unittest

from pyramid import testing

def _initTestingDB():
    from sqlalchemy import create_engine
    from stockpot.models import initialize_sql
    session = initialize_sql(create_engine('sqlite://'))
    return session

class TestMyRoot(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.session = _initTestingDB()

    def tearDown(self):
        testing.tearDown()
        self.session.remove()
        
    def _makeOne(self):
        from stockpot.models import MyRoot
        return MyRoot()

    def test___getitem__hit(self):
        from stockpot.models import MyModel
        root = self._makeOne()
        first = root['1']
        self.assertEqual(first.__class__, MyModel)
        self.assertEqual(first.__parent__, root)
        self.assertEqual(first.__name__, '1')

    def test___getitem__miss(self):
        root = self._makeOne()
        self.assertRaises(KeyError, root.__getitem__, '100')

    def test___getitem__notint(self):
        root = self._makeOne()
        self.assertRaises(KeyError, root.__getitem__, 'notint')

    def test_get_hit(self):
        from stockpot.models import MyModel
        root = self._makeOne()
        first = root.get('1')
        self.assertEqual(first.__class__, MyModel)
        self.assertEqual(first.__parent__, root)
        self.assertEqual(first.__name__, '1')

    def test_get_miss(self):
        root = self._makeOne()
        self.assertEqual(root.get('100', 'default'), 'default')
        self.assertEqual(root.get('100'), None)

    def test___iter__(self):
        root = self._makeOne()
        iterable = iter(root)
        result = list(iterable)
        self.assertEqual(len(result), 1)
        model = result[0]
        self.assertEqual(model.id, 1)
        
