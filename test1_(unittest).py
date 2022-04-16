# First Create a test method to determine whether or not to simply execute. 

import unittest

# Write the testcase 
class CustomTests(unittest.TestCase):

    def test_runs(self):
        """Test method to determine whether simple execution """

        custom_function()

# Start the unittest 
if __name__ == '__main__':
    unittest.main()
    
# Since we didn't write custom_function() it doesn't work when I debugged it.

