from pinyin_translator.converter import convert_to_pinyin
from pinyin_translator.html_output import to_html
import webbrowser

def main():
    chinese_text = input("Enter your Chinese text:\n> ").strip()
    if not chinese_text:
        print("No input provided.")
        return

    print("\nUse tone marks or tone numbers?")
    print("1 - Tone marks (e.g., nǐ hǎo)")
    print("2 - Tone numbers (e.g., ni3 hao3)")
    tone_choice = input("> ").strip()

    use_tone_marks = tone_choice != "2"
    pinyin = convert_to_pinyin(chinese_text, use_tone_marks)

    print("\nWhere do you want the output?")
    print("1 - Console")
    print("2 - Text file")
    print("3 - HTML file")
    output_choice = input("> ").strip()

    if output_choice == "1":
        print("\nYour Pinyin Output:\n")
        print(pinyin)

    elif output_choice == "2":
        filename = input("Enter output filename (e.g. output.txt):\n> ").strip()
        if not filename:
            print("No filename provided.")
            return
        with open(filename, "w", encoding="utf-8") as f:
            f.write(pinyin)
        print(f"Pinyin written to {filename}")

    elif output_choice == "3":
        filename = input("Enter HTML output filename (e.g. output.html):\n> ").strip()
        if not filename:
            print("No filename provided.")
            return
        html = to_html(pinyin)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"HTML output written to {filename}")
        webbrowser.open(filename)

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
