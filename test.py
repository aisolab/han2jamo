import unittest
from han2jamo import Han2Jamo


class Han2JamoTestCase(unittest.TestCase):
    def setUp(self):
        self.han2jamo = Han2Jamo()

    def test_str_to_jamo(self):
        target = "ㅇㅏㄴㄴㅕㅇ ㄴㅐ ㅇㅣㄹㅡㅁㅇㅡㄴ ㅃㅗㄹㅗㄹㅗㅇㅑ"
        output = self.han2jamo.str_to_jamo("안녕 내 이름은 뽀로로야")
        self.assertEqual(output, target)

    def test_jamo_to_char(self):
        target = "각"
        output = self.han2jamo.jamo_to_char("ㄱ", "ㅏ", "ㄱ")
        self.assertEqual(output, target)

    def test_jamo_to_str(self):
        source = "ㅇㅏㄴㄴㅕㅇ ㄴㅐ ㅇㅣㄹㅡㅁㅇㅡㄴ ㅃㅗㄹㅗㄹㅗㅇㅑ"
        target = "안녕 내 이름은 뽀로로야"
        output = self.han2jamo.jamo_to_str(source)
        self.assertEqual(output, target)

    def test_char_to_jamo(self):
        source = "안"
        target = ("ㅇ", "ㅏ", "ㄴ")
        output = self.han2jamo.char_to_jamo(source)
        self.assertEqual(output, target)
