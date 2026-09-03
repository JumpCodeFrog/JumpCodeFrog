import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import generate_languages as metrics


class LanguageMetricsTests(unittest.TestCase):
    def test_collect_language_bytes_skips_non_public_sources(self):
        repositories = [
            {"name": "public", "private": False, "fork": False, "languages_url": "lang://public"},
            {"name": "dpowcoin", "private": False, "fork": False, "languages_url": "lang://dpowcoin"},
            {"name": "fork", "private": False, "fork": True, "languages_url": "lang://fork"},
            {"name": "private", "private": True, "fork": False, "languages_url": "lang://private"},
        ]
        responses = {"lang://public": {"Go": 70, "Python": 30}}

        totals, repository_count = metrics.collect_language_bytes(repositories, responses.__getitem__)

        self.assertEqual(totals, {"Go": 70, "Python": 30})
        self.assertEqual(repository_count, 1)

    def test_empty_language_data_fails_instead_of_publishing_zero_languages(self):
        with self.assertRaisesRegex(RuntimeError, "No public language data"):
            metrics.summarize_languages({})

    def test_summary_is_sorted_filtered_and_limited(self):
        summary = metrics.summarize_languages(
            {"Go": 600, "Python": 300, "Shell": 99, "Noise": 1},
            limit=2,
            minimum_percent=1.0,
        )
        self.assertEqual([item[0] for item in summary], ["Go", "Python"])

    def test_rendered_svg_is_valid_and_escapes_language_names(self):
        svg = metrics.render_svg([("A&B", 75, 75.0), ("Go", 25, 25.0)], 2, 3)

        ET.fromstring(svg)
        self.assertIn("A&amp;B", svg)
        self.assertIn("75.00%", svg)
        self.assertIn("3 PUBLIC NON-FORK REPOS", svg)

    def test_sparse_summary_uses_full_width_percentage_alignment(self):
        svg = metrics.render_svg([("Go", 80, 80.0), ("Python", 20, 20.0)], 2, 3)

        self.assertIn('x="390" y="95" text-anchor="end"', svg)

    def test_card_uses_native_readme_width_and_readable_primary_type(self):
        svg = metrics.render_svg([("Go", 100, 100.0)], 1, 1)

        self.assertIn('viewBox="0 0 410 196"', svg)
        self.assertIn('font-size="15" fill="#FFE2AE">Go</text>', svg)

    def test_checked_in_card_never_publishes_zero_languages(self):
        card = (Path(__file__).resolve().parents[1] / "metrics-languages.svg").read_text()

        self.assertNotIn("0 Languages", card)

if __name__ == "__main__":
    unittest.main()
