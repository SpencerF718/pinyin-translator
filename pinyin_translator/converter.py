from pypinyin import pinyin, Style

def convert_to_pinyin(text, use_tone_marks=True):
    style = Style.TONE if use_tone_marks else Style.TONE3
    result = pinyin(text, style=style, strict=False, errors='default')
    return " ".join(item[0] for item in result)
