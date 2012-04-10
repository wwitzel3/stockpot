import os
import sys
import transaction

from pyramid.security import ALL_PERMISSIONS
from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from stockpot.models import (
    DBSession,
    Base,
    Group,
    User,
    )

SITE_ACL = [
    ['Allow', 'system.Everyone', ['view']],
    ['Allow', 'role:viewer', ['view']],
    ['Allow', 'role:editor', ['view', 'add', 'edit']],
    ['Allow', 'role:owner', ['view', 'add', 'edit', 'manage']],
    ['Allow', 'role:admin', ALL_PERMISSIONS],
]

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd)) 
    sys.exit(1)

def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        user = User(email='nobody@example.com', password='password', username='admin')
        for ace in SITE_ACL:
            DBSession.add(Group(ace[1]))
        DBSession.flush()
        group = DBSession.query(Group).filter_by(name='role:admin').one()
        user.groups.add(group)
        DBSession.add(user)

