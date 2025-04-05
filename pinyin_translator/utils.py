import re

def get_tone_number(pinyin_syllable):
    """
    Extract the tone number from a pinyin syllable.
    Handles both tone marks (e.g., hǎo) and tone numbers (e.g., hao3).
    Returns 1–4, or 0 if no tone is found.
    """
    tone_marks = {
        'āēīōūǖ': 1,
        'áéíóúǘ': 2,
        'ǎěǐǒǔǚ': 3,
        'àèìòùǜ': 4
    }

    # Check for tone marks
    for marks, tone in tone_marks.items():
        if any(char in pinyin_syllable for char in marks):
            return tone

    # Check for tone numbers (e.g., "hao3")
    match = re.search(r'\d$', pinyin_syllable)
    if match:
        tone = int(match.group())
        if 1 <= tone <= 4:
            return tone

    return 0  # Neutral tone
