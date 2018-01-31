import unittest;
from secondT import two;
class Test_two(unittest.TestCase):
    def test_functionname(self):
        res = two("this is javaScript",'i');
        out=[2,5,15];
        self.assertEqual(res,out);
if __name__ == '__main__':
    unittest.main();
