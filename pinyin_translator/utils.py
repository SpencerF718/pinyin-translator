import re

def get_tone_number(pinyin_syllable):

    tone_marks = {
        'āēīōūǖ': 1,
        'áéíóúǘ': 2,
        'ǎěǐǒǔǚ': 3,
        'àèìòùǜ': 4
    }

    for marks, tone in tone_marks.items():
        if any(char in pinyin_syllable for char in marks):
            return tone

    match = re.search(r'\d$', pinyin_syllable)
    if match:
        tone = int(match.group())
        if 1 <= tone <= 4:
            return tone

    return 0 
