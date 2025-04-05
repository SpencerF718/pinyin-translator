# Pinyin Translator

Convert Simplified Chinese text into **pinyin** (with tone marks or tone numbers), and output it as a **clean, dark-themed HTML page** — complete with:
- Tone color highlights
- Hover tooltips for tone info
- Copy button for raw pinyin
- Console, text file, or HTML export

---

## Screenshots

### HTML Output with Dark Mode
![HTML Output](images/html_output.png)

---

## Features

- Accepts input from user prompt
- Choose tone marks (e.g., `nǐ hǎo`) or tone numbers (`ni3 hao3`)
- Output to:
  - Console
  - `.txt` file
  - `.html` file
- HTML with dark mode, chunked layout, and responsive design
- Copy button to grab just the pinyin

---

## How to Set Up

### 1. Clone the repository

```bash
git clone https://github.com/SpencerF718/pinyin-translator.git
cd pinyin-translator
```

### 2. Install dependencies

Using the `requirements.txt`:
```bash
pip install -r requirements.txt
```

Or if you just want to install manually:
```bash
pip install pypinyin
```

---

## How to Run

Just run the main program and follow the prompts:

```bash
python main.py
```

You'll be asked to:
1. Enter your Chinese text
2. Choose tone formatting (marks or numbers)
3. Choose your output format (console, text, or HTML)

---

## Credits

Built with Python and [pypinyin](https://github.com/mozillazg/python-pinyin)  

---
