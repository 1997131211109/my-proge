from django.test import TestCase
from user_accounts.apps import UserAccountsConfig


class UserAccountsConfigTest(TestCase):
    def test_app_name(self):
        app_config = UserAccountsConfig()
        self.assertEqual(app_config.name, 'user_accounts')

    def test_auto_field(self):
        app_config = UserAccountsConfig()
        self.assertEqual(app_config.default_auto_field, 'django.db.models.BigAutoField')
