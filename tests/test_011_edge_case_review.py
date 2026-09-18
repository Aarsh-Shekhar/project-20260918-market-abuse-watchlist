import unittest

from market_abuse_watchlist.models import Record
from market_abuse_watchlist.scoring import score_record


class DepthCheck11(unittest.TestCase):
    def test_011_edge_case_review(self):
        record = Record(id="order-011", exposure=53361, signal=0.731, urgency=3)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
