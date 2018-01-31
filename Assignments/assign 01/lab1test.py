import unittest;
from firstT import firstTask;
class Test_firstTask(unittest.TestCase):
    def test_functionname(self):
        res = firstTask("mobile");
        self.assertEqual(res,"mbl");
if __name__ == '__main__':
    unittest.main();
