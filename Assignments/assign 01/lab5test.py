import unittest;
from fiveT import dictionary;
class Test_dictionary(unittest.TestCase):
    def test_dictionary(self):
        l=["ahmad","emad","rizk","omnya","adel","samr","islam"];
        res = dictionary(l);
        out={'a': ['ahmed', 'adel'], 'i': ['islam'], 'r': ['rizk'], 'o': ['omneya'], 's': ['samar']};
        self.assertEqual(res,out);
if __name__ == '__main__':
    unittest.main();
