from deep_translator import GoogleTranslator

def translate_text(text, target_language):
    try:
        translated = GoogleTranslator(source='auto', target=target_language).translate(text)
        return translated
    except Exception as e:
        print(f"Translation error: {e}")
        return text

if __name__ == "__main__":
    sample = "This file contains two functions and one class related to file reading."
    lang = input("Translate to (e.g., hi for Hindi, fr for French): ")
    print(translate_text(sample, lang))
