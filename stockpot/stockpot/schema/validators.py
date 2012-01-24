from formencode import Invalid
from formencode import validators as v

import stockpot.models as M

class ValidUser(v.FancyValidator):
    def validate_python(self, values, c):
        login, password = values['login'], values['password']
        user = M.User.authenticate(login, password)
        if not user:
            error = 'Invalid email and/or password.'
            raise Invalid(error, values, c, error_dict=dict(email=error))
        else:
            values['userid'] = user._id

class UniqueEmail(v.FancyValidator):
    def __init__(self, user=None):
        self.user = user
    def validate_python(self, values, c):
        user = M.DBSession.query(M.User).filter_by(email=values['email']).first()
        if not user or user.email == self.user.email:
            pass
        else:
            error = 'This email address is already in use.'
            raise Invalid(error, values, c, error_dict=dict(email=error))

class UniqueUsername(v.FancyValidator):
    def __init__(self, user=None):
        self.user = user
    def validate_python(self, values, c):
        user = M.DBSession.query(M.User).filter_by(username=values['username']).first()
        if not user or user.username == self.user.username:
            pass
        else:
            error = 'This username is already in use.'
            raise Invalid(error, values, c, error_dict=dict(username=error))

