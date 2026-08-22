import unittest
from app.analysis.mention_detector import detect_mentions
from app.analysis.sentiment import analyze_brand_response

class TestAgenticSOV(unittest.TestCase):

    def test_1_brand_detection(self):
        text = "HubSpot is a popular CRM."
        result = detect_mentions(text, ["HubSpot"])
        self.assertEqual(result.get("HubSpot"), 1, "HubSpot should be detected as mentioned.")

    def test_2_brand_omission(self):
        text = "Salesforce and Zoho are popular CRM platforms."
        result = detect_mentions(text, ["HubSpot"])
        self.assertEqual(result.get("HubSpot"), 0, "HubSpot should be detected as omitted.")

    def test_3_positive_sentiment(self):
        text = "HubSpot is an excellent choice for growing SaaS companies."
        result = analyze_brand_response("HubSpot", text)
        self.assertEqual(result.get("sentiment"), "positive")

    def test_4_negative_sentiment(self):
        text = "HubSpot may become expensive as the organization scales."
        result = analyze_brand_response("HubSpot", text)
        self.assertEqual(result.get("sentiment"), "negative")

    def test_5_neutral_sentiment(self):
        text = "HubSpot was founded in 2006."
        result = analyze_brand_response("HubSpot", text)
        self.assertEqual(result.get("sentiment"), "neutral")

if __name__ == "__main__":
    unittest.main()