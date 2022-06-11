def solution(string):
    # count the number of each individual character
    # can form a palindrome only if:
    # at most one of the character counts is odd, all others must be even 
    return sum([string.count(l)%2 for l in set(string)]) <= 1
