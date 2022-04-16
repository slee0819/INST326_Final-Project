# Add the function that was missing in the first module test and check if it works after debugging.

import unittest
import os


def custom_function(file_name):
    with open(file_name, 'rt') as f:
        return sum(1 for _ in f)


# Write the Testcase
class CustomTests(unittest.TestCase):

    def setUp(self):
        """Write the file before the test starts"""
        self.file_name = 'test_file.txt'
        with open(self.file_name, 'wt') as f:
            f.write("""
            Hello
            world
            Thanks!
            """.strip())

    def tearDown(self):
        """ After test delete the file"""
        try:
            os.remove(self.file_name)
        except:
            pass

    def test_runs(self):
        """Test method to determine whether simple execution"""

        custom_function(self.file_name)

    def test_line_count(self):
        self.assertEqual(custom_function(self.file_name), 3)


# Start the unittest
if __name__ == '__main__':
    unittest.main()
    
# Two tests are run and show success.
