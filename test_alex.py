from unittest import TestCase
import alex


class Test(TestCase):
    def test_group_by_account(self):
        return self.assertEqual(alex.group_by_account([]), {})
