from context import Arguments

import unittest


class TestCases(unittest.TestCase):
    """Advanced test cases."""

    def test_application(self):
        data = Arguments(arguments=["--dir=.", "--o=app.json"])
        self.assertIsNone(None)


if __name__ == '__main__':
    unittest.main()