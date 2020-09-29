import unittest
from anagrams import anagrams


class TestAnagrams(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(anagrams.reverse_words(''), '')

    def test_one_word(self):
        self.assertEqual(anagrams.reverse_words('kevin'), 'nivek')

    def test_words(self):
        self.assertEqual(anagrams.reverse_words('kevin alone at home'), 'nivek enola ta emoh')

    def test_words_with_another_symbols(self):
        self.assertEqual(anagrams.reverse_words('ke!vin al2one at ho*me'), 'ni!vek en2ola ta em*oh')

    def test_words_in_russian(self):
        self.assertEqual(anagrams.reverse_words('русский текст'), 'йикссур тскет')

    def test_words_in_ukrainian(self):
        self.assertEqual(anagrams.reverse_words('українский текст'), 'йикснїарку тскет')

    def test_only_symbols(self):
        self.assertEqual(anagrams.reverse_words('%*&)(@! *((()))$'), '%*&)(@! *((()))$')

    def test_repeated_words(self):
        self.assertEqual(anagrams.reverse_words('aannaggrrams'), 'smarrggannaa')

    def test_upper_lower_cases(self):
        self.assertEqual(anagrams.reverse_words('KeVin'), 'niVeK')

    def test_digit(self):
        self.assertRaises(TypeError, anagrams.reverse_words, 1)

    def test_boolean(self):
        self.assertRaises(TypeError, anagrams.reverse_words, True)



if __name__ == '__main__':
    unittest.main()