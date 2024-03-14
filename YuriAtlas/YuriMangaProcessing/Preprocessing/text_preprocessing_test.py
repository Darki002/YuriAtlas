import unittest
from text_preprocessing import TextPreprocessor


class TextPreprocessorTest(unittest.TestCase):
    def test_normalize_lowercase_text(self):
        text = 'The QuIcK Brown fOx juMpS'
        preprocessor = TextPreprocessor(text)
        preprocessor.normalize()
        self.assertEqual("the quick brown fox jumps", preprocessor.text)

    def test_tokenize_tokens_without_punctuation(self):
        text = 'The quick, brown fox.'
        preprocessor = TextPreprocessor(text)
        preprocessor.tokenize()

        expected = ['The', 'quick', 'brown', 'fox']
        self.assertEqual(expected, preprocessor.text)

    def test_remove_stopwords_from_text(self):
        text = 'The quick fox is brown'
        preprocessor = TextPreprocessor(text)
        preprocessor.normalize().tokenize().remove_stopwords()

        expected = ['quick', 'fox', 'brown']
        self.assertEqual(expected, preprocessor.text)

    def test_lemmatize_text(self):
        text = 'The quick fox is running faster'
        preprocessor = TextPreprocessor(text)
        preprocessor.tokenize().lemmatize()

        expected = ['The', 'quick', 'fox', 'be', 'run', 'fast']
        self.assertEqual(expected, preprocessor.text)

    def test_process_chains_all_preprocessor_methode(self):

        preprocessor = TextPreprocessor("The quick, brown fox, is running fast.")
        preprocessor.process()
        result = preprocessor.text

        expected = ['quick', 'brown', 'fox', 'run', 'fast']
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
