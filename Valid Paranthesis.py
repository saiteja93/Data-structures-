"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

"""

def isValid(self, s):
        tup = {"}":"{", "]":"[", ")":"("}
        stack = []
        for i in s:
            if i in tup.values():
                stack.append(i)
            else:

                if len(stack) == 0 or stack.pop() != tup[i] : return False

        return len(stack) == 0
    
