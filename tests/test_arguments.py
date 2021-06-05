from context import Arguments

import unittest


class TestCases(unittest.TestCase):
    """Advanced test cases."""

    def test_application(self):
        data = Arguments(
            arguments=[
                "--dir=.",
                "--o=dara.json",
                "--show=True",
                "--ignore=data.json,file.json,test.json",
            ]
        )

        print(data.parse())
        self.assertIsNone(None)


if __name__ == "__main__":
    unittest.main()
