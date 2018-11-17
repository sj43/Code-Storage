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

    def elements(self, prefix):
        d = self._trie
        for char in prefix:
            if char in d:
                d = d[char]
            else:
                return []
        return [prefix + x for x in self._elements(d)]

    def _elements(self, d):
        result = []
        for c, v in d.items():
            if c == ENDS_HERE:
                subresult = ['']
            else:
                subresult = [c + s for s in self._elements(v)]
            result.extend(subresult)
        return result

    def print_trie(self):
        print(self._trie)


trie = Trie()
for word in WORDS:
    trie.insert(word)

def autocomplete(s):
    return trie.elements(s)

# trie.print_trie()

print(autocomplete('de'))
