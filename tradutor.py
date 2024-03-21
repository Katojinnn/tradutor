from googletrans import Translator

LANGUAGES_FULL_NAME = {
    "ar": "Arabic",
    "pt": "Portuguese",
    "de": "German",
    "bn": "Bengali",
    "bg": "Bulgarian",
    "hr": "Croatian",
    "sl": "Slovenian",
    "sk": "Slovak",
    "es": "Spanish",
    "tl": "Tagalog",
    "fr": "French",
    "el": "Greek",
    "nl": "Dutch",
    "hu": "Hungarian",
    "id": "Indonesian",
    "en": "English",
    "it": "Italian",
    "lt": "Lithuanian",
    "pl": "Polish",
    "ro": "Romanian",
    "ru": "Russian",
    "sr": "Serbian",
    "sv": "Swedish",
    "th": "Thai",
    "tr": "Turkish",
    "zh-tw": "Chinese (Traditional)",
    "uk": "Ukrainian",
    "vi": "Vietnamese"
}

phrase = input("Digite a frase que deseja traduzir: ")

translator = Translator()

for language_code, language_name in LANGUAGES_FULL_NAME.items():
    translated_phrase = translator.translate(phrase, dest=language_code)
    print("Tradução para {}: {} \n".format(language_name, translated_phrase.text))