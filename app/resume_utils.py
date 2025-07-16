import nltk
from pdfminer.high_level import extract_text

def extract_text_from_pdf(uploaded_file):
    return extract_text(uploaded_file)

def extract_keywords(text):
    try:
        # Try loading stopwords: common English words (and, or...)
        stopwords = set(nltk.corpus.stopwords.words('english'))
    except LookupError:
        # If not found, download once and try again
        nltk.download('stopwords')
        stopwords = set(nltk.corpus.stopwords.words('english'))
        
    words = text.lower().split()
    keywords = [word for word in words if word.isalpha() and word not in stopwords]
    return set(keywords)

def compare_keywords(resume_keywords, jd_keywords):
    matched = resume_keywords & jd_keywords
    missing = jd_keywords - resume_keywords
    score = int((len(matched) / len(jd_keywords)) * 100) if jd_keywords else 0
    return matched, missing, score