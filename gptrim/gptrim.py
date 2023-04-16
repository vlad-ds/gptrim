import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer

nltk.download('punkt')
nltk.download('stopwords')

ARTICLES_PREPOSITIONS = [
        'the', 'a', 'an', 'in', 'on', 'at', 'for', 'to', 'of'
    ]

NEGATION_WORDS = ['no', 'nor', 'not', 'don', "don't", 'ain', 'aren',
                  "aren't", 'couldn', "couldn't", 'didn', "didn't",
                  'doesn', "doesn't", 'hadn', "hadn't", 'hasn',
                  "hasn't", 'haven', "haven't", 'isn', "isn't",
                  'mightn', "mightn't", 'mustn', "mustn't",
                  'needn', "needn't", 'shan', "shan't", 'shouldn',
                  "shouldn't", 'wasn', "wasn't", 'weren', "weren't",
                  'won', "won't", 'wouldn', "wouldn't"]

NLTK_STOPWORDS = stopwords.words("english")

WORDS_TO_EXCLUDE = NLTK_STOPWORDS + ARTICLES_PREPOSITIONS
WORDS_TO_INCLUDE = NEGATION_WORDS
WORDS_TO_EXCLUDE = set(WORDS_TO_EXCLUDE) - set(WORDS_TO_INCLUDE)


def trim(text: str,
           stemmer: str = "snowball") -> str:

    accepted_stemmers = ("snowball", "porter", "lancaster")
    if stemmer not in accepted_stemmers:
        raise ValueError("Stemmer must be one of", accepted_stemmers)

    # merge contractions
    text = text.replace("'", "")

    # tokenize words, keep uppercase
    tokenized = [word for word in nltk.word_tokenize(text) if word.lower() not in WORDS_TO_EXCLUDE]

    # stem words
    if stemmer == "porter":
        stemmer = PorterStemmer()
    elif stemmer == "snowball":
        stemmer = SnowballStemmer("english")
    elif stemmer == "lancaster":
        stemmer = LancasterStemmer()
    stemmed = [stemmer.stem(word) for word in tokenized]

    # restore title_case and uppercase
    case_restored = []
    for i, word in enumerate(stemmed):
        if tokenized[i].istitle():
            word = word.title()
        elif tokenized[i].isupper():
            word = word.upper()
        case_restored.append(word)

    # remove spaces
    trimmed = "".join(case_restored)
    return trimmed
