def capitalize_words(words: str) -> str:
    return ' '.join(word.capitalize() for word in words.split())