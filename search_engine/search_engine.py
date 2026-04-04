import re
import string

def search(docs:list[dict], text:str) -> list[str]:
    search_result:list[str] = []
    if not docs:
        return search_result

    clean_word:str = text.lower().strip(string.punctuation)

    for document in docs:
        words:set[str] = set(re.findall(r'\w+', document['text'].lower()))
        if clean_word in words:
            search_result.append(document['id'])

    return search_result