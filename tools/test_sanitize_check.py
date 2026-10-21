"""Unit tests for sanitize_check.scan_line."""
import unittest
from sanitize_check import scan_line


def labels(line, deny=()):
    return [label for label, _ in scan_line(line, list(deny))]


class TestScanLine(unittest.TestCase):
    def test_flags_private_ip_allows_documentation_range(self):
        self.assertIn("IP address", labels("host 10.20.30.40"))
        self.assertEqual(labels("host 192.0.2.10 and 203.0.113.0/24"), [])

    def test_flags_real_email_allows_example_domains(self):
        self.assertIn("Email", labels("contact jane@acmecorp.com"))
        self.assertEqual(labels("contact user@example.com"), [])

    def test_flags_secrets(self):
        self.assertIn("GitHub token", labels("ghp_" + "a" * 36))
        self.assertIn("Generic secret assignment", labels("password = Hunter2Secret!"))
        self.assertEqual(labels("password = <REDACTED>"), [])

    def test_mac_address(self):
        self.assertIn("MAC address", labels("aa:bb:cc:dd:ee:ff"))
        self.assertEqual(labels("00:00:5E:00:53:01"), [])

    def test_denylist_is_whole_word_and_case_insensitive(self):
        self.assertIn("Denylist term", labels("Acme onboarding", ["acme"]))
        self.assertEqual(labels("user token expired", ["tok"]), [])

    def test_version_strings_are_not_ips(self):
        self.assertEqual(labels("upgraded to 1.2.3"), [])


if __name__ == "__main__":
    unittest.main()
