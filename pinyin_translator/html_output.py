from pinyin_translator.utils import get_tone_number

def to_html_with_characters(chinese_text, pinyin_text, title="Pinyin Output", chunk_size=12):
    characters = list(chinese_text)
    pinyin_words = pinyin_text.split()

    # Break into chunks
    rows = []
    pinyin_lines = []  # For JS copy block
    for i in range(0, len(characters), chunk_size):
        chunk_chars = characters[i:i + chunk_size]
        chunk_pinyin = pinyin_words[i:i + chunk_size]

        chinese_row = "<tr>" + "".join(f"<td class='char'>{char}</td>" for char in chunk_chars) + "</tr>"

        pinyin_cells = []
        raw_line = []  # To collect raw text
        for j, char in enumerate(chunk_chars):
            word = chunk_pinyin[j] if j < len(chunk_pinyin) else ""
            tone = get_tone_number(word)
            tooltip = f"Tone {tone}" if tone in {1, 2, 3, 4} else "Neutral tone"
            raw_line.append(word)

            if tone == 0:
                pinyin_cells.append(f"<td class='pinyin' title='{tooltip}'>{word}</td>")
            else:
                pinyin_cells.append(
                    f"<td class='pinyin' title='{tooltip}'><span class='tone{tone}'>{word}</span></td>"
                )

        pinyin_row = "<tr>" + "".join(pinyin_cells) + "</tr>"

        rows.append(chinese_row)
        rows.append(pinyin_row)
        pinyin_lines.append(" ".join(raw_line))

    full_table = "\n".join(rows)
    raw_pinyin_text = "\n".join(pinyin_lines)

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
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }}
        h1 {{
            font-size: 1.8em;
            text-align: center;
            margin-bottom: 1rem;
            color: #ffffff;
        }}
        .legend {{
            font-size: 1em;
            text-align: center;
            margin-bottom: 1.5rem;
        }}
        .legend span {{
            font-weight: bold;
            margin: 0 0.5em;
            padding: 0.2em 0.5em;
            border-radius: 5px;
            color: white;
        }}
        .tone1 {{ background-color: #e74c3c; }}
        .tone2 {{ background-color: #f39c12; }}
        .tone3 {{ background-color: #27ae60; }}
        .tone4 {{ background-color: #3498db; }}

        .copy-section {{
            text-align: center;
            margin-bottom: 1.5rem;
        }}
        .copy-button {{
            padding: 0.5em 1em;
            font-size: 1em;
            border: none;
            border-radius: 5px;
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

        table {{
            width: 100%;
            border-collapse: separate;
            border-spacing: 0.4em 0.3em;
            text-align: center;
            font-size: 1.4em;
        }}
        td {{
            padding: 0.3em 0.5em;
            background-color: #3a3a3a;
            border-radius: 8px;
            word-wrap: break-word;
            white-space: nowrap;
            vertical-align: middle;
        }}
        .pinyin, .char {{
            vertical-align: middle;
        }}
        .tone1, .tone2, .tone3, .tone4 {{
            display: inline-block;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{title}</h1>

        <div class="copy-section">
            <button class="copy-button" onclick="copyPinyin()">📋 Copy Pinyin</button>
        </div>

        <div class="legend">
            <strong>Tone Color Key:</strong><br><br>
            <span class="tone1">Tone 1</span>
            <span class="tone2">Tone 2</span>
            <span class="tone3">Tone 3</span>
            <span class="tone4">Tone 4</span>
        </div>

        <table>
            {full_table}
        </table>
    </div>

    <textarea id="rawPinyin">{raw_pinyin_text}</textarea>

    <script>
        function copyPinyin() {{
            const text = document.getElementById("rawPinyin").value;
            navigator.clipboard.writeText(text).then(() => {{
                alert("✅ Pinyin copied to clipboard!");
            }});
        }}
    </script>
</body>
</html>
"""
    return html
