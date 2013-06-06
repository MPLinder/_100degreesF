import os
import sys

PROJECT_ROOT = os.path.join(os.path.join(os.path.join(os.path.abspath(__file__), '..'), '..'), '..')
sys.path.insert(0, os.path.abspath(PROJECT_ROOT))

from django.core.management import setup_environ
# TODO this couples the app to the project. Can that be avoided?
from _100degreesF import settings

setup_environ(settings)