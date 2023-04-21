from typing import Optional

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer

nltk.download('punkt')
nltk.download('stopwords')

ARTICLES_PREPOSITIONS = {
    "english": ['the', 'a', 'an', 'in', 'on', 'at', 'for', 'to', 'of']
}

NEGATION_WORDS = {
    "spanish": [
        'no',
        'ni',
        'nunca',
        'jamas',
        'tampoco',
        'nadie',
        'nada',
        'ninguno',
        'ninguna',
        'ningunos',
        'ningunas',
        'ningun',
    ],
    "english": [
        'no',
        'nor',
        'not',
        'don',
        "don't",
        'ain',
        'aren',
        "aren't",
        'couldn',
        "couldn't",
        'didn',
        "didn't",
        'doesn',
        "doesn't",
        'hadn',
        "hadn't",
        'hasn',
        "hasn't",
        'haven',
        "haven't",
        'isn',
        "isn't",
        'mightn',
        "mightn't",
        'mustn',
        "mustn't",
        'needn',
        "needn't",
        'shan',
        "shan't",
        'shouldn',
        "shouldn't",
        'wasn',
        "wasn't",
        'weren',
        "weren't",
        'won',
        "won't",
        'wouldn',
        "wouldn't",
    ],
}


def trim(
    text: str, stemmer: Optional[str] = None, language: str = "english"
) -> str:

    if language not in stopwords.fileids():
        raise ValueError("Unsupported language")

    accepted_stemmers = ("snowball", "porter", "lancaster")
    if stemmer and stemmer not in accepted_stemmers:
        raise ValueError("Stemmer must be one of", accepted_stemmers)

    # merge contractions
    text = text.replace("'", "")

    nltk_stopwords = stopwords.words(language)
    words_to_exclude = set(
        nltk_stopwords + ARTICLES_PREPOSITIONS.get(language, [])
    ) - set(NEGATION_WORDS.get(language, []))

    # tokenize words, keep uppercase
    words = [
        word
        for word in nltk.word_tokenize(text)
        if word.lower() not in words_to_exclude
    ]

    if stemmer:
        if stemmer == "porter":
            stemmer = PorterStemmer()
        elif stemmer == "snowball":
            stemmer = SnowballStemmer(language)
        elif stemmer == "lancaster":
            stemmer = LancasterStemmer()
        words = [stemmer.stem(word) for word in words]

    # restore title_case and uppercase
    case_restored = []
    for i, word in enumerate(words):
        if words[i].istitle():
            word = word.title()
        elif words[i].isupper():
            word = word.upper()
        case_restored.append(word)

    # remove spaces
    trimmed = "".join(case_restored)
    return trimmed
