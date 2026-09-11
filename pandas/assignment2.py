# ---------------------------------------------------------------
# q1 answer
# ---------------------------------------------------------------

roll = "1024170352"
L = [int(d) * 10 for d in roll]

# i. Print L
print("i. L =", L)
# L = [10, 0, 20, 40, 10, 70, 0, 30, 50, 20]

# ii. Adding elements
L.append(90)
print("ii. after append(90):", L)
# append() adds 90 at the END of the list; length goes 10 -> 11, no index shifts

L.insert(2, 25)
print("ii. after insert(2, 25):", L)
# insert() places 25 AT index 2; every element from old index 2 onward shifts one place right

# iii. Removing elements
L.remove(10)
print("iii. after remove(10):", L)
# remove() deletes by VALUE - only the first matching 10 is deleted, returns nothing

popped = L.pop()
print("iii. after pop():", L, "| popped value =", popped)
# pop() deletes by INDEX (last one by default) and RETURNS the removed element

# iv. Sorting
L.sort()
print("iv. ascending :", L)
L.sort(reverse=True)
print("iv. descending:", L)
# sort() modifies L in place and returns None (use sorted(L) if you want a copy)

# v. Slicing
print("v. first three:", L[:3])
print("v. last three :", L[-3:])

# vi. List comprehension - elements greater than the average
avg = sum(L) / len(L)
above_avg = [x for x in L if x > avg]
print("vi. average =", avg, "| greater than average:", above_avg)


# ---------------------------------------------------------------
# q2 answer
# ---------------------------------------------------------------

# first 8 values of the ORIGINAL L from Q1 (before the edits above)
scores = tuple(int(d) * 10 for d in roll)[:8]
print("scores =", scores)
# scores = (10, 0, 20, 40, 10, 70, 0, 30)

# i. Highest / lowest
highest = max(scores)
lowest = min(scores)
print("i. highest =", highest, "at index", scores.index(highest))
print("i. lowest  =", lowest, "occurs", scores.count(lowest), "time(s)")

# ii. Reversing
reversed_list = list(scores[::-1])
print("ii. reversed as list:", reversed_list)
# A tuple is immutable, so it has no .reverse() method - we slice a NEW tuple and cast it to a list

# iii. Search for a user-entered score
target = int(input("iii. Enter a score to search: "))
if target in scores:
    print("iii.", target, "found at first index", scores.index(target))
else:
    print("iii.", target, "is not present in scores")

# iv. Trying to mutate a tuple
try:
    scores[0] = 100
except TypeError as e:
    print("iv. Error caught:", e)
# Tuples are immutable, so item assignment is not supported at all - a list allows L[0] = 100 because lists are mutable

# v. Unpacking with *
first, second, *rest = scores
print("v. first =", first, "| second =", second, "| rest =", rest)
# the starred name soaks up all leftover values and is always a LIST


# ---------------------------------------------------------------
# q3 answer
# ---------------------------------------------------------------

import random
from collections import Counter

random.seed(1024170352)   # my roll number -> same "random" list every run, unique to me

# i. 100 random numbers between 100 and 900 inclusive
nums = [random.randint(100, 900) for _ in range(100)]
print("i. numbers:", nums)

# ii. Odd numbers
odds = [n for n in nums if n % 2 != 0]
print("ii. odd count =", len(odds), "| odds:", odds)

# iii. Even numbers
evens = [n for n in nums if n % 2 == 0]
print("iii. even count =", len(evens), "| evens:", evens)

# iv. Prime numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):   # checking up to sqrt(n) is enough
        if n % i == 0:
            return False
    return True

primes = [n for n in nums if is_prime(n)]
print("iv. prime count =", len(primes), "| primes:", primes)

# v. Most frequent number
freq = Counter(nums)
value, times = freq.most_common(1)[0]
print("v. most frequent number =", value, "| occurs", times, "time(s)")
# ---------------------------------------------------------------
# q4 answer
# ---------------------------------------------------------------

roll = "1024170352"
digits = [int(d) for d in roll[:8]]        # [1, 0, 2, 4, 1, 7, 0, 3]

A = {d * 7 for d in digits}
B = {d * 9 for d in digits}
print("A =", A)      # {0, 7, 14, 21, 28, 49}   (duplicates collapse automatically)
print("B =", B)      # {0, 9, 18, 27, 36, 63}

# vi. Union - every unique value in either set
print("vi. union:", A | B)          # or A.union(B)

# vii. Intersection - values present in both
print("vii. intersection:", A & B)  # or A.intersection(B)  -> {0}

# viii. Differences, each direction separately
print("viii. A - B:", A.difference(B))   # in A but not in B
print("viii. B - A:", B.difference(A))   # in B but not in A
# difference() is one-directional (what A has that B lacks); symmetric_difference() is both directions at once

# ix. Symmetric difference - in exactly one of the two sets
print("ix. symmetric difference:", A.symmetric_difference(B))   # or A ^ B

# x. Subset / superset checks
print("x. A.issubset(B)   =", A.issubset(B))     # False - A has 7, 14, ... which B lacks
print("x. B.issuperset(A) =", B.issuperset(A))   # False - same reason, mirrored

# xi. Safe removal
X = int(input("xi. Enter a value to remove from A: "))
A.discard(X)
print("xi. A after discard:", A)
# discard() does nothing if the value is absent, while remove() raises KeyError - safer when existence is uncertain


# ---------------------------------------------------------------
# q5 answer
# ---------------------------------------------------------------

my_dict = {
    "name": "Rithik",
    "roll_no": "1024170352",
    "branch": "CSE",
    "age": 20,                # <- put your real age
    "city": "Patiala"         # <- put your real home city
}
print("original:", my_dict)

# i. Rename "city" -> "location", keeping the value (generic, works for any dict)
my_dict["location"] = my_dict.pop("city")
print("i.", my_dict)
# pop() returns the value while deleting the key, so it can be re-assigned under the new name in one line

# ii. Add a new key
my_dict["cgpa"] = 8.5         # <- put your real CGPA
print("ii.", my_dict)

# iii. Increase age by 1
my_dict["age"] += 1           # same as my_dict["age"] = my_dict["age"] + 1
print("iii.", my_dict)

# iv. Two ways of deleting, on two separate copies
copy1 = my_dict.copy()
copy2 = my_dict.copy()

removed = copy1.pop("branch")
print("iv. copy1 after pop():", copy1, "| pop returned:", removed)

del copy2["branch"]
print("iv. copy2 after del  :", copy2)
# pop() RETURNS the deleted value (and accepts a default if the key is missing); del is a statement that returns nothing and raises KeyError if absent

# v. Iterate with .items()
print("v. key-value pairs:")
for key, value in my_dict.items():
    print(f"   {key} -> {value}")

# vi. Safe key access
if "email" in my_dict:
    print("vi. email:", my_dict["email"])
else:
    print("vi. 'email' key not found - no email on record")
# checking with `in` avoids the KeyError that my_dict["email"] would raise

# vii. Merging two dictionaries
friend_dict = {
    "name": "Aarav",
    "roll_no": "1024170399",
    "branch": "ECE",
    "age": 21,
    "location": "Ludhiana"
}
merged = {**my_dict, **friend_dict}
print("vii. merged:", merged)
# on a key clash the RIGHTMOST dict wins, so friend_dict's values overwrite mine here

# viii. Keep only string-valued pairs
strings_only = {k: v for k, v in my_dict.items() if isinstance(v, str)}
print("viii. string values only:", strings_only)
