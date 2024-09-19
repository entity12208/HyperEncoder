import unittest
from src.main import encode, decode

class TestHyperEncoder(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(encode("hello"), "aGVsbG8=")
    
    def test_decode(self):
        self.assertEqual(decode("aGVsbG8="), "hello")

if __name__ == '__main__':
    unittest.main()
