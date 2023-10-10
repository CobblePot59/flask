from flask import Flask
from flask_ldap3_simple_auth import LDAPManager
from flask_toastr import Toastr

app = Flask(__name__)
app.config.from_pyfile('config.py')

ldap = LDAPManager(app)

toastr = Toastr(app)

from views import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
