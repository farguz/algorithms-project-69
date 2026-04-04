import re
import string


def search(docs: list[dict], text: str) -> list[str]:
    search_result: dict[str] = []
    if not docs:
        return search_result

    clean_word: str = text.lower().strip(string.punctuation)
    search_freq: dict = {}
    for document in docs:
        words = re.findall(r'\w+', document['text'].lower())
        search_freq[document['id']] = search_freq.get(document['id'], 0) + words.count(clean_word)

    search_result = [k for k, v in sorted(search_freq.items(), key=lambda item: -item[1]) if v != 0]
    return search_result
