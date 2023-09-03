"""
    Module: test_auth
"""
import unittest

import melhorenvio


class TestAuth(unittest.TestCase):
    sdk = melhorenvio.SDK(
        is_production=False,
        user_config={
            "user_agent": "Aplicação (email para contato técnico)",
            "client_id": 1234,
            "client_secret": "senha",
            "redirect_uri": "https://localhost.com/approve/",
            "code": "dkjahsdqoiweuqw",
        },
    )

    def test_refresh_token(self):
        self.assertEqual(self.sdk.auth().refresh_token()["status"], 200)


if __name__ == "__main__":
    unittest.main()
