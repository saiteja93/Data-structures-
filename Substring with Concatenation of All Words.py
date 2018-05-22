"""
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

"""

from collections import Counter, defaultdict
class Solution(object):
    def test(self, sub_str, word_len, ctr):
        i, seen = 0, defaultdict(int)
        while i < len(sub_str):
            next_word = sub_str[i:i+word_len]
            if next_word not in ctr or seen[next_word] == ctr[next_word]:
                return False
            seen[next_word], i = seen[next_word] + 1, i+word_len
        return True

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        start, end, result = 0, len(words)*len(words[0])-1, []
        ctr = Counter(words)
        while end < len(s):
            if self.test(s[start:end+1], len(words[0]), ctr):
                result.append(start)
            start, end = start+1, end+1
        return result

# Say length of each word is wl and we have wc words. total_len of substring = wl * wc
# Two pointer sliding window solution. Initialize a window [start, end] = [0, total_len-1]
# Now we slide through s and capture every substring. We then test if this substring is valid and meets our conditions.
# We prepare a frequency map of input words. We call it ctr.
# We initialize a dictionary called seen.
# Now we pick every word (called next_word) sequentially in our window. Note there will be only wc words each of length wl.
# If next_word is not in ctr then we know the window is invalid. If it is, but the frequency in seen is already equal to the frequency in ctr, then we know we have an extra occurence of this word in the window and the window is invalid. Otherwise, we increment its frequency in seen.
# If every word in this window is valid, then the entire window is valid.
# Time complexity: (len(s) - wl * wc) * wc or number_of_windows * words_per_window
# Space complexity: O(wc) + O(wc)
        
