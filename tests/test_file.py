from context import PolyglotPath

import unittest


class TestCases(unittest.TestCase):
    """Advanced test cases."""
    def test_application(self):
        d = PolyglotPath(".")
        print(d.stat.parent)
        self.assertIsNone(None)


if __name__ == '__main__':
    unittest.main()