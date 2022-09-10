'''unit test file'''
import unittest

from translator import english_to_french, french_to_english

class InputTest(unittest.TestCase):
    '''input test class'''
    def test_null(self):
        '''default input tests'''
        self.assertTrue(english_to_french('hello').
        get_result()['translations'][0]['translation'])
        self.assertTrue(french_to_english('bonjour').
        get_result()['translations'][0]['translation'])

class TranslationTest(unittest.TestCase):
    '''translation test class'''
    def test_translation(self):
        '''default translation tests'''
        self.assertEqual(english_to_french('Hello').
        get_result()['translations'][0]['translation'], 'Bonjour')
        self.assertEqual(french_to_english('Bonjour').
        get_result()['translations'][0]['translation'], 'Hello')

if __name__ == '__main__':
    unittest.main()
