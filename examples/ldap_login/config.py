from datetime import timedelta

SECRET_KEY = 'fneurhfjpwejfnldusnfiwbsocjdpscouwehdnfbwnojno'
PERMANENT_SESSION_LIFETIME = timedelta(minutes=15)
SESSION_COOKIE_SAMESITE = "None"
SESSION_COOKIE_SECURE = True

LDAP_SCHEMA = 'ldaps'
LDAP_DOMAIN = 'cobblepot59.int'
LDAP_HOST = 'ldap.cobblepot59.int'
LDAP_PORT = 636
LDAP_USE_SSL = True
LDAP_BASE_DN = 'OU=Internal,OU=Domain Users,DC=cobblepot59,DC=int'
LDAP_BIND_DIRECT_CREDENTIALS = True
LDAP_USERNAME = ''
LDAP_PASSWORD = ''
