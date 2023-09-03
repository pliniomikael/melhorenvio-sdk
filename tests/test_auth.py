"""
    Module: test_auth
"""
import unittest

import melhorenvio


class TestAuth(unittest.TestCase):
    sdk = melhorenvio.SDK(is_production=False, token="token")

    def test_refresh_token(self):
        self.assertEqual(self.sdk.auth().refresh_token()["status"], 200)


if __name__ == "__main__":
    unittest.main()
