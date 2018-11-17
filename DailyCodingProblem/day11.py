WORDS = ['dog', 'deer', 'deal']


# O(N) naive method

def autocomplete(s):
    results = set()
    for word in WORDS:
        if word.startswith(s):
            results.add(word)
    return results


print(autocomplete('de'))


# pre-process the dictionary with Trie structure and search with it. This way, at most O(N) (when every word in dictionary starts with the prefix we are looking for)
ENDS_HERE = '__ENDS_HERE'


class Trie(object):
    def __init__(self):
        self._trie = {}

    def insert(self, text):
        trie = self._trie
        for char in text:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie[ENDS_HERE] = True
