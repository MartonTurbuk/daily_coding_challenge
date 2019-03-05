# This problem was asked by Twitter.
#
# Implement an autocomplete system. That is, given a query string s and a set of
# all possible query strings, return all strings in the set that have s as a prefix.
#
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
#
# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

# My own solutions

query = 'de'

strings = ['dog', 'deer', 'deal']


def auto_complete(q, string_list):
    result_list = set()
    for chars in string_list:
        if q in chars[:2]:
            result_list.add(chars)

    return result_list


def auto_complete_2(q, string_list):
    return {chars for chars in string_list if q in chars[:2]}


print(auto_complete(query, strings))

print(auto_complete_2(query, strings))

# DailyCoding solutions:

words_1 = ['foo', 'bar', ...]


def autocomplete(s):
    results = set()
    for word in words_1:
        if word.startswith(s):
            results.add(word)
    return results


ENDS_HERE = '__ENDS_HERE'

words = ['foo', 'bar']


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
        return self._elements(d)

    def _elements(self, d):
        result = []
        for c, v in d.items():
            if c == ENDS_HERE:
                subresult = ['']
            else:
                subresult = [c + s for s in self._elements(v)]
            result.extend(subresult)
        return result


trie = Trie()
for word in words:
    trie.insert(word)


def autocomplete(s):
    suffixes = trie.elements(s)
    return [s + w for w in suffixes]


