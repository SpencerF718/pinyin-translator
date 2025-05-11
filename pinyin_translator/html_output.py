from pinyin_translator.utils import get_tone_number

def to_html(pinyin_text, title="Pinyin Output"):
    pinyin_words = pinyin_text.split()

    pinyin_cells = []
    for word in pinyin_words:
        tone = get_tone_number(word)
        if tone == 0:
            pinyin_cells.append(f"<span>{word}</span>")
        else:
            pinyin_cells.append(f'<span class="tone tone{tone}">{word}</span>')

    pinyin_row = " ".join(pinyin_cells)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        body {{
            font-family: "Segoe UI", sans-serif;
            background-color: #1e1e1e;
            margin: 0;
            padding: 0;
            color: #f0f0f0;
        }}
        .container {{
            max-width: 900px;
            margin: 40px auto;
            background-color: #2b2b2b;
            padding: 2rem 2.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            overflow-x: auto;
        }}
        h1 {{
            font-size: 1.8em;
            text-align: center;
            margin-bottom: 1.5rem;
        }}
        .legend {{
            font-size: 1em;
            text-align: center;
            margin-bottom: 1.8rem;
        }}
        .legend span {{
            font-weight: bold;
            margin: 0 0.5em;
            padding: 0.2em 0.5em;
            border-radius: 5px;
            color: white;
        }}
        .tone1 {{ background-color: rgba(231, 76, 60, 0.7); }}
        .tone2 {{ background-color: rgba(243, 156, 18, 0.7); }}
        .tone3 {{ background-color: rgba(39, 174, 96, 0.7); }}
        .tone4 {{ background-color: rgba(52, 152, 219, 0.7); }}

        .tone {{
            padding: 0.2em 0.4em;
            border-radius: 6px;
            margin: 0 0.25em;
            display: inline-block;
        }}

        .copy-section {{
            text-align: center;
            margin-bottom: 2rem;
        }}
        .copy-button {{
            padding: 0.5em 1.2em;
            font-size: 1em;
            border: none;
            border-radius: 6px;
            background-color: #4a90e2;
            color: white;
            cursor: pointer;
        }}
        .copy-button:hover {{
            background-color: #357ab7;
        }}
        #rawPinyin {{
            display: none;
        }}

        .pinyin {{
            font-size: 1.6em;
            text-align: center;
            line-height: 2em;
            letter-spacing: 0.08em;
            word-spacing: 1em;
            padding: 1rem 0;
        }}

        @media print {{
            body {{
                background-color: white;
                color: black;
            }}
            .container {{
                box-shadow: none;
                background-color: white;
                color: black;
                padding: 1.5rem;
            }}
            .tone {{
                background-color: transparent !important;
                color: black !important;
                border-radius: 0;
            }}
            .legend,
            .copy-section {{
                display: none;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{title}</h1>

        <div class="copy-section">
            <button class="copy-button" onclick="copyPinyin()">Copy Pinyin</button>
        </div>

        <div class="legend">
            <strong>Tone Color Key:</strong><br><br>
            <span class="tone1">Tone 1</span>
            <span class="tone2">Tone 2</span>
            <span class="tone3">Tone 3</span>
            <span class="tone4">Tone 4</span>
        </div>

        <div class="pinyin">
            {pinyin_row}
        </div>
    </div>

    <textarea id="rawPinyin">{pinyin_text}</textarea>

    <script>
        function copyPinyin() {{
            const text = document.getElementById("rawPinyin").value;
            navigator.clipboard.writeText(text).then(() => {{
                alert("Pinyin copied to clipboard");
            }});
        }}
    </script>
</body>
</html>
"""
    return html
