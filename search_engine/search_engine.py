def search(docs:list[str], text:str) -> list[str]:
    search_result:list[str] = []
    if not docs:
        return search_result

    for document in docs:
        if text.lower() in document['text'].lower().split():
            search_result.append(document['id'])
    
    return search_result