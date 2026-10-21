"""Offline tests: parsing and classification of captured `dig +short` output."""
import unittest
from mail_provider_check import classify, parse_mx, parse_spf


class TestClassify(unittest.TestCase):
    def test_microsoft_365(self):
        mx = parse_mx(["0 example-com.mail.protection.outlook.com."])
        spf = parse_spf(['"v=spf1 include:spf.protection.outlook.com -all"'])
        r = classify(mx, spf)
        self.assertEqual(r["primary_inbound"], "Microsoft 365 (Exchange Online)")
        self.assertEqual(r["spf_senders"][0]["provider"], "Microsoft 365")

    def test_google_workspace_priority_order(self):
        mx = parse_mx(["10 alt3.aspmx.l.google.com.", "1 aspmx.l.google.com.", "5 alt1.aspmx.l.google.com."])
        r = classify(mx, parse_spf(['"v=spf1 include:_spf.google.com ~all"']))
        self.assertEqual(r["mx"][0]["host"], "aspmx.l.google.com")
        self.assertEqual(r["primary_inbound"], "Google Workspace")

    def test_gateway_in_front_of_m365(self):
        mx = parse_mx(["10 mxa-000.pphosted.com."])
        r = classify(mx, parse_spf(['"v=spf1 include:spf.protection.outlook.com include:pphosted.com -all"']))
        self.assertIn("Proofpoint", r["primary_inbound"])
        self.assertTrue(any("Microsoft 365" in n for n in r["notes"]))

    def test_split_txt_strings_and_unrelated_txt(self):
        lines = ['"google-site-verification=abc"', '"v=spf1 include:sendgrid.net " "include:_spf.google.com ~all"']
        spf = parse_spf(lines)
        self.assertTrue(spf.startswith("v=spf1"))
        self.assertEqual(len(classify([], spf)["spf_senders"]), 2)

    def test_risk_flags(self):
        self.assertTrue(any("No SPF" in n for n in classify([], None)["notes"]))
        self.assertTrue(any("+all" in n for n in classify([], "v=spf1 +all")["notes"]))
        self.assertIn("No MX", classify([], None)["primary_inbound"])


if __name__ == "__main__":
    unittest.main()
