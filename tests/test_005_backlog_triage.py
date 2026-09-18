import unittest

from market_abuse_watchlist.models import Record
from market_abuse_watchlist.scoring import score_record


class DepthCheck5(unittest.TestCase):
    def test_005_backlog_triage(self):
        record = Record(id="order-005", exposure=88721, signal=0.560, urgency=8)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
