import unittest;
from sixT import myfun;
class Test_arc(unittest.TestCase):
    def test_arc(self):
        res =myfun(4);
        out=['   *', '  **', ' ***','****'];
        self.assertEqual(res,out);
if __name__ == '__main__':
    unittest.main();
