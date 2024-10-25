import unittest
import json
import chopper
import os
import shutil

class TestChopper(unittest.TestCase):
    def setUp(self):
        os.makedirs("test", exist_ok=True)
        self.sample = json.loads(open("src\jsoncards\sample.json").read())

    def tearDown(self):
        shutil.rmtree("test")

    def test_chopping(self):
        chopper.chop_and_save(self.sample, 3, "test", "test")
        self.assertEqual(len(os.listdir("test")), 3)

    def test_joining(self):
        chopper.chop_and_save(self.sample, 3, "test", "test")
        joined = chopper.join("test", "test")
        self.assertEqual(self.sample, joined)

if __name__ == "__main__":
    unittest.main()