import unittest
import sys

sys.path.insert(0, '../anagrams')
import anagrams

expected_cases = [
    ('', ''),
    ('kevin', 'nivek'),
    ('kevin alone at home', 'nivek enola ta emoh'),
    ('ke!vin al2one at ho*me', 'ni!vek en2ola ta em*oh'),
    ('русский текст', 'йикссур тскет'),
    ('українский текст', 'йикснїарку тскет'),
    ('%*&)(@! *((()))$', '%*&)(@! *((()))$'),
    ('aannaggrrams', 'smarrggannaa'),
    ('KeVin', 'niVeK'),
]

unexpected_cases = [
    (1, TypeError),
    (True, TypeError),
    (1+2j, TypeError),
    (0, TypeError),
]


class TestAnagrams(unittest.TestCase):
    def test_works_as_expected(self):
        for p, exp in expected_cases:
            with self.subTest():
                self.assertEqual(anagrams.reverse_words(p), exp)

    def test_works_as_not_expected(self):
        for p, exp in unexpected_cases:
            with self.subTest():
                self.assertRaises(exp, anagrams.reverse_words, p)


if __name__ == '__main__':
    unittest.main()
