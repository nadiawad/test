from unittest import TestCase
import alex


class Test(TestCase):
    def test_group_by_account_empty(self):
        return self.assertEqual(alex.group_by_account([]), {})

    def test_group_by_account_number_of_elements(self):
        response1 = alex.Response('123', 'Amazon', True)
        response2 = alex.Response('456', 'Google', True)
        response3 = alex.Response('789', 'Tesla', False)
        response4 = alex.Response('123', 'Amazon', True)
        response5 = alex.Response('123', 'Amazon', False)

        responses = [response1, response2, response3, response4, response5]

        actual_len = len(alex.group_by_account(responses))
        expected_len = 3
        return self.assertEqual(actual_len, expected_len)