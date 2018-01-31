import unittest;
from thirdT import three;
class Test_three(unittest.TestCase):
    def test_multiplyTable(self):
        res = multiplyTable(3);
        out=[[1],[2,4],[3,6,9]];
        self.assertEqual(res,out);
if __name__ == '__main__':
    unittest.main();
