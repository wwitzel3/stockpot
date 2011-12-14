Overview
--------
stockpot is the opensource code base for the website Community Cookbook (<http://communitycookbook.net>).
The site is built using Pyramid with MongoDB and Ming.

Installing
----------
You will need a functioning MongoDB installation for your platform. See <http://www.mongodb.org/display/DOCS/Quickstart>

Clone the stockpot code repository

    git clone git clone https://git.code.sf.net/p/stockpot/code stockpot-code

Now run the setup.py script. It is reccomend you do this inside a virtual environment. See <http://pypi.python.org/pypi/virtualenv>

    python setup.py develop

Once that is completed you will want to edit your development.ini file to reflect your local settings.

    mongo.url = mongodb://localhost:27017/
    mongo.database = stockpot

You will also need to open and edit the CONFIG.yaml.sample file. This file should be renamed to CONFIG.yaml so that Velruse
can properly pickup your OAuth provider credentials. See <http://packages.python.org/velruse/providers.html> for more information
on configuring providers.

    OpenID:
        Realm: http://example:6543
        Endpoint Regex: http://example.com

You will also need to make sure that your /etc/hosts file contains a mapping of your external domain to 127.0.0.1 if you plan to run
and test the application locally. If you do not setup this mapping, the velruse endpoints / callback URLs will not work when the OAuth
providers redirect you after logging in.

    # Using above settings, your etc hosts would look like this
    127.0.0.1 example.com

Make sure you have MongoDB running.

    # Here is how I start it on MacOS X
    mongod run --config /usr/local/Cellar/mongodb/2.0.0-x86_64/mongod.conf

Now you can start the application.

    pserve development.ini

Visti http://localhost:6543 in your browser.

Feedback
--------
You can send questions or comments to <wayne@pieceofpy.com> or use the [discussion forums](https://sourceforge.net/p/stockpot/discussion/general/)

