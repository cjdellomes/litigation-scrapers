import unittest
from parser import Parser

class TestParser(unittest.TestCase):

    def get_enforcement_action_detail_links(self):
            test_page = '<a href="/newsroom/"></a><p>lr123.txt</p><a href="/enforcement/actions/foo/"></a><a href=/enforcement/actions/bar/></a>'
            expected_links = ['/enforcement/actions/foo/', '/enforcement/actions/bar/']
            self.assertCountEqual(Parser.get_litigation_links(test_page), expected_links)

if __name__ == '__main__':
    unittest.main()