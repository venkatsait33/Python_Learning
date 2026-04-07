# 🔥 What is [::-1] in Python?

# 👉 It is slicing syntax used to reverse a sequence (string, list, tuple).

# sequence[start : end : step]

# start → default (end of string)
# end → default (beginning)
# step → -1 (move backwards)

def reverse_string(s):
    return s[::-1]

print(reverse_string("Hello World"))

def reverse_string_manually(s):
    res = ""
    for char in s:
        res = char + res
    return res

print(reverse_string_manually("Hello World"))

#palindrome

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("madam"))

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))

def first_unique_char(s):
    for char in s:
        if s.count(char) == 1:
            return char

print(first_unique_char("leetcode"))