import unittest
from parser import Parser

class TestParser(unittest.TestCase):

    def test_get_enforcement_action_detail_links(self):
            test_page = '<a href="/newsroom/"></a><p>lr123.txt</p><a href="/enforcement/actions/foo/"></a><a href=/enforcement/actions/bar/></a>'
            expected_links = ['/enforcement/actions/foo/', '/enforcement/actions/bar/']
            self.assertCountEqual(Parser.get_enforcement_action_detail_links(test_page), expected_links)

    def test_is_last_enforcement_action_filter_page_enabled_button_should_return_false(self):
        test_page = '<p>blah</p><div><a class="a-btn m-pagination_btn-next"></a></div>'
        self.assertFalse(Parser.is_last_enforcement_action_filter_page(test_page))

    def test_is_last_enforcement_action_filter_page_disabled_button_should_return_true(self):
        test_page = '<div><a class="a-btn a-btn__disabled m-pagination_btn-next"></a></div>'
        self.assertTrue(Parser.is_last_enforcement_action_filter_page(test_page))

if __name__ == '__main__':
    unittest.main()