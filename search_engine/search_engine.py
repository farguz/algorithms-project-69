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
                count = doc_words.count(word)
                if count > 0:
                    doc_id = document['id']
                    search_freq[doc_id] = search_freq.get(doc_id, 0) + count
    
    sorted_items = sorted(search_freq.items(), key=lambda item: -item[1])
    search_result: list[str] = [k for k, v in sorted_items]
    return search_result


def inverted_index(docs: list[dict], text: str) -> dict:
    clean_words: list[str] = re.findall(r"[\w']+", text.lower())
    index_result: dict = {}
    for document in docs:
        doc_words: set = set(re.findall(r"[\w']+", document['text'].lower()))
        for word in clean_words:
            if word in doc_words:
                index_result.setdefault(word, []).append(document['id'])

    return index_result
    
    

