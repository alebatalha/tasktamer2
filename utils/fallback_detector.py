def haystack_available():
    try:
        import haystack
        return True
    except ImportError:
        return False

def nltk_available():
    try:
        import nltk
        return True
    except ImportError:
        return False

def youtube_transcript_api_available():
    try:
        import youtube_transcript_api
        return True
    except ImportError:
        return False


USING_FALLBACK = not haystack_available()
USING_NLTK = nltk_available()
USING_NLTK_WITH_HAYSTACK = not USING_FALLBACK and USING_NLTK
USING_NLTK_FALLBACK = USING_NLTK
USING_YOUTUBE_API = youtube_transcript_api_available()