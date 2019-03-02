numbers = [10, 15, 3, 7]

k = 17


def two_sum(lst, number):
    seen = set()
    for num in lst:
        if number - num in seen:
            return True
        seen.add(num)
    return False


print(two_sum(numbers, k))


