import re


def search(docs: list[dict], text: str) -> list[str]:
    if not docs:
        return []

    clean_words: list[str] = re.findall(r"[\w']+", text.lower())
    search_freq: dict = {}
    for document in docs:
        doc_words = re.findall(r"[\w']+", document['text'].lower())
        for word in clean_words:
            if word in doc_words:
                words_count = doc_words.count(word)
                if words_count > 0:
                    search_freq[document['id']] = search_freq.get(document['id'], 0) + words_count
    
    search_result: list[str] = [k for k, v in sorted(search_freq.items(), key=lambda item: -item[1])]
    return search_result