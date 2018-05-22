"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
         # @return a string
    def minWindow(self, S, T):
        indices = {}
        for char in T:
            indices[char] = []
        miss = list(T)
        start = 0
        end = len(S)
        for i in range(len(S)):
            if S[i] in T:
                if S[i] not in miss and indices[S[i]] != []:
                    indices[S[i]].pop(0)
                elif S[i] in miss:
                    miss.remove(S[i])
                indices[S[i]].append(i)
            print indices
            if miss == []:
                maximum = max([x[-1] for x in indices.values()])
                minimum = min([x[-1] for x in indices.values()])
                if maximum-minimum+1 < end-start+1:
                    start = minimum
                    end = maximum
        if miss != []:
            return ""
        else:
            return S[start:end+1]
    #   Basically I kept a dictionary to record the index of each character of T. Each time I found a window, (when miss == []), I checked the length of this window by subtracting the maximum index and the minimum index of the characters. If this window is the smallest one so far, I record its beginning and ending index as “start” and “end.”
