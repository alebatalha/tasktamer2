def haystack_available():
    try:
        import haystack
        return True
    except ImportError:
        return False

def nltk_available():
    try:
        import nltk
        try:
            nltk.data.find('tokenizers/punkt')
            nltk.data.find('corpora/stopwords')
            return True
        except LookupError:
            try:
                nltk.download('punkt')
                nltk.download('stopwords')
                return True
            except:
                return False
    except ImportError:
        return False

USING_FALLBACK = not haystack_available()
USING_NLTK = nltk_available()
USING_NLTK_WITH_HAYSTACK = not USING_FALLBACK and USING_NLTK
USING_NLTK_FALLBACK = USING_NLTK