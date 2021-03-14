import unittest
from parser import Parser

class TestParser(unittest.TestCase):

    def test_get_litgation_links(self):
        test_page = '<p>lr123.txt</p><a href="/litigation/litreleases/lr1234.htm"></a><a href=/litigation/litreleases/lr1235.txt></a>'
        expected_links = ['/litigation/litreleases/lr1234.htm', '/litigation/litreleases/lr1235.txt']
        self.assertCountEqual(Parser.get_litigation_links(test_page), expected_links)

if __name__ == '__main__':
    unittest.main()