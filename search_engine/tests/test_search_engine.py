import pytest

from search_engine.search_engine import search


@pytest.fixture
def docs():
    doc1 = "I can't shoot straight unless I've had a pint!"
    doc2 = "Don't shoot shoot shoot that thing at me."
    doc3 = "I'm your shooter."
    docs = [
            {'id': 'doc1', 'text': doc1},
            {'id': 'doc2', 'text': doc2},
            {'id': 'doc3', 'text': doc3},
            ]
    return docs


def test_search_basic(docs):
    assert search(docs, 'shoot') == ['doc2', 'doc1']
    assert search([], 'shoot') == []


def test_search_with_punctuation(docs):
    assert search(docs, 'pint') == ['doc1']
    assert search(docs, 'pint!') == ['doc1']
