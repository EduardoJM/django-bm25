import unittest
from django.db import connection
from django.test import TestCase, modify_settings

@unittest.skipUnless(connection.vendor == "postgresql", "PostgreSQL specific tests")
@modify_settings(INSTALLED_APPS={"append": "django.contrib.postgres"})
class PostgreSQLTestCase(TestCase):
    pass
