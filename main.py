from googletrans import Translator, LANGUAGES

def CodeLang(lang: str) -> str:
    """
    Повертає код за назвою мови або навпаки.
    """
    lang = lang.lower()
    
   
    if lang in LANGUAGES:
        return LANGUAGES[lang].capitalize()
    
    
    for code, name in LANGUAGES.items():
        if name.lower() == lang:
            return code
            
    return "Error: Language not found"

def LangDetect(txt: str) -> str:
    """
    Визначає мову тексту та впевненість (confidence).
    """
    try:
        translator = Translator()
        result = translator.detect(txt)
        return f"Detected(lang={result.lang}, confidence={result.confidence})"
    except Exception as e:
        return f"Error: {e}"

def TransLate(str_txt: str, lang: str) -> str:
    """
    Перекладає текст на задану мову.
    """
    try:
        translator = Translator()
        target_lang = lang.lower()
        if target_lang not in LANGUAGES:
            target_lang = CodeLang(lang)
            
        if "Error" in target_lang:
            return target_lang

        translated = translator.translate(str_txt, dest=target_lang)
        return translated.text
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    txt = "Доброго дня. Як справи?"
    lang = "en"
    
    print(txt)
    print(LangDetect(txt))
    print(TransLate(txt, lang))
    print(CodeLang("En"))
    print(CodeLang("English"))