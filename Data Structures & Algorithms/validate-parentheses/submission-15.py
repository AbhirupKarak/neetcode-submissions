class Solution:
    def isValid(self, s: str) -> bool:
        valid = {')' : '(', ']' : '[', '}' : '{'}
        st = []
        for char in s:
            if char in ['[', '{', '(']:
                st.append(char)
            elif char in [']', '}', ')']:
                if not st or valid.get(char) != st[-1]:
                    return False
                st.pop()
        return not st