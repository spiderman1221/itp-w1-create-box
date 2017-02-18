import unittest

from create_box import create_box
from create_box import extra_space_box

first_box_expected = """
****
****
****
""".lstrip()

second_box_expected = """
@
""".lstrip()

third_box_expected = """
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
""".lstrip()

fourth_box_expected = """
*****
*   *
*   *
*   *
*****
""".lstrip()

class TestCreateBox(unittest.TestCase):
    def test_box(self):
        self.assertEqual(create_box(3, 4, '*'), first_box_expected)

    def test_small_box(self):
        self.assertEqual(create_box(1, 1, '@'), second_box_expected)

    def test_big_box(self):
        self.assertEqual(create_box(3,24,'x'), third_box_expected)
        
    def test_empty_space(self):
        self.assertEqual(extra_space_box(5,5,'*'), fourth_box_expected)
        # Add your own test using third_box_expected

# # _______________________________________________________________________________
#     def test_empty_space(self):
# >       self.assertEqual(extra_space_box(5,5,'*'), fourth_box_expected)
# E       AssertionError: '*****\n*   *\n*   *\n*   *\n*****' != '*****\n*   *\n*   *\n*   *\n*****\n'