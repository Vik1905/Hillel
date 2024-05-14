import unittest
from homework_10 import log_event

class TestLoginEventLogging(unittest.TestCase):

    def test_successful_login(self):
        log_event("test_user", "success")
        with open('login_system.log', 'r') as log_file:
            log_content = log_file.read()
            self.assertIn("Login event - Username: test_user, Status: success", log_content)

    def test_expired_password(self):
        log_event("test_user", "expired")
        with open('login_system.log', 'r') as log_file:
            log_content = log_file.read()
            self.assertIn("Login event - Username: test_user, Status: expired", log_content)

    def test_failed_login(self):
        log_event("test_user", "failed")
        with open('login_system.log', 'r') as log_file:
            log_content = log_file.read()
            self.assertIn("Login event - Username: test_user, Status: failed", log_content)

if __name__ == '__main__':
    unittest.main()