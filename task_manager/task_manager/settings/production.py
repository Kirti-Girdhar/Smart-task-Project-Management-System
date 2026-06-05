from .base import *

DEBUG= False

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS','127.0.0.1,localhost').split(',')