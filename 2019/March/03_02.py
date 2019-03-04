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
    return [chars for chars in string_list if q in chars[:2]]


print(auto_complete(query, strings))

print(auto_complete_2(query, strings))
