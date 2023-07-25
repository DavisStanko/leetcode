# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    s = sorted(s)
    t = sorted(t)
    for i in range(len(s)):
        if s[i] != t[i]:
            return False
    return True