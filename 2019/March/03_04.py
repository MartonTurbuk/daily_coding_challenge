# This problem was asked by Amazon.
#
# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct
# characters.
#
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".


# Own solution
def distinct_chars(text):
    cache = ''
    temp_cache = ''
    for char in text:
        if char not in cache:
            cache += char
        else:
            temp_cache = cache.replace(char, '')
            # Meg kell nézni, hogy van-e következő karakter vagy nincs. Ha nincs akkor nem kell nullázni ha van akkor
            # igen.
            cache = ''
    return cache if len(cache) > len(temp_cache) else temp_cache


print(distinct_chars('abcdadfgh'))


# Solution of the dailyCodingChallenge team
def longest_substring_with_k_distinct_characters(s, k):
    current_longest_substring = ''
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if len(set(substring)) <= k and len(substring) > len(current_longest_substring):
                current_longest_substring = substring
    return len(current_longest_substring)


# Improved version
def longest_substring_with_k_distinct_characters_2(s, k):
    if k == 0:
        return 0

    # Keep a running window
    bounds = (0, 0)
    h = {}
    max_length = 0
    for i, char in enumerate(s):
        h[char] = i
        if len(h) <= k:
            new_lower_bound = bounds[0]  # lower bound remains the same
        else:
            # otherwise, pop last occurring char
            key_to_pop = min(h, key=h.get)
            new_lower_bound = h.pop(key_to_pop) + 1

        bounds = (new_lower_bound, bounds[1] + 1)
        max_length = max(max_length, bounds[1] - bounds[0])

    return max_length
