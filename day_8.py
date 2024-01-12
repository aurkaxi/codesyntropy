# sum of arbitary arguments
def sum(*args: int) -> int:
    total = 0
    for i in args:
        total += i
    return total


print(f"Sum: {sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}")


# average of arbitary arguments
def average(*args: float) -> float:
    total = 0
    for i in args:
        total += i
    return total / len(args)


print(f"Average: {average(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}")


# maximum of arbitary number of arguments
def maximum(*args: float) -> float:
    return max(args)


print(f"Maximum: {maximum(1, 2, 3, 4, 5, 16, 7, 8, 9, 10)}")


# minimum of arbitary number of arguments
def minimum(*args: float) -> float:
    return min(args)


print(f"Minimum: {minimum(1, 2, 3, 4, 5, 16, 7, 8, 9, 10)}")


# concatenate strings
def con_str(*args: str) -> str:
    return "".join(args)


print(f"Concatenate: {con_str('Hello', 'World', 'Python', 'is', 'Awesome')}")


# count occurence
def count_occurence(*args: int):
    uniques: set[int] = set()
    for i in range(len(args)):
        if args[i] in uniques:
            continue

        print(f"{args[i]}: {args.count(args[i])}")
        uniques.add(args[i])


print("Count Occurence: ")
count_occurence(1, 2, 3, 4, 5, 1, 2, 2, 2)


# product of Arbitary arguments
def product(*args: int) -> int:
    total = 1
    for i in args:
        total *= i
    return total


print(f"Product: {product(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}")


# check palindrome as arbitary arguments
def palindrome(*args: str) -> list[bool]:
    res: list[bool] = []
    for i in args:
        if i == i[::-1]:
            res.append(True)
        else:
            res.append(False)
    return res


print(f"Palindrome: {palindrome('madam', 'racecar', 'python', 'java')}")


# filter odd numbers
def filter_odd(*args: int) -> list[int]:
    res: list[int] = []
    for i in args:
        if i % 2 == 0:
            res.append(i)
    return res


print(f"Filter Odd: {filter_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}")


# calculate factorial
def fact(*nums: int) -> list[int]:
    res: list[int] = []
    for num in nums:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        res.append(factorial)
    return res


print(f"Factorial: {fact(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}")


# reverse list
def reverse_list(*args: int) -> list[int]:
    return list(reversed(args))


print(f"Reverse List: {reverse_list(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}")


# find prime numbers
def is_prime(num: int) -> bool:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    return False


def prime(*args: int) -> list[int]:
    res: list[int] = []
    for num in args:
        if is_prime(num):
            res.append(num)
    return res


print(f"Prime: {prime(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}")


# check anagram
# example arguments: anagram(('python', 'typhon'), ('java', 'avaj'))
# we will check if each pair of arguments are anagrams or not
def is_anagram(a: str, b: str) -> bool:
    return sorted(a) == sorted(b)


def anagram(*args: tuple[str, str]) -> list[bool]:
    res: list[bool] = []
    for pair in args:
        res.append(is_anagram(pair[0], pair[1]))
    return res


print(f"Anagram: {anagram(('python', 'typhon'), ('java', 'avaj'), ('hello', 'world'))}")


# convert celc to fahrenheit
def celc_to_fahr(*args: float) -> list[float]:
    res: list[float] = []
    for temp in args:
        res.append((temp * 9 / 5) + 32)
    return res


print(f"Celc to Fahr: {celc_to_fahr(0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100)}")


# calculate exponential
def exponential(num: int, *args: int) -> list[int]:
    res: list[int] = []
    for power in args:
        res.append(num**power)
    return res


print(f"Exponential: {exponential(2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}")


# sort strings by length
def sort_by_length(*args: str) -> list[str]:
    return sorted(args, key=len)


print(
    f"Sort by length: {sort_by_length('python', 'java', 'c', 'c++', 'javascript', 'typescript', 'go', 'rust', 'kotlin', 'swift', 'dart')}"
)


# find common elements from multiple lists as arbitary arguments
def common_elements(*args: list[int]) -> list[int]:
    res: list[int] = []
    for i in args[0]:  # i is first list
        for li in args:  # li is each list of lists
            if i not in li:
                break
            else:
                continue
        else:
            res.append(i)
    return res


print(
    f"Common Elements: {common_elements([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [2, 3, 4, 5], [3, 4, 5], [4, 5], [5])}"
)


# check prime factors
def prime_factors(num: int) -> list[int]:
    res: list[int] = []
    for i in range(2, num + 1):
        if num % i == 0:
            res.append(i)
    return res


def prime_factors_of_multiple(*args: int) -> list[list[int]]:
    res: list[list[int]] = []
    for num in args:
        res.append(prime_factors(num))
    return res


print(
    f"Prime Factors of Multiple: {prime_factors_of_multiple(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}"
)


# merge dictionaries
def merge_dicts(*args: dict[str, int]) -> dict[str, int]:
    res: dict[str, int] = {}
    for d in args:
        res.update(d)
    return res


print(
    f"Merge Dicts: {merge_dicts({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})}"
)
