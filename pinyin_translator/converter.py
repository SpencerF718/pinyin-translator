from pypinyin import pinyin, Style

def convert_to_pinyin(text, use_tone_marks=True):
    """
    Converts Simplified Chinese Characters into Pinyin.

    Args:
        text (str): Chinese Characters to convert into Pinyin.
        use_tone_marks (bool): If True, uses unicode tone marks over vowels to indicate tones.
                               If False, uses tone numbers.

    Returns: 
        str: Pinyin translation of the Simplified Chinese Characters.
    """

    style = Style.TONE if use_tone_marks else Style.TONE3

    pinyin_list = pinyin(text, style=style, strict=False)
    flat = [item[0] for item in pinyin_list]

    return ' '.join(flat)
