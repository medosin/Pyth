import unittest;
from FourT import calcArea;
class Test_calcArea(unittest.TestCase):
    def test_calcArea(self):
        res = calcArea("c",10);
        self.assertEqual(res,314.0);
if __name__ == '__main__':
    unittest.main();
