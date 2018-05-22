"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""
"""
    The idea is to scan the string from left to right, keep track of the maximum length Non-Repeating Character Substring (NRCS) seen so far. Let the maximum length be max_len. When we traverse the string, we also keep track of length of the current NRCS using cur_len variable. For every new character, we look for it in already processed part of the string (A temp array called visited[] is used for this purpose). If it is not present, then we increase the cur_len by 1. If present, then there are two cases:

a) The previous instance of character is not part of current NRCS (The NRCS which is under process). In this case, we need to simply increase cur_len by 1.
b) If the previous instance is part of the current NRCS, then our current NRCS changes. It becomes the substring staring from the next character of previous instance to currently scanned character. We also need to compare cur_len and max_len, before changing current NRCS (or changing cur_len).

"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dic, start, maxlen = {}, 0, 0
        for a, b in enumerate(s):
            if b not in dic:
                #print a,start
                maxlen = max(maxlen, a - start + 1 )
            else:
                if dic[b] < start:
                    #print a,start, "less"
                    maxlen = max(maxlen, a - start + 1 )
                else:
                    start = dic[b]+1
                    #print a,start, "greater"
                    maxlen = max(maxlen, a - start + 1 )
            dic[b] = a
        return maxlen
