# Edit this file to override the default graphite settings, do not edit settings.py
from os import environ

# Set SECRET_KEY if passed in via environment variable
try:
    if environ['SECRET_KEY']:
        SECRET_KEY = environ['SECRET_KEY']
except KeyError:
    pass

# Turn on debugging and restart apache if you ever see an "Internal Server Error" page
#DEBUG = True

# Set your local timezone (django will try to figure this out automatically)
TIME_ZONE = 'UTC'

STORAGE_DIR = '/data/graphite'

# Setting MEMCACHE_HOSTS to be empty will turn off use of memcached entirely
#MEMCACHE_HOSTS = ['127.0.0.1:11211']

# Sometimes you need to do a lot of rendering work but cannot share your storage mount
#REMOTE_RENDERING = True
#RENDERING_HOSTS = ['fastserver01','fastserver02']
#LOG_RENDERING_PERFORMANCE = True
#LOG_CACHE_PERFORMANCE = True

# If you've got more than one backend server they should all be listed here
#CLUSTER_SERVERS = []

# Override this if you need to provide documentation specific to your graphite deployment
#DOCUMENTATION_URL = "http://wiki.mycompany.com/graphite"

# Enable email-related features
#SMTP_SERVER = "mail.mycompany.com"

# LDAP / ActiveDirectory authentication setup
#USE_LDAP_AUTH = True
#LDAP_SERVER = "ldap.mycompany.com"
#LDAP_PORT = 389
#LDAP_SEARCH_BASE = "OU=users,DC=mycompany,DC=com"
#LDAP_BASE_USER = "CN=some_readonly_account,DC=mycompany,DC=com"
#LDAP_BASE_PASS = "readonly_account_password"
#LDAP_USER_QUERY = "(username=%s)"  #For Active Directory use "(sAMAccountName=%s)"

# If sqlite won't cut it, configure your real database here (don't forget to run manage.py syncdb!)
DATABASE_ENGINE = 'postgres' # or 'postgres'
DATABASE_NAME = 'graphite_grafana'
DATABASE_USER = 'nanoleaf'
DATABASE_PASSWORD = '5vbV2AVpFpkg4356'
DATABASE_HOST = 'nanoleaf-graphite-grafana.cdwnqaxfvpzf.us-east-1.rds.amazonaws.com'
DATABASE_PORT = '5432'
