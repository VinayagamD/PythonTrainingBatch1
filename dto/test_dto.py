import unittest
import json

from dto import BioData


class MyTestCase(unittest.TestCase):

    def test_create_bio_data(self):
        expected_name = "Test Name"
        expected_age = 25
        bio_data = BioData(name=expected_name, age=expected_age)
        self.assertNotEqual(bio_data, None)
        self.assertEqual(bio_data.name, expected_name)
        self.assertEqual(bio_data.age, expected_age)

    def test_to_json(self):
        expected_name = "Test Name"
        expected_age = 25
        bio_data = BioData(name=expected_name, age=expected_age)
        print(bio_data.to_json())
        self.assertNotEqual(bio_data.to_json(), None)

    def test_from_json(self):
        expected_name = "Test Name"
        expected_age = 25
        json_src = {'name': expected_name, 'age': expected_age}
        json_data = json.dumps(json_src)
        bio_data = BioData.from_json(json_data)
        self.assertNotEqual(bio_data, None)
        print(bio_data.__str__())
        print(bio_data)
        print(bio_data.to_json())
        self.assertEqual(bio_data.name, expected_name)
        self.assertEqual(bio_data.age, expected_age)
        with open('bio_data.json', 'w+') as f:
            f.write(str(bio_data.to_json()))
            f.flush()


if __name__ == '__main__':
    unittest.main()
