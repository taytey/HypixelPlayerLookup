import unittest
import hypixel_util


class TestGetInfo(unittest.TestCase):

    def test_getJSON_badurl_should_return_empty(self):
        self.assertEqual(hypixel_util.get_json('https://jsonplaceholder.typicode.com/todos/1'), '')

    def test_getJSON_emptyurl_should_return_empty(self):
        self.assertEqual(hypixel_util.get_json('https://jsonplaceholder.typicode.com/todos/1'), '')

    def test_getJSON_validurl_should_return_data(self):
        self.assertIsNotNone(hypixel_util.get_json('https://jsonplaceholder.typicode.com/todos/1'))

    def test_getJSON_validurl_should_return_json(self):
        expected_return_value = {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": False
        }
        self.assertNotEqual(expected_return_value,
                            hypixel_util.get_json('https://jsonplaceholder.typicode.com/todos/1'))


if __name__ == '__main__':
    unittest.main()
