import unittest
from pinyin_translator.converter import convert_to_pinyin

class TestConverter(unittest.TestCase):

    def test_with_tone_marks(self):
        result = convert_to_pinyin("你好", use_tone_marks=True)
        self.assertEqual(result, "nǐ hǎo")

    def test_with_tone_numbers(self):
        result = convert_to_pinyin("你好", use_tone_marks=False)
        self.assertEqual(result, "ni3 hao3")

    def test_empty_string(self):
        result = convert_to_pinyin("", use_tone_marks=True)
        self.assertEqual(result, "")

    def test_punctuation_marks(self):
        result = convert_to_pinyin("你好！", use_tone_marks=True)
        self.assertEqual(result, "nǐ hǎo ！")

    def test_mixed_chinese_english(self):
        result = convert_to_pinyin("你好, world!", use_tone_marks=False)
        self.assertEqual(result, "ni3 hao3 , world!")

    def test_full_sentence(self):
        text = "今天天气很好，我们去公园吧。"
        expected = "jīn tiān tiān qì hěn hǎo ， wǒ men qù gōng yuán ba 。"
        result = convert_to_pinyin(text, use_tone_marks=True)
        self.assertEqual(result, expected)

    def test_numbers_and_symbols(self):
        text = "你好123！？"
        expected = "nǐ hǎo 123！？"
        result = convert_to_pinyin(text, use_tone_marks=True)
        self.assertEqual(result, expected)

    def test_neutral_tone(self):
        text = "我的"
        result = convert_to_pinyin(text, use_tone_marks=True)
        self.assertTrue("de" in result or "de" == result.split()[-1])

if __name__ == "__main__":
    unittest.main()
